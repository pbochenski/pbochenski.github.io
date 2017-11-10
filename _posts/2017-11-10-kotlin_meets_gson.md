---
layout: post
title: Kotlin meets gson
date:   2017-11-10 10:00 +0200
summary: Kotlin pitfalls
comments: true
---
During my work I found a way to trick Kotlin and put null into not nullable variable. 

Lets define data class in Kotlin:
{% gist eb15e71938244ddfc3b5b862a72e75d6 person.kt %}

and its representation in json:
{% gist eb15e71938244ddfc3b5b862a72e75d6 person.json %}

Now we can deserialize it like this:
{% gist eb15e71938244ddfc3b5b862a72e75d6 deserialize1.kt %}

What will happen if we try to deserialize following string?
{% gist eb15e71938244ddfc3b5b862a72e75d6 wrong1.json %}

address field is set as not nullable, but with value of null. WAT?
{% gist eb15e71938244ddfc3b5b862a72e75d6 wat.kt %}

What happened is that Gson is java library and it generates a java class. That class is compliled to Kotlin platform type that looks something like this:

{% gist eb15e71938244ddfc3b5b862a72e75d6 platformType.kt %}

Those exclamation marks shows, that this fields may or may not be nulls. More on platform types [here](https://www.youtube.com/watch?v=2IhT8HACc2E) and [here](https://kotlinlang.org/docs/reference/java-interop.html) 

So what to do now?
well only use non-null types if you are 100% sure, that json that contains that fields are filled. 
and our Person class should looke like this:
{% gist eb15e71938244ddfc3b5b862a72e75d6 properPerson.kt %}

Also please lookout for automatic json to object conversion f.e. using Retrofit!