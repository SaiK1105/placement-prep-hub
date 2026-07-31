# BFS / Level Order — mistake log

## Mistake — BFS Level Order (Right Side View) — reading-error

**What happened:**
Asked which node is visible from the right at each level, I answered
"node.right" — and repeated it after a counterexample was put in front
of me. The correct answer is the *last node of the level*, whichever
side it hangs from.

**Why:**
Word association. "Right side view" contained the word *right*, so I
mapped it straight onto the `.right` attribute without checking the
claim against a tree. I never actually tested it.

**Antidote:**
When a problem's English word matches a field name in my code
(`right`, `max`, `first`, `top`), stop and ask: "am I matching a word
or a definition?" Then draw the one tree where the two come apart —
here, a node whose only child is on the left.

## Mistake — BFS Level Order (Level Order Traversal II) — state-tracking-error

**What happened:**
Wrote the guarded child-pushes (`if node.left: q.append(...)`) at the
same indentation as the `for` loop instead of inside it. Passed the
sample test (right-heavy tree, so the bug didn't show), then failed
23/34 hidden cases. On `[1,2,3,4,5]`, only node 3's children (there are
none) got considered for pushing — node 1's and node 2's children were
silently dropped.

**Why:**
I was thinking "push children, once per level" instead of "push this
node's children, once per node popped." A node's `.left`/`.right` only
exist relative to that node — the push has to be scoped to the node,
not the level.

**Antidote:**
Before writing any line that reads `node.something` inside a level-BFS
loop, ask: "is this indented under the `for _ in range(size)`, or did
it drift out to the `while` level?" A silent-wrong-answer-on-hidden-
tests pattern (sample passes, most hidden cases fail) is this bug's
signature — check indentation scope first, before re-deriving logic.

**Recurrence — 2026-07-31, LC 103 Zigzag, inverted:**
Same root cause fired again the very next problem, in the opposite
direction: `flag += 1` (a per-LEVEL counter) was written inside the
`for`, so it counted nodes. Level `[9, 20]` bumped it twice and the
parity check went wrong from level 1 on.

Generalized antidote — for EVERY line in a level-BFS body, answer out
loud before typing it: "once per node, or once per level?"
  - per node   -> inside `for _ in range(size)`   -> anything `node.*`
  - per level  -> outside it, in the `while`      -> `size`, the level
    list, the counter/flag, `res.append(...)`
Two bugs in two problems, both from skipping this one question.
