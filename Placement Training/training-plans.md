# Training Plans — written 21 July 2026, after the 0-for-5 reset

Two plans. Plan A is the recommendation and the commitment. Plan B is a
one-week intensive to be used deliberately, not emotionally.

Honest note up front: **no plan makes you an expert in 1 week.** Expertise
is ~300 reps; a week buys ~40. What a hard week CAN do: build typing-level
fluency on the core patterns, calibrate you to exam difficulty, and break
the "blank editor panic" reflex. That's a launch ramp, not a destination.

---

## PLAN A — The Contract (recommended · ~2–2.5 h/day · 8 weeks)

The rule: this happens EVERY day. A short day is 1 problem, never 0.

| Slot | What | Rules |
|---|---|---|
| Daily · ~90 min | **3 DSA problems** from the 210-tracker, ladder order | 25-min timer each. Stuck → read APPROACH only, close it, type full solution yourself. Submit on LeetCode. No solution-reading without a retype from blank. |
| Daily · 20 min | **Timed aptitude** (aptitude-coach or HQ drills) | Includes pseudocode/output-tracing. Timer always on. |
| Mon/Wed/Fri · 30 min | **SQL** — LeetCode SQL 50, in order | Executed against a real engine, never solved "by eye". |
| Sunday · 2 h | **Cold mock**: MCQ block + 2–3 DSA + 1 SQL | Exam conditions. Scored honestly. Every miss → root cause → next week's drills target it. |

**Ladder order:** arrays/strings → hashing → two pointers/sliding window →
binary search → stack/queue → linked list → trees/BFS/DFS → heap → greedy →
DP basics → graphs.

**Weekly volume:** ~21 DSA + ~9 SQL + 1 mock.
**8-week output:** ~170 DSA reps + SQL 50 done + 8 exam-tier mocks.

Milestones:
- Week 2: arrays/strings/hashing clean at medium tier
- Week 4: clearing 2-of-3 mediums in Sunday mocks
- Week 6: medium-hards entering the mix
- Week 8: full OA sims at real difficulty, consistently above cut-line pace

---

## PLAN B — Hell Week (7 days · ~6–7 h/day · push tier)

Use when: an OA is <2 weeks out, OR as an aggressive launch ramp into Plan A.
Sleep 7+ hours — it is part of the plan, not a luxury to cut. If you miss a
day, you don't "make it up" — you fall back into Plan A. That's the deal.

**Daily structure (Days 1–6):**

| Block | Time | What |
|---|---|---|
| Morning | 2.5 h | **5 DSA problems**, ladder order, 25-min cap each. Cap hit → approach-peek → full retype from blank. |
| Midday | 1 h | **7 SQL problems** (SQL 50 pace) |
| Afternoon | 1.5 h | **Consolidation**: yesterday's misses re-solved from a BLANK editor (not reviewed — re-solved) + 30 min timed aptitude |
| Evening | 1.5–2 h | Alternates: **odd days** = 60–90 min cold mini-mock · **even days** = 2 hard problems worked Socratically (tutor mode, invariants stated before code) |

**Day 7:** Full OA simulation — 2 h, MCQ + 3 DSA (M/M/MH) + 1 SQL, cold.
Then full review: root-cause every miss, write the week's mistake log,
decide next week's Plan A entry point.

**Week output:** ~35 DSA + ~20 SQL + 3 mini-mocks + 1 full sim (~40 reps).

**What this week will actually give you:** heapq/Counter/two-pointer
skeletons that come out of your fingers without thought, calibration to real
exam tier, and 4 cold-exam exposures. **What it will not give you:** graphs,
DP depth, or "expert". Those come from Plan A's weeks 4–8.

---

## The recommendation

Run **Hell Week now** (today's fire is fuel — use it), then drop into
**Plan A from Monday 28 July** and hold it through September. Hell Week
without Plan A after it is a crash diet; Plan A is the actual transformation.

Either way, Day 1 opens with the **45-minute baseline** (2 problems, cold)
so the ladder starts at the right rung.

## Language policy (decided 22 Jul — do not re-litigate)
- **Python is the primary language.** All Hell Week + Contract weeks 1–4 reps
  in Python only. One language, maximum fluency — that's the rebuild.
- **Weeks 5–8: +15 min/day Java revival** — re-type ONE already-solved
  problem in Java (logic known, syntax revival only: HashMap, PriorityQueue,
  arrays vs ArrayList). Covers "do it in Java" interview moments.
- **Per-company recon checks allowed languages** 2 days out. Python 3 is
  allowed on virtually every campus platform (HackerEarth/HackerRank/
  HirePro/Codility); if a drive ever locks Java, that company's
  format-matched mock is done in Java.

## Non-negotiables (both plans)
1. Every problem TYPED and SUBMITTED — reading ≠ reps
2. Timer on everything
3. Misses get root causes, not shrugs (mistake log)
4. Mock results are the only readiness signal we trust
5. Per-company prep = format/logistics recon only, 2 days out, one
   format-matched mock. No content prediction cramming, ever again.
