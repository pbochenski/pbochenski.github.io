---
layout: post
title:  Testing android jsr310 backport
date:   2017-04-14 21:00:00 +0200
summary: code snippet
comments: true
---
When dealing with dates on android I use jsr310 [Android backport by Jake Wharton](https://github.com/JakeWharton/ThreeTenABP) . 
This library loads timezone data on app startup using AndroidThreeTen.init(this).
Unfortunately this uses context (this = Application) which is not aviable in unit tests. 

So just calling some functions that use dates will end in crash:
**org.threeten.bp.zone.ZoneRulesException: No time-zone data files registered**

How to fix that?
First thing to do is create resources folder in test path (f.e. project/src/test/resources).
Than copy [time zone database](https://github.com/JakeWharton/ThreeTenABP/raw/master/threetenabp/src/main/assets/org/threeten/bp/TZDB.dat)
 into that folder. After that I'm using following snippet (in Kotlin) to load database:
{% highlight kotlin %}
fun Any.loadTimeZone() {
    if (ZoneRulesProvider.getAvailableZoneIds().isEmpty()) {
        val stream = this.javaClass.classLoader.getResourceAsStream("TZDB.dat")
        stream.use(::TzdbZoneRulesProvider).apply {
            org.threeten.bp.zone.ZoneRulesProvider.registerProvider(this)
        }
    }
}
{% endhighlight %}

just calling this in any test class constructor: 
{% highlight kotlin %}
class SomeTestClass {

    init {
        loadTimeZone()
    }

    @Test
    fun shouldTest() {
        //your test here
    }
}
{% endhighlight %}

Happy testing!