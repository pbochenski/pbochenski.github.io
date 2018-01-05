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

What happened is that Gson creates object using default constructor (with no parameters) and than tries to fill the fields that are in json. If something is missing it stays as null.

So what to do now?
well only use non-null types if you are 100% sure, that json that contains that fields are filled. 
and our Person class should looke like this:
{% gist eb15e71938244ddfc3b5b862a72e75d6 properPerson.kt %}

If you are, like me, a fan of fail early paradigm then you can use copy function to validate object (as suggested by [mandrizzle](https://www.reddit.com/r/androiddev/comments/7c75yl/kotlin_pitfall_with_gson/dpsb682/)):
{% gist eb15e71938244ddfc3b5b862a72e75d6 enforce.kt %}

Also please lookout for automatic json to object conversion f.e. using Retrofit!

-- Updates based on feedback on reddit:
- how gson works
- using copy function to fail early.