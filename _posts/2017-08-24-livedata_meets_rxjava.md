---
layout: post
title:  LiveData meets RxJava
date:   2017-08-24 12:00 +0200
summary: Android Architecture Components part 3
comments: true
---
In my journey to explore new Architecture Components I've found out that LiveData is not sufficient in complex cases to drive off-the-mainthred work. It is hard to combine results of different LiveData instances. But we have other tools that we use. One of them is RxJava. Can we make them work togheter? Sure we can!

Let's start from the beggining: defining a problem. In my test app I try to implement HackerNews client. In its api in order to download front page items you first need to get item ids list. This defines two actions (interactors) that we wan't to do: reset item ids and load data. I also want to delegate lifecycle management to Architecture Componenets.

My view model looks like this: (full source code can be found on [github](https://github.com/pbochenski/ArchitectureComponents))

{% gist 1ff98db674fd2542987f7b6ee1a52f7b ViewModel.kt %}

I have 3 things in my repo interface that can be seen in view model
1. posts LiveData object to observe downloaded content
2. load function that reset state and download new id list 
3. loadMore function that download items using item ids list

So the problem is how to call two functions but get response on only one LiveData object?

First lets defice switchMap convinience function on LiveData class :

{% gist 1ff98db674fd2542987f7b6ee1a52f7b switchmap.kt %}

I'm using command pattern to solve problem of keeping posts LiveData subscribed in view model and having more than one function to operate on it. 

{% gist 1ff98db674fd2542987f7b6ee1a52f7b repo1.kt %}

As you can see I declared Command sealed class. I can pass parameters to Command objects. Than I have additional commands MutableLiveData, that switchMaps commands into posts. 

Now comes the clash of the worlds of LiveData and RxJava. I want to use RxJava2 to make api requests and convert it into LiveData stream. Fortunately Google provided such transformer in LiveDataReactiveStreams class. To use it you need to add gradle dependency first:

{% gist 1ff98db674fd2542987f7b6ee1a52f7b dependency.gradle %}

Than I convert rx.Single (returned by private functions getFirst and getMore) into LiveData like this:

{% gist 1ff98db674fd2542987f7b6ee1a52f7b switchmap2.kt %}

Final notes:
1. I could probably skip LiveData alltogheter and just unsubscribe RxJava subscriptions in ViewModels ``onCleared()`` method. But that might be more boilerplate that RxJava wrapping (if you consider big project). 
2. If you use LiveData or not, you can use command pattern to have only one observable that emits state.
3. whole source code can be found on [github](https://github.com/pbochenski/ArchitectureComponents)