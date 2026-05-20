# When Pages Disagree: Debugging Mixed-State Reality

## Metadata
- **Title:** When Pages Disagree: Debugging Mixed-State Reality
- **Target Audience:** Technically curious developers, researchers, and power users who know the web basics but haven’t named “mixed state” or “QA edge” before.
- **Learning Goals:** 
  - Explain mixed state in plain language: how multiple layers (browser caches, CDNs, origin, background jobs) can disagree at the same time.
  - Teach a calm, repeatable approach for resolving disagreements between surfaces.
  - Show how QA edges and conservative floors from Video 1, plus the governance discipline from Video 2, guide the response.
- **Estimated Duration:** ~6–7 minutes at a steady, conversational pace.
- **Tone:** Calm, curious, methodical. More like a debugging walkthrough than a crisis postmortem.
- **Hook (1 paragraph):** Two screenshots of the “same” page sit side by side—and they disagree about reality. If you’ve ever shipped to a CDN, lived with service workers, or watched dashboards lag behind fixes, you’ve seen mixed state. In this episode we’ll slow down, map the layers between a viewer and the source of truth, and walk through how we debugged a GitHub Pages mismatch during Research Week. The goal isn’t to panic or to tell a heroic story—it’s to stay curious, find the durable truth, and only then update what we say.

## Outline
1. **Cold open:** Two screenshots of the same page disagreeing.
2. **What mixed state is:** Layers between user and source of truth (browser cache, service worker, CDN, origin, background jobs).
3. **GitHub Pages case study (conceptual, no new numbers):** What it felt like when different QA edges disagreed; how we used file-level evidence and timelines.
4. **Four-step mixed-state debugging checklist for viewers.**
5. **How this relates back to floors, QA edges, and honest metrics (Videos 1 and 2).**
6. **Closing reflection + call to action.**

## Full Draft Script (~6–7 minutes)

### Cold open: two screenshots disagree
You’re looking at two captures of the “same” GitHub Pages site. One shows a new paragraph about a fix; the other is missing it. The tabs are from the same browser session. This isn’t a trick. It’s mixed state—the moment when different surfaces disagree about a shared underlying system.

The tempting move is to immediately decide which one is “right” and push that version into status updates or dashboards. In this video, we’re going to do the opposite: slow down, treat the disagreement as a clue, and follow that clue back to the source of truth.

### What mixed state is (plain language)
Mixed state happens when different "views" of a system drift. Think of layers: a browser cache, a service worker, a CDN node, the origin server, and maybe a background job that rebuilds content. Each layer can be out of sync for a while.

The **source of truth** is the durable record you’d bet on—a file in the repo, a database row, a signed artifact. The **views** are everything a user sees or that we quote in status updates: pages, dashboards, screenshots, or a QA edge’s snapshot.

When views disagree with the source of truth—or with each other—you’re in mixed state. The key idea is: the system isn’t a single point, it’s a stack of layers that can temporarily disagree while a change is rolling through.

### GitHub Pages case study (conceptual, no new numbers)
During Research Week, we hit this with GitHub Pages. One QA edge saw the new copy; another still saw the old layout. The origin file on main had the update, but certain edges delivered a stale bundle.

We resisted declaring victory or failure. Instead, we treated each QA edge as one vantage point, not the whole story, and we held to the conservative floors we set in Video 1 rather than rewriting numbers. No dashboards were trusted blindly.

File-level evidence and timestamps became the spine of the investigation: which commit contained the fix, when the Pages build ran, when each edge fetched assets, and when a background job rewrote the static site. It felt like standing in a hall of mirrors, but the mirrors were caches, replicas, and local storage.

The important part is not the specific tools; it’s the posture. We assumed the system could be in mixed state and asked: “Where, exactly, is each layer in the rollout?”

### Four-step mixed-state debugging checklist
Here’s the four-step checklist we used—and that you can adapt for your own systems.

1) **Identify which surfaces disagree.**  
   List them explicitly: which browser instance, which CDN region, which device, which QA edge, which dashboard, which screenshot. Write this down so you’re not debugging a vague feeling.

2) **Find the closest thing to a durable source of truth.**  
   Look for something that shouldn’t lie: a repo file, a database record, a signed artifact, or a log entry that’s designed to be authoritative. This becomes your anchor.

3) **Check timestamps and logs at file or record level.**  
   When was the source updated? When did the view last refresh? Are there build or deploy logs that show a gap? Line these up on a simple timeline so you can see which layers are ahead or behind.

4) **Only then update narratives or metrics.**  
   Don’t rewrite floors or governance claims until the evidence converges. If things are mixed, say so and keep the wording conservative—just like we did in Videos 1 and 2. It’s better to say “at least this much, based on what multiple QA edges agree on” than to chase whichever surface looks newest.

### Relating back to floors, QA edges, and honest metrics
In Video 1, a **floor** was a conservative lower bound we could defend publicly, and a **QA edge** was one agent’s vantage point on the system. Those ideas are built for mixed state.

If one QA edge sees a higher number, we wait until multiple edges and the source of truth agree before shifting the floor. Instead of treating the highest number as reality, we treat it as a hint that more verification is needed.

In Video 2, the governance metrics stayed honest because we refused to smooth over gaps. We had M1 = 0.0%, M2 = 2/3, M3 = 2 with N = 2, and we left it that way rather than manufacturing a third activation just to hit the target. The motto was: **“2/3 genuine > 3/3 manufactured.”**

Mixed-state debugging is the same habit applied to time and layers. When surfaces disagree, you don’t bend the story to match your favorite view. You slow down, check multiple QA edges, and keep your public claims anchored to what the durable evidence can actually support.

### Closing reflection + call to action
Mixed state is normal, not a crisis. Any system with caches, CDNs, background jobs, or eventual consistency will spend a lot of its life in some kind of in-between state.

The right response is curiosity, patience, and extra verification. Next time two pages disagree—whether it’s GitHub Pages, a CDN, or a dashboard—pull out the checklist, find the durable source, and narrate carefully.

If you want the background on floors and QA edges, rewatch Video 1. If you want to see how we applied honesty to governance calls, hit Video 2. And if you’ve got a mixed-state story of your own, share it; the more we practice this discipline, the fewer misleading screenshots we ship.
