---
layout: post
title:  dotSecurity dotScale
date:   2017-04-27 10:00 +0200
summary: conferences recap
comments: true
---
Last weekend I had a pleasure to attend dotSecurity conference and dotScale following Monday. Conferences took place in Paris in very atmospheric places (200 years old theatres). Either security or scaling, while very important topics, are not first class persons in mobile world, so that is the reason I decided to attend and widen my view on developing software. And I was charmed.  

![venue]({{ site.url }}/images/blog/1.jpg){:class="centered"}

The conference was prepared in Ted talks manner. Host encuraged people to talk to each other and every talk ended with short discussion about the talk with host. Which I think was very nice idea and great execution (the host was very well prepared for all the talks and asked questions that enriched expirience)

Here is a recap of talks (all will be available at [dotConferences](https://www.dotconferences.com/talks))
## dotSecurity
1. **Ingrid Epure**  
Talk about writing secure code in very fast changing codebase (400(?) commits to master a day).
Importance of automated checks was discussed. I liked end conversation where Ingrid pointed out that teaching newcomers should go along with using tools (couldn't agree more)
2. **Zane Lackey**  
He pointed out security should be visible to everyone especially managers. Zanes company has created monitoring tools for security so if you are interested you might visit [Signal Sciences](https://www.signalsciences.com/)
3. **Mikko Hypponen**  
Fight for security in future world. S stands for "Security" in IoT. Why Ikea is leading race in iot secure devices. and much more. So great talk, that I didn't have time to make notes :)
4. **Joseph Bonneau**  
Another awesome talk that made me thinking. Joseph discussed trusted lotteries, randomness beacons and applications of those. This talk convinced me that "blockchain" is not just empty buzzword. Later I've found some more material from Joseph on [coursera](https://www.coursera.org/learn/cryptocurrency/lecture/be6cd/bitcoin-as-an-append-only-log)
5. **Jim Manico**  
This charismatic fellow made some good points. Don't think about security in the end (or never) of development process. write it down. make it requirement. Hire security experts, so security does not need to be figured out during implementation (its too complex to figure it out by own in stessed conditions)
6. **Paul Mockapetris**  
Inventor of DNS talks about complexity of dns nowadays, how it evolved and also about firewall dns. 
7. **Philipp Jovanovic**  
Trust is the center of security. so trust none. use blockchain (or Decentralized witness cosigning). I'm wondering if we see this kind of solutions in wild. Lets hope so :)
8. **Tanja Lange**  
Post quantum cryptography. This was scary talk. and opened my eyes. I thought that quantum computers will be all nice and games, but it turned out that it will break private key crypto (so PGP, Signal, Bitcoin, HTTPS...). Also I didn't know that some organizations like NSA are storing all encrypted data in datacenters to break it in future (wow). People (Tanja included) started to figure it out with some success but a lot of more work is needed.
9. **Nick Sullivan**  
In the end Nick showed importance of TLS 1.3. 

## dotScale
this conference was concentrating more on server side and devops technologies. Still some talks were instested for me. I will only point out those:
1. **Aish Raj Dahal**  
Interesting talk about what to do when shit hits the fan :)
2. **Ulf Adams**  
Lead Bazel developer showed how they improved compile times at google. Unfortunately he didn't tell when bazel will become main build tool in android :(
4. **Benjamin Hindman**  
talks that server side infrastructure should be more like operating system.

To sum up I'm very pleased with those conferences. I feel very refreshed and exited about new things I've learned. It is a good thing to leave comfort zone from time to time.
