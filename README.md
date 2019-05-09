# Test-Driven Development with Python

This git repo is the result of me kind of following through the TDDPY book
written by Harry J.W. Percival (ISBN 978-1-449-36482-3). "Kind of" since I
started with a git repo first and not the prerequisites strictly in order.

Also, since the versions will differ, I wonder how much these would affect
the performance. But well.

## Prerequisites

I borrowed the 1st edition, revision 3 (dated 2014-09-19). At the time the
book was written, the following software versions were used:

  - Python 3.4.0
  - pip 3.3
  - Django 1.7
  - Selenium (not stated)
  - Firefox (not stated)
  - git (not stated)

The versions I used on my work-through in 2019 are:

  - Python 3.5.2
  - pip3 19.1
  - Django 2.2
  - Selenium 3.141.0
  - Firefox 66.0.3
  - git 2.7.4

## Selenium webdriver

Selenium requires a webdriver for each browser it is to work with. Mozilla
supplies one for [Firefox][gecko] on Github. I used version 0.24.0.

## Exceptions

The book doesn't recommend virtualenv, but I used one from the get-go. The
directory for the virtualenv wasn't added to the git repo, so you can work
without it.

## Reference Code

Percival points to the [reference source code][hjpw] at the end of Chapter
4, so you can pick it up from there; `$URL/tree/chapter_03` is the code in
Chapter 3, and so on.

[hjpw]:https://github.com/hjpw/book-example
[gecko]:https://github.com/mozilla/geckodriver/releases
