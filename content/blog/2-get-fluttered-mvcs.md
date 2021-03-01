---
title: "Get Fluttered: MVC+S Architecture, Example"
date: 2021-01-14T19:52:02Z
type: post
image: images/blog/2-get-mvcs/get-mvcs-logo.png
author: John Manning, MD, FAMIA, FACEP
tags: ["flutter","mvc+s","get_fluttered","prapare","tutorial"]
---

## Intro -

To all who watched my original GetFluttered: MVC+S Architecture video, I want to thank you immensely for your patience.

Before making new GetFluttered videos, we wanted to implement:

1. A means to provide written, supplemental info ... [Meta-Blog](https://mayjuun.com/blog/);
2. A complex, production-level MVC+S example ... [PRAPARE app](https://github.com/firejuun/prapare); &
3. A means for others to join / collaborate ... [FlutterJuun Slack invite](https://join.slack.com/t/flutterjuun/shared_invite/zt-mzbgwc85-sgm3ClBYj1IrzlSf9jfWzA).

With these elements now firmly established, it should be easier to follow along with GetFluttered content by comparing [simple](https://github.com/FireJuun/get_fluttered) + [complex](https://github.com/FireJuun/prapare) code examples that achieve the same objective.

Given our healthcare focus, and specifically our interest in connecting [FHIR](https://www.hl7.org/fhir/overview.html) to Flutter, our roadmap for GetFluttered videos will also include some [FHIR-FLI](https://www.fhirfli.dev/) content...but by no means is the GetFluttered series limited to health apps. Many of the topics covered can be applied to any Flutter app.

Here's the primer on FHIR-FLI:

{{< youtube nE3faNn9aNU >}}

Finally, I plan to periodically update this architecture page so the Slack invite remains active (since Slack links now expire after 30 days)...but if I miss it, let me know in a comment on one of my YouTube videos. I’ll respond to your comment when the invite link is reactivated.

### MVC+S: Architecture

{{< youtube 2ttaAMkce6I >}}

You should probably start by reading Ryan Edge’s post on [Flutter State 5 Ways](https://poetryincode.dev/flutter-state-5-ways). Then read GSkinner’s article on [MVC+S Architecture.](https://blog.gskinner.com/archives/2020/09/flutter-state-management-with-mvcs.html) Finally, check whatever latest discussions may exist in the Flutter community. As of Jan 2021, [Simon Lightfoot’s video](https://youtu.be/sYG7HAGu_Eg?t=7440) may be a good start...

When deciding state / architecture, consider:

* Do your classes follow the single responsibility principle?
* Are they testable?
* Are they modular?
* How difficult is this setup?
* Are others able to understand and build from it?

Ultimately, we decided upon the [Get](https://pub.dev/packages/get) package to manage state and the GSkinner suggestion on MVC+S for our architecture. Because Get uses its controllers -- not models -- to manage state, we elected to make slight modifications from the original GSkinner approach.

{{< figure src="/images/blog/2-get-mvcs/get-mvcs-diagram.png" title="Get MVC+S Diagram" class="img-center" width="75%" >}}

### Working with Streams

In the Architecture video, I particularly made a point of swapping between `int counter = 0;` and `RxInt rxCounter = 0.obs;` because I wanted you to be able to use this architecture with and without [streams](https://youtu.be/nQBpOIHE4eE). GetX makes it extremely easy to work with streams and with minimal boilerplate, so you should feel comfortable swapping between the two.

Keep in mind that the `GetX` and `OBx` methods require a stream to function properly.  If it isn’t a stream, use `GetBuilder` instead. Also, make sure to call `update();` in your controller if you need to trigger a UI refresh.

I was very intentional in my [GetFluttered commit history](https://github.com/FireJuun/get_fluttered/commits/1_get_mvcs_architecture) to have each commit focus on a single objective in my video. Swapping between typical variables &lt;--> streams is one example where [the commit log](https://github.com/FireJuun/get_fluttered/commit/78b69ff7fd2cd151843bfc19e57bae41fceece6e) can help. I plan to continue this format as best I can (and within reason).

### Variable Names ± Streams

Initially, I was quite strict about updating all variable names to include ‘rx’ at the front if it referenced a stream...but as we built PRAPARE it became apparent that this level of control seemed more a hindrance than a benefit. Including ‘rx’ was useful in many cases, but should not be a set requirement. For complex data models, I would suggest you focus on variables and method names that are easy to read / understand, following patterns when it makes sense to do so.

## MVC+S: Example

{{< youtube FvB9PbGfmRk >}}

In my opinion, learning about folder structure is best accomplished via example. Our video outlining the PRAPARE app as a complex example of the MVC+S architecture pattern should help. Keeping everything in one place, this is the general guideline we followed:

  | **Folder**   | **Subfolder**                          | **Description**                                                                                        |
  | ------------ | -------------------------------------- | ------------------------------------------------------------------------------------------------------ |
  | /_internal   |                                        | custom modifications, constants / enums, utility classes                                               |
  |              | /components                            | custom components / variations on Flutter widgets                                                      |
  |              | /constants                             | local constants created for the app                                                                    |
  |              | /enums                                 | predefined, named constants                                                                            |
  |              | /utils                                 | local functions that do things like formatting                                                         |
  | /api         |                                        | optional API key location                                                                              |
  |              | &lt;custom>.dart                       | private API keys                                                                                       |
  |              | api_public.dart                        | public API keys (no gitignore)                                                                         |
  |              | api.dart                               | generic export file                                                                                    |
  | /controllers |                                        | manages state of the model and resultant data                                                          |
  |              | /commands                              | performs a specific global task (login, logout, change password)                                       |
  |              | ../&lt;custom>_command.dart            | custom command class                                                                                   |
  |              | ../abstract_command.dart               | abstract class for commonly used controllers, placeholder execute() method for commands                |
  |              | &lt;custom>_controller.dart            | custom controller, typically used for state management                                                 |
  | /models      |                                        | classes / objects created specifically for this app                                                    |
  |              | &lt;custom>_data.dart                  | custom data class                                                                                      |
  |              | &lt;custom>_model.dart                 | data model that typically modifies or shapes a data class                                              |
  | /routes      |                                        | maps route to screen widgets                                                                           |
  |              | app_pages.dart                         | the directory of each page within an app                                                               |
  |              | app_routes.dart                        | string route names used in the app                                                                     |
  | /services    |                                        | interaction with the outside world (REST, FHIR, http, file storage)                                    |
  | /ui          |                                        | essentially all things a user sees in the app                                                          |
  |              | /styled_components                     | shared widgets that use a common design system / theme so that the app seems consistent across screens |
  |              | ../styled_&lt;widget_name>.dart        |                                                                                                        |
  |              | /views                                 | top level widgets that are loaded via a route                                                          |
  |              | ../&lt;screen_name>/                   |                                                                                                        |
  |              | ../../&lt;screen_name>.dart            | the screen widget, may optionally include 'page', 'card', or 'panel' at the end based on view type     |
  |              | ../../&lt;screen_name>_binding.dart    | controllers/services that are loaded (or lazy-loaded) in a view                                        |
  |              | ../../&lt;screen_name>_controller.dart | the viewcontroller that only affects this screen widget                                                |
  |              | ../../&lt;screen_name>_test.dart       | any relevant tests for the screen widget or its viewcontroller                                         |
  |              | icons.dart                             | icon asset locations                                                                                   |
  |              | localization.dart                      | strings with multiple translations                                                                     |
  |              | strings.dart                           | strings used throughout an app                                                                         |
  |              | themes.dart                            | custom themes and font sizes                                                                           |
  | main.dart    |                                        | the first file a Dart app runs                                                                         |

## Conclusion

I hope these written supplements will be useful as you design and build your own Flutter apps.

If there are any questions, or if you have any specific requests for GetFluttered topics to cover next, feel free to join us on the FlutterJuun Slack. A lot of GetFluttered content will build directly off of the work we already created in PRAPARE, and we have a lot of features to cover (themes, locales, databinding, serialization, etc.) in the short-term. That said, the path forward is pretty flexible and welcome to suggestions.

Keep learning, keep creating, and stay safe!

--John
