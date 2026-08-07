# A Palace of Ice at the End of the World

#### An interactive scroll-driven web-graphic-novel about the race to the South Pole — built with SvelteKit and D3.js.

_→ Live demo (coming soon)_

**TL;DR: A scrollytelling graphic novel where a D3.js map animates two historical expedition routes in real time as you read, fully synced to scroll position. Full multi-language routing, seamless scroll-based chapter transitions, a custom image performance pipeline, and a modular component system for effects like parallax and curved text. Made by a two-person team — concept, illustration, and all code by me; text and dialogue by my co-creator.**

---

_It's 1910. Two men. Two expeditions. One goal._

_British officer Robert Falcon Scott and Norwegian explorer Roald Amundsen set out on a perilous journey across the most unforgiving terrain on Earth — racing to be the first to reach the South Pole. Driven by ambition, but also by duty and an unbending will._

_What the history books record as a sporting contest was, in truth, a fight for survival — against cold, exhaustion, doubt, and the sheer, unforgiving vastness of the white continent._

_Based on the original expedition diaries, "A Palace of Ice at the End of the World" brings one of the most dramatic stories in the history of exploration back to life. Across six chapters and over 500 illustrated panels, Part One tells the story of how this race came to be._

_Let's get comfortable and cast off._

---
## About this repository

This repository is primarily a technical portfolio piece. The graphic novel is a collaboration within the artist collective DNA Graphic Novels, currently a two-person team: I brought the original concept, researched the historical diaries, created the illustrations, and built everything you see here technically; my co-creator wrote the text and dialogue. The graphic novel is promoted separately to readers — here, it serves to demonstrate what the code behind it can do.

I bring a dual background: illustration/design and software development. This project sits at the intersection of both — every technical decision here was made in service of a real, collaboratively-built piece of storytelling, not as an abstract exercise.

**What's next:** the components built here are laying the groundwork for an assistant tool that will help illustrators without a programming background build graphic novels like this one themselves.

---
## Tech stack
- SvelteKit (Svelte 5, runes syntax) — frontend framework
- D3.js — map projection, geographic calculations, dynamic SVG rendering
- TopoJSON — geographic data for landmasses
- Plain CSS for layout and animation, no UI library

---
## Architecture highlights

A few of the more interesting technical problems this project solves:

#### Scroll-synced, time-accurate map animation

A background map draws two historical expedition routes at the real pace they happened, not at a fixed scroll rate. A fixed D3 map sits behind the panels, tracing Scott's and Amundsen's routes as the reader scrolls — not linearly, but time-accurately: every coordinate carries a real timestamp, so fast legs of the journey draw quickly and slow legs draw slowly. The animation automatically pauses whenever a comic panel covers the map, and resumes only within the transparent scroll windows designed for it.

#### Multi-language routing done properly

Full [lang] routing with server-side language detection, clean shareable URLs, and no duplicated logic. Complete [lang]-based routing (German, English, Norwegian, easily extendable) with server-side language detection based on user preference and a fallback chain, clean URL structure (/en/chapter3) for SEO and shareability, and automatic sync between URL state and UI state.

#### Seamless chapter navigation

No "next chapter" button breaks immersion — scrolling itself carries you across chapter boundaries. Scroll-based transitions between chapters, backed by IntersectionObserver triggers with dwell-time tolerance to avoid false positives, unobtrusive fallback controls for accessibility and edge cases, and a themed loading transition that masks load time on slower devices.

#### An image performance pipeline built from scratch

A custom Python tooling chain cut illustration payload by over 80%, after vector export turned out to be the wrong format entirely. Illustrations originally exported as high-resolution vector graphics turned out to be a poor fit for the use case (megabytes per image due to vectorization artifacts from image-tracing). Built a custom Python tooling chain to convert to optimized raster formats, plus automated aspect-ratio extraction to prevent layout shifts under native lazy loading.

#### A modular component system

Text bubbles, curved text, parallax layers, and fully standalone "bonus" modules all plug into one generic rendering pipeline without touching its core. Text bubbles, text curving along SVG paths, parallax image layers, and fully self-contained "bonus" modules (e.g. interactive in-story newspaper pages) all plug into a shared generic image-rendering pipeline via a registry pattern, without ever modifying its core logic.

--- 
## Running locally
 
```bash
npm install
npm run dev
```
 
To access it from other devices on the same network (e.g. testing on tablets):
 
```bash
npm run dev -- --host
```

---
## Status

Actively in development. Chapters 1–6 are fully implemented; visual polish and additional chapters are ongoing.

---
## License

All rights reserved. This repository is shared publicly for portfolio and demonstration purposes only. No part of the code, story, illustrations, or any other content may be copied, modified, or reused — commercially or otherwise — without prior written permission.

If you'd like to use anything from this project, please reach out.

---
## Credits

A DNA Graphic Novels production.
Based on the historical diaries of the Scott and Amundsen expeditions (1910–1912).
