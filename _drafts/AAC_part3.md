---
layout: post
title:  LiveData meets RxJava
date:   2017-07-12 21:00 +0200
summary: Android Architecture Components part 3
comments: true
---
In my journey to explore new Architecture Components I've found out that LiveData is not sufficient in complex cases to drive off-the-mainthred work. It is hard to combine and results of differend LiveData instances. But we have other tools that we use and love. One of them is RxJava. Can we make them work togheter? Sure we can!

Let's start from the beggining, that is defining a problem. In my test app I try to implement HackerNews client. In its api in order to download front page items you first need to get item ids list. This defines to actions (interactors) that we wan't to do: reset item ids and load data. I also wan't to delegate lifecycle management to Architecture Componenets.

so my Repo interface will look like this:
