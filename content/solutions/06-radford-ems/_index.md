---
title: Radford EMS Protocols
description: Interactive, searchable PDFs
type: solutions
date: 2022-07-06T13:19:42Z
image: solutions/06-radford-ems/images/radford-home.png
client: Radford EMS Commission
releaseDate: Sept 27, 2022
location: Virginia
links: 
  - title: Apple - App Store
    url: https://apps.apple.com/gb/app/radfordems/id1629242084
  - title: Google - Play Store
    url: https://play.google.com/store/apps/details?id=com.mayjuun.radford.ems
  - title: More Info
    url: https://www.radfordva.gov/174/Radford-Emergency-Medical-Services-Commi
policies:
  - title: Privacy Notice
    url: privacy-notice
  - title: EULA
    url: eula
categories: ["open source","EMS","PDF"]

---
## 2023 Update -

This solution was featured as part of the Nov 2022 [IHE USA](https://www.iheusa.org/) Path to Production series (#6). That video is available here:

{{< youtube ga4atnRC8pQ >}}

## Radford EMS Protocols -

The Radford EMS Protocols app is a cross-platform Flutter app designed to quickly view, interact, and search through PDFs. The app allows EMTs to access the guidelines and protocols necessary for on-shift patient care.

This app builds heavily on the use of interactive PDFs. For example, a separate PDF exists for each year the protocol was updated / released. For future projects, additional PDFs may be created to satisfy different needs, such as locations, agencies, clinical settings, etc.

## Customization / Scalability

- All features in the Radford EMS Protocols app are similar to our [WVEMS Protocols](/solutions/03-wvems-protocols/) app, given they are both based on the same [open-source backbone](https://github.com/MayJuun/wvems_protocols).

- If you are interested in harnessing your own PDF guidelines and protocols, [contact us](/contact/) and we can discuss pricing.

## Features

- `Navigate` between pages using links on the Table of Contents or swiping up / down. Click on underlined text to go to a linked page. Press the `Home` key to go back to the Table of Contents

- Click the `settings` icon to download other PDFs or to change between light / dark themes

- This feature uses Firebase authentication and Firebase cloud storage, via [FlutterFire](https://firebase.flutter.dev)

- Use the bar at the top to `search PDF content`, including a history of your last 10 searches

- `Firebase cloud messaging` makes it so that the EMS agency can send the occasional push notification to its users

{{< figure src="images/radford-home.png" class="img-center" height="500" >}}

{{< figure src="images/radford-settings.png" class="img-center" height="500" >}}

{{< figure src="images/radford-messages.png" class="img-center" height="500" >}}
