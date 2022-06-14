---
title: ACEP emPOC
description: Emergency Medicine - Point of Care
type: portfolio
date: 2021-12-10T00:07:59Z
image: portfolio/4-acep-empoc/images/demo-acep-empoc.gif
client: American College of Emergency Physicians (ACEP)
releaseDate: Dec 6, 2021
location: USA
links: 
  - title: Apple - App Store
    url: https://apps.apple.com/us/app/acep-empoc/id1460691785#?platform=iphone
  - title: Google - Play Store
    url: https://play.google.com/store/apps/details?id=org.acep.em_poc
  - title: More Info
    url: https://www.acep.org/patient-care/point-of-care-tools
categories: ["cloud updates","Firebase","JSON"]

---
## ACEP emPOC -

The American College of Emergency Physicians (ACEP) Emergency Medicine Point of Care (emPOC) app is a cross platform application designed to provide evidence-based, Emergency Medicine clinical content in a point-of-care tool designed for use at the bedside. Content within this app is curated from the field's top experts and thought leaders. A web version of this content is available separately on [ACEP's website](https://www.acep.org/patient-care/point-of-care-tools).

For the Android and iOS Flutter release of emPOC (Dec '21), we rebuilt emPOC from scratch in collaboration with ACEP's staff. We are harnessing Firebase as our cloud-hosted backend to allow for synchronized distribution of content updates (when relevant) without the need to publish changes to the app's code each time a new tool is created.

We also identified a need to build a high-quality `content management system (CMS)` that leans into the native strengths inherent to Firebase, so we created a means to connect spreadsheet data to Firebase via the [JSON standard](https://www.json.org/json-en.html). This made it far easier to add and update emPOC content into Firebase.

If you have an app idea that requires dynamically-displayed layouts and online / offline sync of content with the cloud, then our efforts with emPOC may serve as a good starting point.

## Features

- To access this tool, you must first login via ACEP's Single Sign On

{{< figure src="images/acep-empoc-1.png" class="img-center" height="500" >}}

- The re-launch of the app includes twelve point of care bedside tools. You can `create additional tools via the cloud (Firebase)` without adding new code. The app will then dynamically display new tools / content

{{< figure src="images/acep-empoc-2.png" class="img-center" height="500" >}}

- App information, acknowledgements, and tables are displayed as `dismissible dialogs`

{{< figure src="images/acep-empoc-3.png" class="img-center" height="500" >}}

- Clicking on a tool will show `custom content, icons, and headings` as determined by Firebase

{{< figure src="images/acep-empoc-4.png" class="img-center" height="500" >}}

- Within each heading, you may `expand/collapse content` and quickly swap to `other headings`

{{< figure src="images/acep-empoc-5.png" class="img-center" height="500" >}}

- All content are displayed dynamically, including the `background colors` for each tool

{{< figure src="images/acep-empoc-6.png" class="img-center" height="500" >}}

- emPOC also includes `custom / advanced JSON specifications` to display videos, hyperlinks, and (some) HTML formatting. As noted above, all of these are specified via a Google spreadsheet, thereby optimizing the means by which additional information is added / updated into Firebase

{{< figure src="images/acep-empoc-7.png" class="img-center" height="500" >}}
