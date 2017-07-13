---
layout: post
title:  Unit testing LiveData
date:   2017-07-12 21:00 +0200
summary: Android Architecture Components part 2
comments: true
---
Last time I tried to use Android Architecture components. I couldn't make LiveData to run in unit tests. But it turns out it is possible.

When trying to use LiveData in unit test I encountered this crash:
{% gist e9aef99158003f70f273cf0e2b9d43b0 crash.md %}

The reason it happens is that thread in unit test is not in Android environment. We can fix it. First add architecture components core-testing artefact like this:

{% gist e9aef99158003f70f273cf0e2b9d43b0 gradle.gradle %}

Then add testing rule to test, that installs proper TaskExecutor to AppToolkitTaskExecutor, which drives LiveData execution. This will also make everything run on single a thread. In Kotlin it will look like this:

{% gist e9aef99158003f70f273cf0e2b9d43b0 test.kt %}

And that's it. Now we can test. 
For example:

{% gist e9aef99158003f70f273cf0e2b9d43b0 test2.kt %}

Here I create mock Observer<T> class and I add it as my models LiveData observer. I can use observeForever method, because model we be destroyed at the end of test.  Now I have something I can verify on. Then I change LiveData (MutableLiveData) itself. In the end, I verify on observer object if transformation in my model fits my expectation. 

I would say it was quite easy, and the test looks nice and concise. 

The source code can be found [here](https://github.com/pbochenski/ArchitectureComponents)