---
name: oa-prep-builder
description: Build a company-specific OA prep plan, "Prep HQ" dashboard, and predicted mock paper. Use whenever the user mentions an upcoming company assessment or interview — "I have an OA", "X company test tomorrow", "prepare me for <company>", "make a prep plan", "predicted paper", "what should I study for <company>", or drops a new JD/company folder into Companies/. This is the established workflow for every company in this repo (Morgan Stanley, Presidio, Tredence, Swym already follow it) — new companies get the same treatment.
---

# OA Prep Builder

Every company S Sai Kumar interviews with gets a targeted prep package, built from research rather than generic advice. The pattern is proven — `Companies/Tredence/tredence_prep_hq.html` and `Companies/Morgan_Stanley/morgan_stanley_oa_prep_plan_mock_paper.html` are the reference implementations. Reproduce that quality for each new company.

## Step 1 — Gather intelligence

In order of trust:

1. **The JD** in `Companies/<company>/` — role, listed skills, assessment platform if named (Codility, HackerRank, SHL…). Platform determines format more than company does.
2. **Past papers** in `Placement material/<COMPANY>/` — if the company has a folder there, its old papers are the single best predictor of question style.
3. **Web research** — recent candidate reports (GfG experiences, Reddit, LeetCode discuss) for THIS role and batch year. Save findings to `Companies/<company>/research.txt` with sources, like the Morgan Stanley one.
4. **The tailored resume** in the company folder — interviews will probe what's on it.

State confidence honestly: distinguish "confirmed format from official guidelines" vs "predicted from 2 candidate reports". A prep plan built on a wrong format guess wastes the most scarce resource — the days before the test.

## Step 2 — Build the Prep HQ

One self-contained HTML file: `Companies/<company>/<company>_prep_hq.html`. No external dependencies (it gets opened from the filesystem, sometimes offline). Match the visual style of the existing prep HQs and the repo's Claude-style theme.

Sections (the Tredence structure, adapt as the format demands):

1. **Reality check / format** — what the OA actually looks like, sections, timing, and how confident each claim is
2. **Learn** — the 5–8 concepts this specific OA tests, each with a "prove it" self-check question
3. **Drill** — interactive practice questions with reveal-answer
4. **Weak spots** — a personal review deck (localStorage-backed if the existing tools do that)
5. **Mock** — timed MCQ section under exam conditions
6. **Coding** — 2–3 predicted coding questions with constraints, sized to the real time limit
7. **Interviews** — round-by-round notes on what THIS company's later rounds ask
8. **Sources** — where every prediction came from

## Step 3 — Predicted mock paper

The mock's value is calibration: same section order, question count, difficulty, and clock as the real thing. Base coding questions on past-paper patterns; write original questions in the same style, never copied verbatim (papers circulate and get patched — pattern-matching transfers, memorized answers don't).

## Step 4 — Time-boxed study plan

Scale the plan to reality: "OA tomorrow" gets a 1-night triage plan (highest-yield topics only, like the Swym one); a week out gets a day-by-day ramp ending in the mock 24h before. Always end the plan with: take the mock under real conditions, then drill only the misses.

## Companion skills

Hand off drilling to the specialists: aptitude sections → `aptitude-coach`, coding practice → `dsa-tutor` (with `problem-decoder`, `dry-run-coach`, `debug-coach`, `complexity-coach`, and `test-case-coach` for deeper passes on each stage), timed simulation and later rounds → `mock-interviewer`, post-solve generalization → `pattern-transfer-coach`.
