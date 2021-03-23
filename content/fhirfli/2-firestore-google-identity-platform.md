---
title: "Hipaa Compliant Login with Google's Firestore"
date: 2021-03-15T15:24:35Z
type: post
author: Grey Faulkenberry, MD MPH
tags: ["Flutter","FHIR","Firestore", "Identify Platform", "HIPAA"]
---

## Firestore, Google Identify Platform and HIPAA

Firestore is a great resource (especially for startups and smaller organizations - the free data tier offers a LOT of benefits), it is also [HIPAA compliant](https://cloud.google.com/security/compliance/hipaa-compliance). If you look on that list, you will find ***Cloud Firestore*** but NOT ***Firebase***. Meaning anything outside the scope of Firestore that falls into the realm of Firebase may not offically be able to be called HIPAA Compliant (note, HIPAA Compliance is NOT explicitly defined, and is actually a legal definition, not a technial one). Nonetheless, you will not be able to get a BAA with Google if you use services not listed above.

That's the long winded version of, we can use Firestore for data storage, but we need something else for authentication. Namely, Google's Identify Platform. So mostly for my benefit, but in case anyone else is interested, I'm going to walk through how to create a HIPAA Compliant login mechanism using [Google and Firestore](https://cloud.google.com/solutions/authenticating-users-to-firestore-with-identity-platform-and-google-identities). Btw, after going through this process, it's essentially the same thing. As far as I can tell, the only real issue difference is that firebase auth is done through firebase, Google's Identity Platform you do through the Google Cloud Console. 

This will not be a tutorial on Google Cloud (although I may consider that at some point in the future). So I'm going to assume you have a GCP account, and have created a project. Select that project, and then go to the hamburger icon at the top left, and choose ***APIs & Services***. At the bottom of this page, you'll need to look and see if Datastore or AppEngine is listed. If they are, click on them, and then there should be an option to Disable API. You may need to disable other APIs in the process, but this apparently is required. Also, if you've already created a Firestore database with security rules, these will be overwritten, so it's probably best to do this in a new project, or one you don't care about.

Next, go to the Identify Platform Marketplace Page. You should be able to search for it in GCP, use the link above and they have a direct link for it, or go to ***APIs & Services*** >> ***Library***, and search it there. Activate it, then go through the same process for Firestore. Click **Select Native Mode** and **Create Database**.

Now, you will need multiple tabs. One you should already have for Firestore [TAB1], and you're going to open one for Identify Platform, one for APIs & Services, and eventually another for the Firestore Console. 
### Identity Platform
- [TAB2]
- Click **Providers** for Identify Platform, and then **ADD A PROVIDER**
- Select Google
- Click the ***APIs and Services Link***
- [TAB3]
- Go to the ***Credentials*** page
- Under **OAuth 2.0 Client IDs** there should be one with the name **Web client (auto created by Google Service), open this
- On the top right, you should be able to see a **Client ID** and a **Client Secret**, you will need both of these
- Do not close that tab, but return to the ***New Identity Provider*** tab
- Copy and paste the **Client ID** and **Client Secret** into the fields for **Web Client ID** and **Web Client Secret**
- Click Save
- Return back to the Credentials tab, and click ***OAuth consent screen***, and then ***External*** and ***Create***
- Enter an app name (this will be displayed to your users) a user support email, and an Email address at the bottom
- Click ***Save and Continue*** at the bottom, and again, and again, and finally ***BACK TO DASHBOARD***
- Go back to the Identity Platform tab, click **ADD A PROVIDER**, this time select Email / Password, and make sure it's enabled.
- Click Save

### Firestore
- Go to [TAB4][Firestore](https://console.firebase.google.com/) - that link may not work. You may need to use the one on the Google instructions for this tutorial, or just search for it yourself. Seriously, do I have to do everything?
- Select the project that you have been working with in the GCP console
- Click **Firestore** and then **Start Collection**
- I tend to title this collection "users" because this is where you're going to make a list of your users, but you can name it whatever you want
- In the Document ID put an email (yours or make one up)
- Create a Field name "Name" and enter a name
- Enter a Field name "Company" and enter a company
- Do this a couple of times, at least once enter your name and email
- Click **Save**
- Select the **Rules** tab 
- Copy and paste the following over it

```
rules_version = '2';
service cloud.firestore {
 match /databases/{database}/documents { 
  match /users/{userID} {
  allow read:
   if request.auth.uid != null
     && (request.auth.token.firebase.sign_in_provider == "google.com" ||
     request.auth.token.firebase.sign_in_provider == "password")
     && request.auth.token.email == userID
    }
  }
}
```
- Then select **Publish**
- This will allow a user to get their information, but only if it's their customerId (their email) and they've logged in using either google or their username and password (we can create a password in a later section)

### Flutter & Android
- Alright, now we're getting somewhere
- In whatever flutter project you're using, first take a look at your pubspec.yaml
- For this tutorial, you'll need to include all of the following
```
environment:
  sdk: '>=2.12.1 <3.0.0'

dependencies:
  cloud_firestore: ^1.0.1
  firebase_auth: ^1.0.1
  firebase_core: ^1.0.1
  google_sign_in: ^5.0.1
```
- Next up, check out your ```android/build.gradle``` file, and add the following
```
buildscript {
  dependencies {
    // ... other dependencies
    classpath 'com.google.gms:google-services:4.3.3'
  }
}
```
- FYI that section in mine looks like this:
```
buildscript {
    dependencies {
        classpath 'com.android.tools.build:gradle:3.5.0'
        classpath 'com.google.gms:google-services:4.3.5'
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
    }
}
```
- Open ```android/app/build.gradle``` and you'll need to add the google services line, mine looks like this:
```
apply plugin: 'com.android.application'
apply plugin: 'kotlin-android'
apply plugin: 'com.google.gms.google-services'
apply from: "$flutterRoot/packages/flutter_tools/gradle/flutter.gradle"
```
- Under defaultConfig, make sure that the minSdkVersion is at least 21
- Go back to the Firestore Console, and on the Project Overview page, below the **Get started by adding Firebase to your app** section, click the Android.
- The android package name is in ```android/app/build.gradle``` as the applicationId
- App nickname is what it will be called when displayed to the user
- The SHA-1 password isn't required, but if you want dynamic links or phone authentication, it is (I just include it in case)
- ```$ keytool -list -v \ -alias androiddebugkey -keystore ~/.android/debug.keystore```
- that should provide some text, one line of which should look like (but alphanumeric)
```
SHA1: AA:BB:CC:DD:EE:FF:GG:HH:II:JJ:KK:LL:MM:NN:OO:PP:QQ:RR:SS:TT
```
- Copy and put in the Debug signing certificate SHA-1 field
- Click ***Register App**
- Then download the file offered, called ```google-services.json```
- Place this file in your ```android/app/``` directory (and remember to add it to .gitignore if you're building this somewhere public like github)
- Click ***Next*** and follow all instructions. We should have done all of them except for adding the dependencies at the bottom of ```android/app/build.gradle```
- For us, we need to add:
```
    implementation platform('com.google.firebase:firebase-bom:26.7.0')
    implementation 'com.google.firebase:firebase-auth'
    implementation 'com.google.firebase:firebase-firestore'
```
- Add any other firebase services you want, like analytics
- Rebuild your flutter project (flutter create)
- Click next and continue to Console

### Flutter & iOS
- Setup is the same as above for dependencies
- Actually, I'll have to come back to this