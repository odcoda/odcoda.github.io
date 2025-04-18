---
layout: story
title: "The Akashic Record: System Design"
date: 1969-08-05
---

(Editor's note: the following is one of many documents recovered from the *pons* following the retrieval of the Ashburne local node from interstellar space. As one of relatively few twenty-first century scientist neural images within the *pons* with the mental capacity to comprehend the system in its entirety, your assistance in historical memeplex reconstruction is greatly appreciated. The document has been translated and re-rendered in a format that should be familiar to you. Please read and absorb it carefully. Post-processing will begin once you're finished.

Abstract: Monitoring, recording, and tracing the activity of individual users of the akashic layer remains an open question. Existing exhaustive proposals (e.g. Watson--Cascassia) are highly-secure but require parallel resources equal to if not larger than the system being monitored. We demonstrate that a simple astral injection and target-redirection can achieve secure recording with only a fraction of the cost, boosting the overall Kardashaev upper-bound on the King-wrapped Ra system to almost 94% of the original.

# (1) Background

The akashic system [1] provides a simple abstraction layer on top of the raw nonlocality interface. Requests are processed through a multimodal interpreter which permits only whitelisted operations. Through a condensed field-system emulator, fundamental means of abstraction and means of combination can be encoded and delivered to the underlying nonlocality system, without any loss of compressibility for safe operations. Provable safety guarantees are encoded within the akashic interpreter itself and can be checked computationally downstream.

The problem of monitoring and record-keeping was first observed in [2]. Given the potential for decay, misuse, and error, it's now recognized that a provably safe nonlocal-capable system must still satisfy the following real-world criteria:
* Composition: given an akashic request, administrators should be able to identify the corresponding nonlacal requests, and vice versa
 * Monitorability: for every akashic request, administrative records contain
   sufficient information to fully reconstruct the field-system state before the request, in real time
* Integrity: administrators have access to manual and automated operations to
  confirm that specific field-system states match observed outcomes, from large-scale down to individual waveforms.

A standard von Neumann--Huang field-system trace is the standard academic solution. However, it'slinear in both the number of system nodes and the time-granularity of the system being traced, which is immediately cost-prohibitive given the high-energy scale of the field-system emulator. Further works ([3], [4]) develop an automatically garbage-collected tag-and-track system, which can maintain a shadow history of every waveform within the field-system emulator. However, linking the shadow history to the original is complex -- playback must start from the full system snapshot, and proceed forward in time at max-simulation speed tracing an object to the present day (the "forward pass"), then run with time-reversed to capture pathts (the "backward pass"). Even assuming direct nonlocal computation (with no abstraction/safety controls on the monitor) the Kardashaev upper bound of full traces is 33%, once each for baseline and the forward/backward operations.

The Cascassia proposal relies

# (2) Review of nonlocal tracing

# (3) Tracing via waveform-pointer injection

# (4) Storage and retrieval of traces

# (5) 

Because we rely on the pointer-injection trick to save data, 

However, no proof can be perfectly applied to a real-world system, and 

[1] King et al, Akasia: safety through abstraction

[2] Watson
