---
layout: post
title: Learning Dagger
date:   2017-10-24 13:00 +0200
summary: part 1
comments: true
---
I know IoC rule is one of the most important pattern in Object Oriented programming. I use it in my everyday work. But I never bothered to learn Dagger. For Kotlin project I used Injekt library. Learning Dagger feels like learning new language and my projects where small enough that I never needed big tool like this. But now I feel it is time for me to learn it. I will document my learning process here.

Plan:
1. basic injection
3. android specific injection
4. unit testing
5. espresso testing (MockWebServer)

I will use dagger 2 and my login-dojo project to learn this stuff. In this project I tried to build simple Log-in activity with headless fragment and unidirectional data flow. It has simple dependency graph:

Activity -> MainActivityAH (Headless Fragment that acts like ViewModel) -> Repo -> Retrofit api object

Unfortunately Dagger tutorial on home page is a little bit like drawing owl. 

![drawing owl image](http://i0.kym-cdn.com/photos/images/original/000/572/078/d6d.jpg)

I will try to do it in baby steps. To use dagger we need Component (which is an entry point to our dependency graph). Component is build from Modules which provides Objects. Lets build empty Component (in Kotlin):

{% gist 55ca6a881530f2e6131cd38aa19caa80 component.kt %}

The nice thing about Dagger2 that it is 100% compile time. So we can see what has been generated. Let's do it: 

{% gist 55ca6a881530f2e6131cd38aa19caa80 componentGenerated.kt %}

Here we can see that DaggerAppComponent class was created and that it has builder to create object of this class. we can use it in our Application class to build the graph:

{% gist 55ca6a881530f2e6131cd38aa19caa80 componentBuild.kt %}

This does nothing yet, but it creates entry point to our DI graph. Lets create some module and add it to graph.

{% gist 55ca6a881530f2e6131cd38aa19caa80 module.kt %}

This defines RestDModule which can create Repo object. it is also annotated with @Singleton, so only one instance of this object will be created. 
Now we need to add module to component:

{% gist 55ca6a881530f2e6131cd38aa19caa80 componentWithModule.kt %}

OK, so our dependency graph is done. now we need to inject those objects into classes that uses them. I have such class named MainActivityAH, which needs Repo class. MainActivityAH inherits from Fragment, so we need to do field injection. Usually we prefer constructor injection, but it is not possible for Fragments and Activities. (This is a little code smell, so maybe lets handle it later).

To inject field in fragment we need to annotate the field with @Inject annotation:

{% gist 55ca6a881530f2e6131cd38aa19caa80 fragmentInjection1.kt %}

The last thing we need to do is actually inject objects. in my onCreate() function in MainActivityAH i put:

{% gist 55ca6a881530f2e6131cd38aa19caa80 fragmentInjection2.kt %}

Here I take component (which is builded AppComponent and saved in App object) and call inject method on it. but what is this method? We need to create it first:

{% gist 55ca6a881530f2e6131cd38aa19caa80 componentInject1.kt %}

And that's it. Injection works! Now if I want to Inject into another fragment I need to add another inject method:

{% gist 55ca6a881530f2e6131cd38aa19caa80 componentInject2.kt %}

This does not look good, if you have a dozen of fragments. lets try to fix it in next part! Stay tuned!

as always code aviliable at [github](https://github.com/pbochenski/login-dojo/tree/dagger)