# Daily 20 Protocol — the volume escalation (declared 28 July 2026)

Goal stack, in your words: **become expert at DSA · cross 400+ LeetCode solved ·
finish the Striver A2Z sheet · minimum 20 questions/day, touching every DSA
topic every day.**

This is an escalation layer ON TOP of the Contract, not a replacement. The
Contract stays the frame — its ladder order, aptitude slot, SQL slot, and
Sunday mock are untouched. The only line that changes: "3 DSA problems/day"
becomes the **Daily 20 engine** below.

Honest math up front, same spirit as the Contract doc: expertise ≈ 300+ quality
reps. At 20/day this system produces **~135/week, ~1,000+ reps over 8 weeks**
(including spaced re-solves). That is expert territory — IF the reps are real:
typed, submitted, timed, and root-caused. 20 skimmed problems count as zero.

---

## The four blocks (every grind day = 3 + 8 + 6 + 3 = 20)

| Block | Q | Timer | What | Source |
|---|---|---|---|---|
| **A · Speed** | 3 | 8 min each | Arrays/strings/hashing maintenance reps at typing speed. This is the implementation-fluency attack — the gap that cost the 0-for-5 streak. Full code, submitted, no pauses. | `dsa_drill_expanded.html` arr/str/hash sections → then LC topic tag (Easy/Med) |
| **B · Spine** | 8 | 25 min each | Deep work on the **current Contract-ladder week** (reordered ladder: W1 grid DP → W2 graphs I → W3 graphs II → W4 DP core → W5 greedy/heap → W6 trees → W7 binsearch/stack/LL → W8 mixed hard). Stuck at cap → approach-peek → close it → full retype from blank. | A2Z step for that topic + `training_plans.html` linked problems + `matrix_mechanics.html` (W1) |
| **C · Coverage** | 6 | 25 min each | One problem from SIX topic families, every single day. This is what makes "touch every topic daily" literally true (map below). | A2Z topic steps → `dsa_drill_expanded.html` leftovers |
| **D · Revenge** | 3 | from blank | Re-solves from `mistake-logs/`, spaced at **+2 / +7 / +21 days**. Not reviewed — re-solved cold. If the queue is short, backfill with hardest recent B misses. | `mistake-logs/*.md` via tracker revenge queue |

**Block C daily family map** (sub-rotation keeps all 15 topics inside every week):

1. Binary search — every day
2. Linked list ⇄ Stack/Queue — alternate by day
3. Trees / BST — every day
4. Graphs — every day
5. DP — every day
6. Rotating third: Heap-Greedy → Recursion/Backtracking-Bit → Two-pointer/Sliding-window

So even in week 1 (grid DP spine), you still touch graphs, trees, binary
search, linked lists, and DP daily. No topic goes cold for more than 48 hours.

## Difficulty quota (per the calibration rule: train AT or ABOVE exam tier)

On a full day: **≤ 5 Easy · ≥ 12 Medium · Hard ≥ 1 (weeks 1–2) rising to ≥ 3
(week 3 onward).** Easy lives in Block A only. If a day ends all-Easy, it was a
comfort day, not a training day — the tracker's quota meter will call it.

## Day modes — 20 is the standard, never the excuse to hit zero

| Mode | Volume | When | Composition |
|---|---|---|---|
| **FULL** | 20 | Default grind day | A3 + B8 + C6 + D3 |
| **SUNDAY** | 20 | Every Sunday | A3 + B5 + **cold mock (3 DSA counted here, 65-min Staples format, plus the Contract's MCQ + SQL)** + C6 + D3 |
| **LIGHT** | 8 | OA day / interview day | A3 + B2 + D3 — the rest of the day belongs to that company's format recon |
| **HALF** | 10 | Collapse day (sick, travel, disaster) | A3 + C4 + D3 |

Contract rule inherited: **a short day is a declared LIGHT/HALF day, never 0.**
Streak survives any day that meets its declared mode's floor.

**Kill-switch (anti-crash-diet):** three consecutive days below floor → drop to
Contract 3/day for two days, then re-enter at FULL. Falling back is the plan
working, not the plan failing.

## Mental math warm-up — 5 min, and deliberately NOT part of the 20

Runs before block A. It is a habit, not a rep: it never counts toward the 20,
never feeds the streak, quota, coverage chips, or history bars. Inflating the
20 with a math drill would make "20/day" a lie, and the whole system depends on
that number being honest.

| Min | Slot | Why |
|---|---|---|
| 1–2 | **➗ Division** (double time) | Declared weak point, 29 Jul. Gets two of the five minutes until it graduates. |
| 3 | **🧩 Compound** | `(1222×56)+888` — finish the product, park it, then the ± tail. |
| 4 | **📖 Recite** — alternates fraction↔% / divisor-splits by date parity | The two tables that make everything else fast. |
| 5 | **⚡ % of number / profit chains** — alternates | The exact shape placement MCQs test. |

**Graduation rule (the only way division's extra minute is released):** tick
"cleared 10 division questions in a row with no 💡 hint" on **3 consecutive
days**. The tracker then rewrites the routine itself — division drops to 1 min,
compound takes the spare minute. Breaking the run restores the double
allocation automatically. Warm-up streak is gated on the division slot alone;
skipping it is skipping the point.

Trainer and the seven moves behind the drills: `mental_math_trainer.html`.
Tracked in `daily_20_tracker.html` as its own panel, with its own streak tile
and a green underline on the history bars.

## Time cost — no fantasy

A ≈ 25 min · B ≈ 2.5–3 h · C ≈ 2–2.5 h · D ≈ 40 min → **≈ 6–6.5 h/day**, plus
the Contract's 20-min aptitude daily and 30-min SQL Mon/Wed/Fri ≈ **7 h on the
heaviest days**. That is Hell-Week tier sustained for 8 weeks. You said push to
the limits — this is what the limit costs. Sleep 7+ hours; it's part of the
plan (Contract rule, unchanged).

## Striver A2Z mapping — how the sheet actually gets finished

Spine weeks consume the big steps; A + C mop up the rest continuously:

- **W1** → Step 16 (DP-on-grids section) + matrix mechanics
- **W2** → Step 15 first half (BFS/DFS, components, grid traversal)
- **W3** → Step 15 second half (Dijkstra, cycles, topo) + Step 7 backtracking
- **W4** → Step 16 remainder (1D, subsequences, knapsack, string DP)
- **W5** → Steps 11 Heaps + 12 Greedy
- **W6** → Steps 13 Binary Trees + 14 BST
- **W7** → Steps 4 Binary Search + 9 Stacks/Queues + 6 Linked List
- **W8** → Steps 17 Tries + 18 Hard Strings + leftovers + full sims
- **A + C continuously** → Steps 1–3 (basics/sorting/arrays), 5 (strings), 8 (bits), 10 (window/2-ptr)

At ~14 sheet-aligned problems/day the sheet's ~439–455 problems complete in
**5–6 weeks**; weeks 7–8 are hard-sim + weak-pattern purge. Step counts are
prefilled in the tracker but **editable — sync them once against the live
sheet** (linked from the tracker). No problem content in this repo is invented;
sources are the sheet, your 144-problem drill, and LeetCode itself.

## The 400+ crossing — projection, not prophecy

Velocity: ~17 new problems/day of which ~80% are LeetCode submissions ≈ **~95
LC/week**. From your actual current solved count (enter it in the tracker once,
then update it weekly from your real LC profile — that number is the only
truth):

| LC solved today | 400 crossed around |
|---|---|
| 50 | end of week 4 |
| 100 | mid week 3 |
| 150 | start of week 3 |

The tracker projects the crossing date from your **actual rolling 7-day
velocity**, not from this table. Mock results and the LC profile number are the
only readiness signals we trust — same as the Contract.

## Non-negotiables (inherited + new)

1. Every problem TYPED and SUBMITTED — reading ≠ reps.
2. Timer on everything; caps are caps.
3. Every miss → root cause in `mistake-logs/` using the taxonomy
   (`reasoning-error`, `pattern-recognition-error`, `implementation-error`,
   `reading-error`, `math-error`, `off-by-one`, `state-tracking-error`) → enters
   the revenge queue at +2/+7/+21 days. The tracker generates the log line;
   dsa-tutor confirms root causes — the tutor never invents one.
4. Python primary (language policy unchanged; weeks 5–8 add the 15-min Java
   revival rep, which does NOT count toward the 20).
5. Per-company prep = format recon only, 2 days out. No prediction cramming.
6. **This week's reality:** Qualcomm OneIT tonight 28 Jul 19:00 (C/C++ MCQ —
   today is LIGHT mode; the day belongs to the Qualcomm cheatsheet + output
   drills). Purchasing Power OA 29 Jul 13:30 → LIGHT. **Day 1 FULL = Thursday
   30 July.**

## Milestones

- **Week 2 end:** ≥ 250 cumulative reps, quota meter green ≥ 10 of 12 grind days
- **Week 3–5:** 400 LC crossed (per projection above)
- **Week 6 end:** A2Z sheet 100%
- **Week 8 end:** ~1,000 reps, 8 Sunday mocks above cut-line pace, mistake-log
  revenge queue empty for 7 straight days — that's what "expert" looks like on
  paper. The OAs will say whether it's real.

Tracker: `daily_20_tracker.html` (same folder — linked from the hub).
