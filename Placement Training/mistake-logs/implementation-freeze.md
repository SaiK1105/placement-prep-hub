# Implementation Freeze

Cross-cutting, not tied to one pattern. Logged when the block is *starting to
write*, not the writing itself.

---

## Mistake — Tree recursion (Height of binary tree) — implementation-error

**What happened:**
I stated the full algorithm correctly in words — "1 + max(left, right), null
returns 0" — and then said "I don't know, help me form it" instead of writing
any code. Given one narrowing prompt, I wrote the entire function correctly on
the first attempt with no code shown to me.

**Why:**
In my own words: "didn't want to write something wrong, failed to convert my
thinking into code." The second half is contradicted by what actually happened
— the conversion took under a minute and was correct. The real cause was the
first half: unwillingness to commit a line that might be wrong.

**Antidote:**
Before asking for help, ask: "have I written a single line yet?" If no, write
the wrong version first — signature and base case only, two lines. A wrong line
on the page is worth more than a right one in my head, and in a timed OA a blank
editor scores zero regardless of what I understand.

**Watch for:** this misreporting itself as an "implementation-fluency gap" in
session notes. The evidence so far says the gap is *initiation*, not ability.
Re-test on every problem where I feel the urge to ask before typing.
