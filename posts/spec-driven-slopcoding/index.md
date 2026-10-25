---
published: 20261025
title: Spec driven Slopcoding
wip: true
---

We now study the case of the **hackathon**, what was once represented by a 
caffeine and hope (mostly caffeine, though) fuelled sprint of pure code angst, 
and has now been transformed into a PowerPoint pitchathon and startup 
mongering hub.

But in the wild, we find the occasional true hackathon. A true exhibition of 
programming spirit; A true game of tradeoffs.

That isn't free from slopcoding, though. I'd actually endorse slopcoding for 
throwaway hackathon codebases; AI is gonna give you fast iteration and building
 speed, with none of the cons that you'd get when applying it to a real SDE job
.

---

## A slight tangent on Telemetrix
As you may know, I study at [Shiv Nadar University Chennai](https://www.snuchennai.edu.in).
 We have a yearly inter-college tech fest called Invente. And this year, we had
 Telemetrix, a hackathon event, as part of it. This wasn't just any hackathon, 
though. It was supposed to be sponsored and judged by [MotorQ](https://motorq.com), 
the company known by everybody at my college as the "1Cr package" company 
(I personally despise turning an entire company into a single transient metric. 
Yes, what you earn does matter, but reducing its entire engineering identity 
and culture as an engineer yourself, is just lazy thinking, IMHO).

And they delivered: the judges were SDE's at MotorQ, who were also our own 
senior alumni.

They also delivered in another unrelated but equally important way: they 
sponsored 4 crates of Sting (the energy drink) for free, for consumption by 
participants. Along with a crate of Slice tetra-paks, but everybody's too busy 
getting caffeine palpitations instead.

I personaly took home (with permission, geez, calm down) 10 bottles of Sting 
with me after the event :P. (The cache lasted me no longer than a week, though)
![Sting haul](images/sting_cache.jpeg)

---

## My hackathon methodology
- Get your idea, the inputs/outputs, and the scope set in stone. In my 
case, they'd asked us to build a vehicle telematics system, and I got the arch 
laid down in some time: pipelined process, transmission using QUIC, and visuals
 using Grafana.
- Break it into deliverable blocks/stages, preferably split cleanly as 
pipeline stages.
- Make a spec for each step/stage, and make insulated definitions about its 
inputs/outputs.
- Hand each stage one by one to an AI agent, testing subseqent stages together.
- Spec drift is inevitable to have occurred. Hence, let an AI agent look at 
everything at once and make integration fixes.

Is this incredibly inefficient? Probably. Is it required for modern coding 
agents/harnesses? Probably not. Is it the one I used to place **3rd** at this 
hackathon? **Yes**.

---

## Why I did what I did
I had no idea OpenCode had such a generous free tier. Other than that, I walked
 into the room with the preset assumption that AI coding free tiers would not 
be remotely enough to carry me to the podium.

What did I use instead? [zAI](https://chat.z.ai)'s Agent Mode. Rotating 3
alt accounts to bypass usage limits.
> As of right now, it is actually the _only_ mode to exist, with the old chat 
mode having been fully removed.

---

## How I did it
Broke the project into distinct modules:
- The fake data generation suite
- The transmitter
- The receiver
- The consumer, inferrer, and Grafana data provider

Chose JSONL as the transmission and storage medium. I would've used a database,
 if I had anything more than **4 hours** to finish writing and presenting this.

The transmitter/receiver modules were the simplest ones to get done. Asked the 
agent to build them as a pair using QUIC (aioquic being the choice of 
implementation) as the transport, and also implement some nifty certificate 
autogeneration. Idenfitied transmitters based on pinned SPKI. Just made the 
receiver log the received JSONL to disk.

The fake data generation was also mostly straightforward to implement. All I 
had to do was hand the bare minimum input parameter requirement the organizers 
gave us to the agent, and ask it to build a data generation script, with 
support for simulating scenarios like harsh braking, harsh acceleration, 
crashes, etc.

And finally, pasted the data spec into yet another session, and asked the agent
 to build an inference and visualization engine for these metrics using 
Grafana.

All roses? Seemingly, yeah.

---

## Spec drift
Remember me mentioning something about this earlier? Yeah, turns out I hadn't 
ensured that the data generator and inference engine shared the same set of 
assumptions about scenarios. Meaning, each worked with a different set of 
tolerances/constants for generating/detecting events in the scenario.

So what did I do? Blasted both files into a new session's context, and asked it
 to give me versions of both whose assumptions were synchronized.

Horrible and lazy? Probably, yeah. Did it work within the given time limit? 
Also yeah.

So at the end, I had this system that could generate data, transmit it, receive
 it, and display it with graphs and event anomaly logging.
