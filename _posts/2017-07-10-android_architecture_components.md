---
layout: post
title:  Android Architecture Components
date:   2017-07-10 10:00 +0200
summary: at last!
comments: true
---
Last I/O Google announced Android architecture components. I couldn't resist to try it out. I build app in kotlin with view models and live data and kotlin coroutinesRecyclerView with 2 view types, infinate scroll and pull-to-refresh. 

The source code can be found [here](https://github.com/pbochenski/ArchitectureComponents)

Here are my thoughts on how it works:
1. **View models**   
I love view models. They survive configuration changes. Multiple fragments can use same model and share state. Super easy to use and test. 

2. **Live data**  
It works ok, but it works only on main thread. so you still need something to do background work. It lacks of operators (filter is one that I use a lot. Having it would be nice. (maybe they will come in future?)) and Single type (for rest api calls) But I don't know if this (having Single) is intention of life data, so maybe my thinking about it needs to adjust. <s> And unit testing it is not working as for now, because unit test does not work on "mainThread". (see and run unit test in example) </s> (use [InstantTestRule](https://developer.android.com/reference/android/arch/core/executor/testing/InstantTaskExecutorRule.html) for unit testing)

3. **kotlin coroutines**   
Someone could probably write a book about it. with LiveData on the side coroutines could probably replace RxJava in my apps, since it is a way to do stuff in background and also combine/manipulate async operations. What I liked about RxJava was that it provided contract and standard way to handle errors, which might by trickier with coroutines. But I liked it and I will observe how it is growing. I might stick to RxJava for now, since I know it better.
 
4. **Room** (not used in my example)  
I toyed a little bit with it and I can say that Google won SQL library battle for me. It is easy, sql based and reactive. also sql queries are parsed like in sqlDelight so it is type safe. Only con is that it is not ciphered. but maybe it will be some day. 

I know that my knowledge is lacking in topic so please comment and review the code :)

To sum up: I can't wait to use it in production code, after leaving alpha stage. I will for sure use it as my main architecture. It is reactive, easy and fixes problem with configuration changes. Unidirectional data flow can be easily achieved with it. I'm super exited about it.

--  
edit: [Reddit post](http://reddit.com/r/androiddev/comments/6mkdb3/ive_tried_architecture_components_and_this_is/) of this article induced nice discussion about ViewModel role in app. I highly recommend this.