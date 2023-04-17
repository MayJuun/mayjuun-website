---
title: "Fish and Flutter: 5 Step Install"
date: 2021-05-14T14:04:09Z
type: post
image: images/blog/06-fish-and-flutter/pexels-pixabay-207580.jpeg
author: John Manning, MD, FAMIA, FACEP
tags: ["fish","flutter","homebrew","tutorial"]
---

## Intro -

This is a supplemental post to the YouTube video tutorial that shows how to install iTerm, Fish, and Flutter on a Mac.

{{< youtube unMS6Tn_oEI >}}

The video boils everything down to 5 steps, which I will define here.

## Step 1: Homebrew + Fish + iTerm2

To get started, you need to follow the [Automatic Installation](https://github.com/FireJuun/iterm-fish-fisher-osx#automatic-installation) steps on my iterm-fish-fisher repo, or you can just copy/paste the same steps that are listed below.

In a terminal shell (command + space -> 'Terminal'), type

```shell
bash
```

To switch from zsh to bash as the shell prompt. Then type

```shell
bash <(curl -s https://raw.githubusercontent.com/firejuun/iterm-fish-fisher-osx/master/install.sh)
```

To load the automatic iTerm-Fish-Fisher install script for OSX.

This installs

- Command line tools (if XCode isn't already installed)
- [Homebrew](https://brew.sh)
- [iTerm2](https://iterm2.com)
- [Meslo LG M DZ Regular Nerd Font Complete Mono](https://github.com/ryanoasis/nerd-fonts/blob/25eec835188d2316ef3fe59820950d9f90c5bcf4/patched-fonts/Meslo/M-DZ/Regular/complete/Meslo%20LG%20M%20DZ%20Regular%20Nerd%20Font%20Complete%20Mono.ttf?raw=true), which is a type of powerline font or '[nerd font](https://github.com/ryanoasis/nerd-fonts)'
- [Fish shell](https://fishshell.com)
- [Fisher](https://github.com/jorgebucaran/fisher)

In my first blog post on the [Meta-Blog](https://mayjuun.com/blog/01-meta-post/), I showed how Homebrew can be used as a package manager for Hugo when making websites. It has far more functionality, which we'll see here.

Once all content has been installed via terminal, I'd also suggest running

```shell
curl https://raw.githubusercontent.com/firejuun/iterm-fish-fisher-osx/master/iTerm-Hotkey-Profiles.json --output ~/Downloads/iTerm-Hotkey-Profiles.json
```

To download the hotkeys / transparent iTerm profile to your `~/Downloads` directory.

Then:

- Open iTerm2 -> File -> Preferences -> Profiles -> Other Actions -> Import JSON Profiles
- Import the iTerm-Hotkey-Profiles.json file from your Downloads folder
- Select the Hotkeys - Default -> Other Actions -> Set as Default. From here on, pressing option + space will open the Hotkeys - Default terminal window, and control + control will open the Hotkeys - Top terminal window.

## Step 2: iOS / Android:  IDEs + Emulators

Set up an iOS emulator:

- Download XCode from the App store
- Open XCode, then go to XCode -> Open Developer Tool -> Simulator
- After Simulator has opened for the first time, you no longer need to use XCode to open this emulator. Simply type command + space -> 'Simulator' or open it from the VS Code Command Palette, as shown in the video.

Set up an Android emulator:

- Run this command to install Android Studio. I would suggest installing all other programs as well (Flutter, VS Code, Google Chrome) if you don't have them yet. If the program is already installed, just delete that program's title from this command:

```shell
brew install --cask android-studio flutter visual-studio-code google-chrome
```

- Open Android Studio, accepting the default values and installing the default SDKs
- From the Android Studio Welcome Screen, go to Configure -> SDK Manager -> SDK Tools. Then click the checkbox to install 'Android SDK Command-line Tools (latest)'
- Also on the Welcome Screen, go to Configure -> AVD Manager and create a new Virtual Device (if not already present). Click the play button to load that device for the first time

If you're ever unsure about what command to run/install next,

```shell
flutter doctor
```

is incredibly helpful.

## Step 3: VS Code + Extensions

The `brew install --cask` command above should install VS Code for you, assuming you don't have it already. Here are the Extensions I suggest, or would consider installing. The only two required extensions are `Dart` and `Flutter`

Flutter Related:

- Awesome Flutter Snippets
- Better Comments
- Bracket pair colorizer 2
- Colonize
- Dart
- Flutter
- Flutter Widget Snippets
- Freezed
- GetX Snippets
- Pubspec Assist

Overall:

- Error Lens
- Git History
- GitLens -- Git supercharged
- Live Share
- Material Icon Theme

Optional:

- Beautify
- Docker
- Even better TOML
- HTML CSS Support
- Hugo Helper
- Hugo Language and Syntax Supporter
- Markdown All in One
- Markdownlint
- Serenade
- Subtitles Editor

## Step 4: Flutter Create

In a shell prompt (such as Fish shell, now by typing option + space), type

```shell
flutter create --org com.example hello_world
```

The `--org` flag is incredibly helpful so that you don't have to change your app's package name later on. Just set it at the beginning, if you already know what to put.

## Step 5: Multi-Device Debugging

Finally, in VS Code, create a new file in the `.vscode/launch.json` folder. I typically have this file (and all of `.vscode` for that matter) listed in `.gitignore`, since that will vary from workstation to workstation.

Follow the steps from [this website](https://github.com/flutter/flutter/wiki/Multi-device-debugging-in-VS-Code) to replace the launch.json file with their default.

```json
{
 "version": "0.2.0",
 "configurations": [
  {
   "name": "Current Device",
   "request": "launch",
   "type": "dart"
  },
  {
   "name": "Android",
   "request": "launch",
   "type": "dart",
   "deviceId": "android"
  },
  {
   "name": "iPhone",
   "request": "launch",
   "type": "dart",
   "deviceId": "iphone"
  },
 ],
 "compounds": [
  {
   "name": "All Devices",
   "configurations": ["Android", "iPhone"],
  }
 ]
}
```

Then run

```shell
flutter devices
```

to find the unique deviceIDs for your workstation, and copy/paste these values into the relevant `deviceId` value of the of your Android and iPhone.

Your final version of this file should look like this:

```json
{
 "version": "0.2.0",
 "configurations": [
  {
   "name": "Current Device",
   "request": "launch",
   "type": "dart"
  },
  {
   "name": "Android",
   "request": "launch",
   "type": "dart",
   "deviceId": "YOUR_ANDROID_ID"
  },
  {
   "name": "iPhone",
   "request": "launch",
   "type": "dart",
   "deviceId": "YOUR_IPHONE_ID"
  },
 ],
 "compounds": [
  {
   "name": "All Devices",
   "configurations": ["Android", "iPhone"],
  }
 ]
}
```

### Launching Multiple Files

On the `Run and Debug` To the right of the play button, you should be able to change `Current Device` to `All Devices`. Note that this is a very powerful feature, and not just limited to phone/iOS emulators.

This setup, for example, is a means to include Flutter web into your `launch.json` file:

```json
{
    // spec: https://github.com/flutter/flutter/wiki/Multi-device-debugging-in-VS-Code
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Current Device",
            "request": "launch",
            "type": "dart"
        },
        {
            "name": "Android",
            "request": "launch",
            "type": "dart",
            "deviceId": "YOUR_ANDROID_ID"
        },
        {
            "name": "iOS",
            "request": "launch",
            "type": "dart",
            "deviceId": "YOUR_IPHONE_ID"
        },
        {
            "name": "Web",
            "request": "launch",
            "type": "dart",
            "deviceId": "chrome"
        },
    ],
    "compounds": [
        {
            "name": "Android/iOS",
            "configurations": [
                "Android",
                "iOS",
            ],
        },
        {
            "name": "Android/iOS/Web",
            "configurations": [
                "Android",
                "iOS",
                "Web",
            ],
        }
    ]
}
```

## Conclusions

Hopefully by now, you should have a bit of a sense on how to get things up and running on a new Mac. If there's interest, let me know and I can make a similar video series for PC...though the steps will admittedly be different (no Fish/Homebrew, unfortunately).

Happy coding! Stay safe out there!

--John
