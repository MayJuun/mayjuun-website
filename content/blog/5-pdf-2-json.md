---
title: "pdf2json: A Step-by-Step Guide"
date: 2021-03-26T02:44:38Z
type: post
image: images/blog/5-pdf-2-json/ferenc-almasi-HfFoo4d061A-unsplash.jpeg
author: John Manning, MD, FAMIA, FACEP
tags: ["terminal","json","pdf","tutorial"]
---

## Intro -

Well, I can't say this issue will come up too often for others...but should you ever need it, here are the exact steps you can take to convert all the text from a PDF file into a JSON file with key-value pairs of `"page#" : "all page text without extra white space"`. Note that `page#` is an integer that starts at 1, not 0.

I needed this in a project where the Flutter packages that performed PDF search functions were not performant, had memory leaks, or seemed to work inconsistently across platforms. That limitation may have changed by the time you read this post, so do a bit of search before going too much further.

Since the files read were quite large to begin with, I decided it would be best for everyone (and for my own peace of mind) to just go ahead an convert all text into something easily consumed by Dart...hence a JSON file. This method isn't specific to Dart/Flutter. For our purposes, it took content from a 20 mb file and compressed it into 200 kb. Search will definitely be more streamlined!

Here are the steps I followed. Later on, I may update this blog post and/or optimize my terminal commands, thus limiting the requirements of manual 'data scrubbing' even further. The data scrubbing steps aren't too cumbersome right now, so for the time being...I'm just leaving them in.

## Converting PDF to JSON (first attempt)

### Requirements

First, you need [pdfgrep](https://pdfgrep.org/doc.html) and [jq](https://stedolan.github.io/jq/) available in your terminal, assuming you haven't previously installed them. On a Mac, using [homebrew](https://brew.sh), simply open a terminal and type:

```terminal
brew install pdfgrep jq
```

-------

## Steps to Follow

I'm going to assume that your PDF file is named in a specific manner where you are sure - without question - that no text exists in your PDF with the file name's title and a trailing `:`, aka `FILENAME.pdf:`. If you can't say that for sure, please change your filename before you run the following command:

```terminal
pdfgrep -nH '.*' FILENAME.pdf | sed 'H;1h;$!d;x;y/\n/ /' | sed "s/\"/'/g" | tr -s ' ' > input.txt
```

Then:

- Open the file
- Turn all of the `FILENAME.pdf:` elements into carriage returns (on Mac, in VS Code, press cmd + d repeatedly to select all duplicates, then enter)
- To the right of the index/page number, add ':::'   (on Mac, after you pressed enter in the previous step, simply press cmd + right, :, :)

Make sure that you remove the first (now unnecessary) carriage return from line 1 and that you wrap the entire document with a single pair of brackets (first character in the file is `{`, last character in the file is `}` ). Now close the file.

Then, in terminal, run:

```terminal
jq -R -n -c '[inputs|split(":::")|{(.[0]):.[1]}] | add' input.txt > output.json
```

Finally, re-open the file, select and delete all ' \f ' and ' \f' fields (if desired)...and sit back and enjoy the fruits of your effort! Once learned, the total time spent to get from PDF to performant JSON file can be measured in seconds.

-------

## So What Just Happened?

I can't say I'm an expert on piping commands through terminal to build optimized regular expressions...nor am I a pro at `sed`, `grep`, and the like...but I am able to do a bit of targeted 'Google searching'.

So I don't forget what each step entails, I'll try to explain each section that was utilized in these two terminal commands below:

- [pdfgrep](https://pdfgrep.org/doc.html) will search for items within a PDF using extended regular expressions. I'm specifically using the `'.*'` expression to get the entire raw file. When testing, add the `--max-count 2` flag
- pdfgrep data are piped through `sed 'H;1h;$!d;x;y/\n/ /'` to remove all carriage returns, through `sed "s/\"/'/g"` to convert all double quotes to single quotes (so it won't break your JSON), and through `tr -s ' '` to remove all trailing whitespace. The result is saved to `input.txt` with the formatting of: 

```terminal
FILENAME.pdf:1: Lorem ipsum dolor ... FILENAME.pdf:2: Lorem ipsum dolor ... FILENAME.pdf:3: Lorem ipsum dolor ...
```

- Note that I am intentionally using 'FILENAME.pdf:' as a unique search term for this document

- I manually turn all `FILENAME.pdf:` instances into carriage returns, and then move over (using cmd + right, since that skips by word and works regardless of how many digits are in the page number) and add two extra `:` fields, thus giving:

```terminal

1::: Lorem ipsum dolor ...
2::: Lorem ipsum dolor ...
3::: Lorem ipsum dolor ...
```

- After deleting the first (empty) line and adding brackets to the start/end...

```terminal
{ 1::: Lorem ipsum dolor ...
2::: Lorem ipsum dolor ...
3::: Lorem ipsum dolor ... }
```

- I save my results and run `jq -R -n -c '[inputs|split(":::")|{(.[0]):.[1]}] | add' input.txt`, which uses `:::` as a delimeter between key-value pairs and carriage return as a delimeter for each entry. This result is saved as `output.json`, though it (unfortunately) also contains ` \f ` in all fields save for the last (which has ' \f' without the trailing space). After deleting those escape characters and extra whitespaces, I now have a fully implemented JSON from a PDF!

```terminal
{ "1": "Lorem ipsum dolor ...",
"2": "Lorem ipsum dolor ...",
"3:" "Lorem ipsum dolor ..." }
```

## Closing Thoughts

This was a quick answer to an interesting challenge. Hopefully others will find it useful, if they ever need to convert the text within a PDF to a JSON string whose index is the page number. In retrospect, it's clear that some of my steps can be better automated/optimized...but this does work and it didn't take much time out of my day.

Hope that helps someone!

--John
