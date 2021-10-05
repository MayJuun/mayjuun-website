---
title: "WVEMS Protocols - Interactive, Searchable PDFs"
date: 2021-10-05T20:58:00Z
type: post
image: images/blog/8-wvems-protocols/wvems-protocols-ios.png
author: John Manning, MD, FAMIA, FACEP
tags: ["wvems","flutter","protocols","projects"]
---

## Intro -

Today (Oct 5, 2021), we at MayJuun are proud to officially release the WVEMS Protocols Flutter app on the [Apple App Store](https://apps.apple.com/ca/app/wvems-protocols-operational/id1437286516) and the [Google Play Store](https://play.google.com/store/apps/details?id=com.WVEMSProtocols).

This was a wonderful project built in collaboration with the [Western Virginia Emergency Medical Services Council, Inc](https://western.vaems.org/), who provides Emergency Medical Services (EMS) in the state of Virginia...specificially in the following 7 cities:

- Covington
- Danville
- Martinsville
- Radford
- Roanoke
- Salem

and 12 counties:

- Alleghany
- Craig
- Botetourt
- Floyd
- Franklin
- Giles
- Henry
- Montgomery
- Roanoke
- Patrick
- Pittsylvania
- Pulaski

Having lived (and trained) in the region for several years, I am both personally and professionally satisfied to have played a small part in this region's ability to provide Acute Unscheduled Care to their community. Opportunities like this are why I picked a career in informatics.

Our efforts aren't over, however. This collaborative was intentionally built in an [open-source](https://github.com/MayJuun/wvems_protocols) format, meaning any who want to mirror our efforts are welcome ([MIT License](https://github.com/MayJuun/wvems_protocols/blob/main/LICENSE)). The content within each PDF are also freely available from WVEMS Council, Inc, under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license. We are happy to work with any who may want to build interactive PDFs and display similar content in a searchable, cross-platform manner.

Interestingly, this was also the first time our company had a client [directly contribute](https://github.com/MayJuun/wvems_protocols/graphs/contributors) to our code while we were actively building and optimizing the interfaces they wanted. That was REALLY fun to do, and absolutely helped add to the collaborative vibe. I hope that gains traction as well.

Without further ado...here is the finished product:

{{< figure src="/images/blog/8-wvems-protocols/wvems-demo.gif" width="50%" >}}

## Features (in Flutter)

For this project, we built an open-source cross-platform Flutter app with the following features:

- Open PDFs via the [flutter_pdfview](https://pub.dev/packages/flutter_pdfview) package
- Search within PDFs using [JSON as a shortcut](https://mayjuun.com/blog/5-pdf-2-json/) to load text data more quickly, and using [material_floating_search_bar](https://pub.dev/packages/material_floating_search_bar) to display search results
- Firebase authentication (anonymous) and Firebase cloud storage, via [FlutterFire](https://firebase.flutter.dev/), so that you could download prior iterations of these protocols (including the original 2019 protocol)
- Firebase cloud messaging, so the EMS agency can send the occasional push notification to its users
- Error and state handling via [freezed](https://pub.dev/packages/freezed)
- Built using the [Get MVC+S Architecture](https://mayjuun.com/blog/2-get-fluttered-mvcs/)

## Features (outside Flutter)

We also created custom WVEMS logos that allow us to display the app in light / dark modes, with background images removed.

{{< figure src="/images/blog/8-wvems-protocols/wvems_logo_light.png" width="50%" >}}

{{< figure src="/images/blog/8-wvems-protocols/wvems_logo_dark.png" width="50%"  >}}

Finally, we set our PDF content + metadata in a standard manner, with resources accessed both inside the [assets folder](https://github.com/MayJuun/wvems_protocols/tree/main/assets/2021-WVEMS-Protocols) and outside (e.g. in Firebase Storage). This allows you to dynamically load folders from the cloud, so that you can add new PDF content dynamically without having to make any changes to your code. Put differently, this allows for an offline-first app that can still be updated via the cloud...but does not require any internet connectivity for day-to-day operations and works 'out of the box' on first install of the app. That was an important feature.

## Closing Thoughts

I am happy to go into any of these features in depth, or to create some additional posts/videos with lessons learned. As with before, the objective is to always push the needle forward, reflect on lessons learned, and continue pushing.

I subscribe heavily to the "[Yes and...](https://www.fastcompany.com/3042080/yes-and-5-more-lessons-in-improv-ing-collaboration-and-creativity-from-second-city)" mentality, and particularly to Second City's saying: "All of us is better than one of us."  This project was truly a collaborative. My only hope is that future projects share in this collaborative culture and sense of community.

To my friends in Western Virginia, take care out there. Hopefully, this app will help.

--John
