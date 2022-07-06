---
draft: true
title: Radford EMS Protocols
description: Interactive, searchable PDFs
type: portfolio
date: 2022-07-06T13:19:42Z
image: portfolio/6-radford-ems/images/demo-radford-protocols.gif
client: Radford EMS Commission
releaseDate: Oct 5, 2021
location: Virginia
links: 
  - title: More Info
    url: https://www.radfordva.gov/174/Radford-Emergency-Medical-Services-Commi
categories: ["open source","EMS","PDF"]

---
## Radford EMS Protocols -

The Radford EMS Protocols app is a cross-platform Flutter app designed to quickly view, interact, and search through PDFs. The app allows EMTs to access the guidelines and protocols necessary for on-shift patient care.

This app builds heavily on the use of interactive PDFs. For example, a separate PDF exists for each year the protocol was updated / released. For future projects, additional PDFs may be created to satisfy different needs, such as locations, agencies, clinical settings, etc.

The app is fully [open-source](https://github.com/MayJuun/radford_ems) and may be modified to view any type of PDF. We strongly suggest using PDFs with `embedded links` so you can more easily swap from one page in the PDF to another. If any interest exists to have a custom-built app that displays your own PDF content, or to have a similar setup for your own needs, email us at info@mayjuun.com and we can work with you.

If you need help creating / modifying your own PDFs as well, just let us know. The PDFs found in the Radford EMS Protocols app fall under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) license, so if you wanted to adapt and modify some of this existing content to match your own needs...you are welcome to do so as long as you provide attribution to the Radford EMS Commission, and you keep your derivative content under the same license. Similarly, if you use your own PDF from scratch, you are welcome to put it under any license you want.

## Features

- PDFs are loaded automatically via the [flutter_pdfview](https://pub.dev/packages/flutter_pdfview) package

{{< figure src="images/Radford-protocols-1.png" class="img-center" height="500" >}}

- `Navigate` between pages using links on the Table of Contents or swiping up / down. Click on underlined text to go to a linked page. Press the `Home` key to go back to the Table of Contents

{{< figure src="images/radford-home.png" class="img-center" height="500" >}}

- Click the `settings` icon to download other PDFs or to change between light / dark themes
- This feature uses Firebase authentication and Firebase cloud storage, via [FlutterFire](https://firebase.flutter.dev)

{{< figure src="images/radford-settings.png" class="img-center" height="500" >}}

- Use the bar at the top to `search PDF content`, including a history of your last 10 searches

{{< figure src="images/Radford-protocols-4.png" class="img-center" height="500" >}}

- `Firebase cloud messaging` makes it so that the EMS agency can send the occasional push notification to its users

{{< figure src="images/radford-messages.png" class="img-center" height="500" >}}
