---
layout: post
title: MVI using Kotlin coroutines
date:   2018-01-05 10:00 +0200
summary: Kotlin coroutines and channels are awesome
comments: true
---
I'm a fan of MVI architecture on Android. If you are not familiar with it please check out this brilliant set of posts by [Hannes Dorfmann](http://hannesdorfmann.com/android/mosby3-mvi-1)
Today I will try to implement it using Kotlin coroutines and channels.

Why bother learning coroutines you might ask? We do have RxJava to abstract asynchronous operations and model apps using streams. My main motivation is that multi platform projects are coming and there will be no RxJava on iOS. Second is that is always nice to learn something new. And third is that with channels and Kotlin/Native Kotlin is stepping into GoLang territory. I think that maybe there will be some opportunities for interesting projects.

Ok, lets go back to MVI. What I want to do is single stream of events per activity/fragment that goes into some kind of controller. That controller has output stream that activity fragment can subscribe to and get state changes. Controller transforms input stream of events into output stream of view states. It would be nice if controller would survive state changes of activity. 

First let's add coroutines gradle dependencies:
{% gist 1e5f189172bed8207880ba4a869aca60 gradle.gradle %}

Now we have all tools we can start build some base activity. In real world this should be some open base class so different activities can inherit from it. But lets keep it simple for now
{% gist 1e5f189172bed8207880ba4a869aca60 baseActivity.kt %}

I'm using lastCustomNonConfigurationInstance to preserve controller during configuration change like rotation. I can imagine if someone puts it into Architecture Components View holder for the same purpose. 

As you can see I create output channel that controller can write to. I pass it to controller in setup function. 
Using launch(UI) coroutine launcher makes sure that all UI changes will happen on main thread. in this launcher I can consume all events written to outputChannel and change UI accordingly. MyActivityState is sealed class that defines all states of the activity. 

{% gist 1e5f189172bed8207880ba4a869aca60 MyActivityState.kt %}

Lets say we want to finish any action in controller when user presses back button. Let's add it to Activity:
{% gist 1e5f189172bed8207880ba4a869aca60 activityBackPressed.kt %}

You can also notice that we started some code execution in onCreate using controller.send(MyActivityInputs.Start) so our inputs class will look like this:
{% gist 1e5f189172bed8207880ba4a869aca60 MyActivityInputs.kt %}

That was easy! now show me the controller!
{% gist 1e5f189172bed8207880ba4a869aca60 MyActivityController.kt %}

first I create input channel as ConflatedBroadcastChannel. This kind of channels caches last item in it and rebroadcasts it on new subscription. This is nice, because 
