# Test-Driven Development with Python

This git repo is the result of me kind of following through the TDDPY book
written by Harry J.W. Percival (ISBN 978-1-449-36482-3). "Kind of" since I
started with a git repo first and not the prerequisites strictly in order.

Also, since the versions will differ, I wonder how much these would affect
the performance. But well.

## Prerequisites

I borrowed the 2nd edition, release 1 (dated 2017-08-02). At the time the
book was written, the following software versions were used:

  - Python 3.6.0
  - pip (not stated)
  - Django 1.11.3
  - Selenium 3.4.3
  - Firefox (not stated)
  - geckodriver 0.17.0
  - git (not stated)

The versions I used on resuming my work-through in 2023 are:

  - Python 3.10.6
  - pip 23.1.2
  - Django 1.11.3 (to work through the examples)
  - Selenium 3.4.3
  - Firefox 114.0.1
  - geckodriver 0.33.0
  - git 2.34.1

## Selenium webdriver

Selenium requires a webdriver for each browser it is to work with. Mozilla
supplies one for [Firefox][gecko] on Github. I used version 0.33.0.

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
