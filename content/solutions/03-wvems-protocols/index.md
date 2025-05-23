---
title: WVEMS Protocols
description: Interactive, searchable PDFs
type: solutions
date: 2021-11-27T22:54:27Z
image: solutions/03-wvems-protocols/images/demo-wvems-protocols.gif
client: Western Virginia Emergency Medical Services Council, Inc.
releaseDate: Oct 5, 2021
location: Virginia
links: 
  - title: Apple - App Store
    url: https://apps.apple.com/ca/app/wvems-protocols-operational/id1437286516
  - title: Google - Play Store
    url: https://play.google.com/store/apps/details?id=com.WVEMSProtocols
  - title: GitHub - Source Code
    url: https://github.com/MayJuun/wvems_protocols
  - title: More Info
    url: https://wvems.org
categories: ["open source","EMS","PDF"]

---

## 2023 Update -

This solution was featured as part of the Nov 2022 [IHE USA](https://www.iheusa.org/) Path to Production series (#6). That video is available here:

{{< youtube ga4atnRC8pQ >}}

## WVEMS Protocols -

The WVEMS Protocols app is a cross-platform Flutter app designed to quickly view, interact, and search through PDFs. It is being used clinically in 7 cities and 12 counties in southwest Virginia. The app allows EMTs to access the guidelines and protocols necessary for on-shift patient care. In the first month of release alone, the app was installed on 1,200 Android phones and iPhones.

This app builds heavily on the use of interactive PDFs. For example, a separate PDF exists for each year the protocol was updated / released. For future projects, additional PDFs may be created to satisfy different needs, such as locations, agencies, clinical settings, etc.

The app is fully [open-source](https://github.com/MayJuun/wvems_protocols) and may be modified to view any type of PDF. We strongly suggest using PDFs with `embedded links` so you can more easily swap from one page in the PDF to another. If any interest exists to have a custom-built app that displays your own PDF content, or to have a similar setup for your own needs, email us at info@mayjuun.com and we can work with you.

If you need help creating / modifying your own PDFs as well, just let us know. The PDFs found in the WVEMS Protocols app fall under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) license, so if you wanted to adapt and modify some of this existing content to match your own needs...you are welcome to do so as long as you provide attribution to the WVEMS Council, Inc and you keep your derivative content under the same license. Similarly, if you use your own PDF from scratch, you are welcome to put it under any license you want.

## Features

- PDFs are loaded automatically via the [flutter_pdfview](https://pub.dev/packages/flutter_pdfview) package

{{< figure src="images/wvems-protocols-1.png" class="img-center" height="500" >}}

- `Navigate` between pages using links on the Table of Contents or swiping up / down. Click on underlined text to go to a linked page. Press the `Home` key to go back to the Table of Contents

{{< figure src="images/wvems-protocols-2.png" class="img-center" height="500" >}}

- Click the `settings` icon to download other PDFs or to change between light / dark themes
- This feature uses Firebase authentication and Firebase cloud storage, via [FlutterFire](https://firebase.flutter.dev)

{{< figure src="images/wvems-protocols-3.png" class="img-center" height="500" >}}

- Use the bar at the top to `search PDF content`, including a history of your last 10 searches

{{< figure src="images/wvems-protocols-4.png" class="img-center" height="500" >}}

- `Share this app` with others using a single QR code, or download / share the PDFs directly

{{< figure src="images/wvems-protocols-5.png" class="img-center" height="500" >}}

- `Firebase cloud messaging` makes it so that the EMS agency can send the occasional push notification to its users

{{< figure src="images/wvems-protocols-6.png" class="img-center" height="500" >}}
