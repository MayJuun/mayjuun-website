---
title: "A Meta-Post for a Meta-Blog"
date: 2020-11-19T12:55:20Z
type: post
image: images/blog/1-meta/magic-cube-cube-puzzle-play-54101.jpeg
author: John Manning, MD, FAMIA, FACEP
tags: ["meta","howto","informatics","website","hugo"]
---

# Welcome to the Informatics Meta-Blog

Knowledge is power...and best shared with others. This is the place where any informatician, innovator, or entrepreneur can crowd-source contribute and build upon each others' knowledge.

Many of the things I post here will be open-source and moderately technical, but that's only my preference. If there's something else you want to share about healthcare, informatics, innovation, or entrepreneurship, please feel free. Just don't use this as a shameless plug for your work. I won't accept those submissions.

By the end of this post, you'll learn:

1. how to contribute to this meta-blog
2. how to make an open-source website

## Why So Meta

There's a reason why this is called a 'meta-blog'. The term [meta] is Greek for 'after' or 'beyond', but the true beauty of this word is its implied transcendence. Take the following:

1. meta-data == data about data
2. meta-analysis == analysis of multiple analyses
3. meta-cognition == thinking about thought

Put simply, if you are shifting focucs from the topic at hand to the factors that surround it, then that's meta. _You are essentially 'breaking the fourth wall' on the topic._

It's fun to be meta. Even the tabletop / D&D podcast [The Adventure Zone] will regularly host 'meta-episodes' (their title), where they talk about the overarching story in general and provide Q&A. If you want to see a meta-episode in action, just look for [The The Adventure Zone Zone].

## Clinical Informatics: A 'Meta-Specialty'

The Clinical Informatics Subspecialty (CIS) is incredibly broad. The Accreditation Council for Graduate Medical Education (ACGME) [defines it] as "the subspecialty of all medical specialties that transforms healthcare." Personally, I think Clinical Informatics is a meta-specialty...not a subspecialty. We all have so many strengths / passions / interests, clinical backgrounds, and career paths that it can be difficult to characterize succinctly. [KOI Pond] was created for this very purpose.

---

## The Meta-Blog

Now with all of that meta stuff out of the way, let me show you how to contribute to this blog and how to make a website.

## Contributing to This Blog

Anyone can make a static website these days, and if you crowd-source build on an open-source foundation, the path forward can be very rewarding. I\'m using the open-source static site generator called [Hugo], implemented with a [custom open-source theme] ([+ my own mods]).

If you've never worked with GitHub Pull Requests, start by watching this 2 minute video:
{{< youtube 8lGpZkjnkt4 >}}

The entire website exists as two Github repos:

1. the repo where I make all changes: [mayjuun-website]  <--- *fork this repo!!!*
2. an auto-updated repo that makes a [GitHub page]

On my end, repo #2 is what this website actually displays. I make use of two convenience scripts ([update], [deploy]) to automate all my Git commands for this repo. All I have to do is open a terminal in ths mayjuun-website folder and type:

```terminal
./update.sh
./deploy.sh
```

...and I'm done. Website is accurate, with all changes implemented and all my layout/content changes tracked in their own separate repo (#1).

## Creating a Post

If you haven't yet, fork my [mayjuun-website] repo.
{{< figure src="/images/blog/1-meta/fork-repo.png" width="600" >}}

Go to the new fork you just created, and clone it to your desktop.

{{< figure src="/images/blog/1-meta/clone-repo.png" width="600" >}}

In terminal, in that folder, create a [new branch], and make whatever edits you want in your favorite IDE, such as [VS Code].

Create a new Markdown file in the blog directory `/content/blog/##-MY-POST.md`. Usually, I'll just copy the previous post, update the tags/images at the header, and delete all the text. I put all images for that post in the `/static/images/blog/##/` folder to keep things organized. Finally, if you have Hugo installed as shown below, you can run `hugo serve -D` in terminal at the mayjuun-website folder to see a local copy of this site. This way, each time you save a file, you can see all layout changes in real time.

The [Markdown Cheat Sheet] is a handy resource for Markdown formatting. Feel free to look at the other `.md` posts as well for tips on handling hyperlinks, videos, etc. Keeping with the open-source theme, consider using [Pexels], [Unsplash], or [Pixabay] when choosing stock images. Finally, if you need an image with custom sizing instead of the default `!(title)[IMAGE.png]`, use this snippet with `img-right`, `img-left`, or `img-center` based on intended alignment and with your custom `width` for that image:

```hugo
{{</* figure src="/images/blog/YOUR_IMAGE.PNG" title="YOUR TITLE" class="img-right" width="250" */>}}
```

Here's an example of what a Markdown file looks like
{{< figure src="/images/blog/1-meta/vs-code.png" width="600" >}}

---

## Submitting a Post

When you're done editing, open a terminal in the repo's main folder and type:

```terminal
hugo-touch.py content/blog/##-MY-POST.md
```

This runs [a simple python script] to update the `date:` timestamp at the top of the file. This timestamp represents the time a post has been finalized and is used to sort blog posts.

Finally, add and commit your changes. You can use the command line, such as was shown in the above YouTube video:

```terminal
git add .
git commit -m "CATCHY COMMIT TITLE 😎"
git push origin MY-BRANCH-NAME
```

...or you can use [VS Code directly], which is my preference. You'll want to make a pull request on my repo so that I can implement your changes, which is covered in both the [YouTube video] and on [this site].

---

### Creating a Website

If you want to make your own website, follow these steps:

1. Install Hugo. I'd suggest using [their steps] based on your operating system. For Mac, you need [Homebrew] first if you don't already have it. To install Homebrew, open a terminal and type:

```terminal
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

2. Then use Homebrew to install Hugo:

```terminal
brew install hugo
```

3. And verify you have hugo installed:

```terminal
hugo version
```

4. You can use Finder/Explorer or you can use [basic terminal commands] to decide where you want to put your website folder on your machine. For example, if you want a website called `quickstart` in a new folder called `~/dev` on Mac/Linux, type:

```terminal
mkdir ~/dev
```

5. Then navigate to that folder:

```terminal
cd ~/dev
```

6. And use Hugo create a brand new site:

```terminal
hugo new site quickstart
```

7. Navigate to the new folder you created:

```terminal
cd quickstart
```

8. And run a local server with the command line:

```terminal
hugo serve -D
```

This will run your site in fast render mode (which is the `-D` flag). You can access this site when the serve is running by going to `https://localhost:1313` in your preferred web browser. If you ran this same command `hugo serve -D` in another folder, such as where you forked/cloned my [mayjuun-website] repo, then you can run a local version of that website instead. As you make changes to the site locally, the browser will automatically update each time a file is saved.

Finally, you can close your server by pressing `ctrl + c` in the terminal. That's it! You now have a static site!

Let me know if you want me to cover other content about static sites. Next post, I'll plan to cover some [Flutter]-related content.

--John

[meta]: https://en.wikipedia.org/wiki/Meta
[The Adventure Zone]: https://maximumfun.org/podcasts/adventure-zone/
[The The Adventure Zone Zone]: https://theadventurezone.fandom.com/wiki/The_%22The_Adventure_Zone%22_Zone
[meta-theatrical]: https://en.wikipedia.org/wiki/Fourth_wall
[defines CIS]: https://www.acgme.org/Portals/0/PFAssets/ProgramRequirements/381_ClinicalInformatics_2020.pdf?ver=2020-06-29-163724-707
[KOI Pond]: https://www.thieme-connect.com/products/ejournals/html/10.1055/s-0039-1701021
[Hugo]: https://gohugo.io/about/
[custom open-source theme]: https://github.com/themefisher/timer-hugo
[+ my own mods]: https://github.com/MayJuun/mayjuun-website/commits/master
[mayjuun-website]: https://github.com/MayJuun/mayjuun-website
[GitHub page]: https://github.com/MayJuun/MayJuun.github.io
[update]: https://github.com/MayJuun/mayjuun-website/blob/master/update.sh
[deploy]: https://github.com/MayJuun/mayjuun-website/blob/master/deploy.sh
[VS Code]: https://code.visualstudio.com/
[new branch]: https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-and-deleting-branches-within-your-repository
[Markdown Cheat Sheet]: https://www.markdownguide.org/cheat-sheet/
[Pexels]: https://www.pexels.com/
[Unsplash]: https://unsplash.com/
[Pixabay]: https://pixabay.com/
[their steps]: https://gohugo.io/getting-started/quick-start/
[Homebrew]: https://brew.sh/
[basic terminal commands]: https://swcarpentry.github.io/2014-04-14-wise/novice/shell/02-create-delete.html
[Github pages install steps]: https://pages.github.com/
[a simple python script]: https://rpeshkov.net/blog/update-timestamp-hugo-post/
[VS Code directly]: https://code.visualstudio.com/docs/editor/versioncontrol#_commit
[YouTube video]: https://youtu.be/8lGpZkjnkt4
[this site]: https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request
[Flutter]: https://flutter.dev/