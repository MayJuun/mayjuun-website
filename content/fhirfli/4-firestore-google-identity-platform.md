---
title: "Hipaa Compliant Login with Google's Firestore"
date: 2021-03-15T15:24:35Z
type: post
author: Grey Faulkenberry, MD MPH
tags: ["Flutter","FHIR","Firestore", "Identify Platform", "HIPAA"]
---

## Firestore, Google Identify Platform and HIPAA

Firestore is a great resource (especially for startups and smaller organizations - the free data tier offers a LOT of benefits), it is also [HIPAA compliant](https://cloud.google.com/security/compliance/hipaa-compliance). If you look on that list, you will find ***Cloud Firestore*** but NOT ***Firebase***. Meaning anything outside the scope of Firestore that falls into the realm of Firebase may not offically be able to be called HIPAA Compliant (note, HIPAA Compliance is NOT explicitly defined, and is actually a legal definition, not a technial one). Nonetheless, you will not be able to get a BAA with Google if you use services not listed above.

That's the long winded version of, we can use Firestore for data storage, but we need something else for authentication. Namely, Google's Identify Platform. So mostly for my benefit, but in case anyone else is interested, I'm going to walk through how to create a HIPAA Compliant login mechanism ~~using [Google and Firestore](https://cloud.google.com/solutions/authenticating-users-to-firestore-with-identity-platform-and-google-identities)~~. The information on that link seems to be outdated, and makes this much harder than it actually needs to be.

This will not be a tutorial on Google Cloud (although I may consider that at some point in the future). So I'm going to assume you have a GCP account, and have created a project. Select that project, and then go to the hamburger icon at the top left, and choose ***APIs & Services***. Select **Library** and then choose and activate Firestore. Go ahead and open up Firestore in GCP (this is different than the Firestore Console). Click **Select Native Mode** and **Create Database**.

### Firestore
- Go to [Firestore](https://console.firebase.google.com/) - that link may not work. You may need to use the one on the Google instructions for this tutorial, or just search for it yourself. Seriously, do I have to do everything?
- Select the project that you have been working with in the GCP console, or if you don't see it, click add new project and select it
- Click through the options, I just keep all of the defaults
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
- Return to **Project Overview**
- Below the **Get started by adding Firebase to your app** section, click the Android.
- The android package name is in the file: ```android/app/build.gradle``` as the applicationId
- App nickname is what it will be called when displayed to the user
- The SHA-1 password isn't required, but if you want dynamic links or phone authentication, it is (I just include it in case)
- ```$ keytool -list -v \
-alias androiddebugkey -keystore ~/.android/debug.keystore```
- that should provide some text, one line of which should look like (but alphanumeric)
```
SHA1: AA:BB:CC:DD:EE:FF:GG:HH:II:JJ:KK:LL:MM:NN:OO:PP:QQ:RR:SS:TT
```
- Copy and put in the Debug signing certificate SHA-1 field
- Click ***Register App**
- Don't download the file just yet though
- Click through, and make sure all of the changes suggested are changed in your files
- Of note, on the bottom of ```android/app/build.gradle``` mine looks like this:
```
dependencies {
    implementation "org.jetbrains.kotlin:kotlin-stdlib-jdk7:$kotlin_version"
    implementation platform('com.google.firebase:firebase-bom:26.7.0')
    implementation 'com.google.firebase:firebase-auth'
    implementation 'com.google.firebase:firebase-firestore'
    implementation 'com.google.firebase:firebase-analytics-ktx'
}
```
- Yours make not look exactly like that, but it should look similar
- Click **Authentication** on the left, and then **Sign-in method**, you can choose any of them, but for our purposes, choose Email/Password and Google
- In Google, you will need to specify a support email address, and then you can download the google-services.json file
- Place this file in your ```android/app/``` directory (and remember to add it to .gitignore if you're building this somewhere public like github)

### GCP
- A few more steps are required in GCP
- You'll need to find Identity Platform. I found it difficult to find from the console actually, so you may be better of trying [here](https://cloud.google.com/identity-platform#:~:text=Identity%20Platform%20is%20a%20customer,with%20confidence%20on%20Google%20Cloud)
- It should say ***Identity Platform***, if it says anything else, it's not what you want.
- Click ***Enable Identity Platform***
- It may ask if you want to upgrade your project, say yes
- Make sure you see Google and Email/Password
- FYI, you can override a user's account by entering their email with a password. So if you entered annoyingUser@gmail.com as one of the users in the firestore collection, and then entered an email with a password for them, they would not be able to login with their google account, and would instead have to use the password you created.


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
- If you weren't following along earlier, make sure the following is in your files as well:
- ```android/build.gradle``` add the following
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
- ```android/app/build.gradle``` and you'll need to add the google services line, mine looks like this:
```
apply plugin: 'com.android.application'
apply plugin: 'kotlin-android'
apply plugin: 'com.google.gms.google-services'
apply from: "$flutterRoot/packages/flutter_tools/gradle/flutter.gradle"
```
- Under defaultConfig, make sure that the minSdkVersion is at least 21
- And again, the bottom of mine looks like this:
```
dependencies {
    implementation "org.jetbrains.kotlin:kotlin-stdlib-jdk7:$kotlin_version"
    implementation platform('com.google.firebase:firebase-bom:26.7.0')
    implementation 'com.google.firebase:firebase-auth'
    implementation 'com.google.firebase:firebase-firestore'
    implementation 'com.google.firebase:firebase-analytics-ktx'
}
```
- Rebuild your flutter project (flutter create)
- Click next and continue to Console

### Flutter & iOS
- Setup is the same as above for dependencies
- Actually, I'll have to come back to this

