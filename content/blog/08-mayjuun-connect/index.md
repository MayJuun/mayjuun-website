---
title: "MayJuun Connect - Add Contacts via QR Code"
date: 2022-03-15T00:07:34Z
type: post
image: images/blog/08-mayjuun-connect/mayjuun-connect-1.png
author: John Manning, MD, FAMIA, FACEP
tags: ["howto", "flutter", "networking", "qr codes"]
---

## Intro -

When flying to a conference, I had inspiration to optimize the means by which my contact information is shared with others. Building apps like these are well within our wheelhouse at MayJuun, and this step seemed like a nice upgrade from the basic business card.

Credit where it's due, this app builds heavily upon the open-source (MIT License) QR Code generator library called [Project Nayuki](https://www.nayuki.io/page/qr-code-generator-library). I've used their code-generator in a number of projects and recommend them highly.

## QR Code 'Business Card'

For the main part of this app, I took the VCard specification, looked around through a number of websites that describe VCards in detail -- including [this site's VCard example](https://shirishgupta.com/10-common-vcard-mistakes/) and [Wikipedia's version comparison](https://en.wikipedia.org/wiki/VCard) -- and set about to create my own custom VCard.

In my research, I noticed a few websites that provided a QR Codes to download a custom VCard from the web, which generates traffic (+ analytics) to that site and is purely dependent on that site remaining up. This method doesn't use that at all. Since I am directly putting my info directly into a QR Code, someone can use this code even without an internet connection.

Note as well that as of March 2022, when you are using a QR code to directly add a contact (versus external website redirect + download)...not all of the items available in a VCard will cross over. I tested each element by hand on Android and iOS and found that the following fields work well for both devices:

```text
BEGIN:VCARD
VERSION:4.0
N:xxLASTNAMExx;xxFIRSTNAMExx;;;
FN:xxFIRSTNAME LASTNAMExx
ORG:xxYOUR ORGxx
TITLE:xxYOUR TITLExx
TEL;type=MOBILE:xxYOURPHONENUMBERXX
EMAIL:xxYOUREMAILADDRESSxx
URL:xxYOURWEBSITExx
NOTE:xxYOURPERSONALIZEDNOTExx
END:VCARD
```

Anything in the above code that begins and ends with `xx` needs to be replaced by you. For my purposes, the QR Code from this image:

{{< figure src="/images/blog/08-mayjuun-connect/mayjuun-connect-1.png" width="40%" >}}

was generated using these lines of code:

```text
BEGIN:VCARD
VERSION:4.0
N:Manning;John;;;
FN:John Manning
ORG:MayJuun LLC
TITLE:CEO
TEL;type=MOBILE:(865) 300-7738
EMAIL:john.manning@mayjuun.com
URL:https://mayjuun.com
NOTE:John Manning, MD, FAMIA, FACEP  ~  Pronouns: he / him / his  ~  Chief Executive Officer (CEO) @ MayJuun  ~  Clinical: Informatics, Emergency Medicine  ~  Dev: Dart/Flutter GDE
END:VCARD
```

*Please don't call/email/text me incessantly...* otherwise I'll take down this section of code.

In the end, you simply need to:

- start with the VCard format listed above
- replace all the `xx___xx` fields with your own information
- delete any lines of code that you don't need
- paste the result into the [Project Nayuki QR Code Generator](https://www.nayuki.io/page/qr-code-generator-library)
- save the resultant QR Code as an image on your phone

And just like that, you now have a quick means to create a contact free QR-code business card! 😎 🔥

## MayJuun Connect

We went a bit above and beyond this idea in our own app, including the ability to harness QR Code links to different sections on our website, a portfolio that demos the work we are most proud of over the last ~year, and a means to quickly show off our [FHIR-FLI efforts](https://fhirfli.dev/). The navigation at the bottom took heavy cues from this [blog post](https://medium.flutterdevs.com/custom-animated-bottomnavigation-bar-in-flutter-65293e231e4a), which seemed very well-designed.

{{< figure src="/images/blog/08-mayjuun-connect/mayjuun-connect.gif" width="40%" >}}

If any of you are interested in having your own custom-built QR code + interactive app portfolio as a business card, email us at info@mayjuun.com. We'll be happy to create something to your liking!

--John
