# markdown_letter

**markdown_letter Allows you write letters in simple Markdown.**

Instead of using a full blown word processor, you can write your letters with [Markdown](https://en.wikipedia.org/wiki/Markdown).

A letter might look like this:

```
---
fromaddress:
- Musterallee 13
- 12345 Musterhausen
fromphone: 06321 123456
fromfax: 06321 123457
fromemail: brejoc@gmail.com
fromurl: http://brejoc.com
place: Musterhausen
date: \today
# yourref: DF346
address:
- ACME Inc.
- Frau Musterfrau
- Musterallee 42
- 12345 Musterhausen
subject: Ihr Schreiben vom 01.01.01
opening: Sehr geehrte Frau Musterfrau,
closing: Mit freundlichen Grüßen,
email: brejoc@gmail.com
fromname: Jochen Breuer
...
Lörem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.


Lörem *ipsum* dolor sit amet, _consete_ sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
```

With a little help of pandoc and texlive this Markdown file is converted to a well formatted (German DIN) letter.

## Installation

markdown_letter is a simple flask application. You can find the python dependencies in the [requirements.txt](https://github.com/brejoc/markdown_letter/blob/master/src/requirements.txt). Additional dependencies are `pandoc` and `texlive-full`. I'm not sure which verison of `texlive-full` is needed, but it won't work on Ubuntu 14.04. 16.04 is fine. FreeBSD 10.3 is also working.

## Hacking your own letter template

Customizations should be fairly simple. At least if you are familiar with Tex… which I'm not. Just take a look at [brief.tex](https://github.com/brejoc/markdown_letter/blob/master/src/brief.tex).
