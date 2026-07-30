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
