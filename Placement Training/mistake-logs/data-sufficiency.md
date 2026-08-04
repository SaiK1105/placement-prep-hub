# Data Sufficiency — mistake log

## Mistake — Data Sufficiency — reasoning-error

**What happened:**
Asked whether "n is a prime between 10 and 20" plus "n + 2 is also
prime" was sufficient to fix n, I answered E (together sufficient).
The candidates are 11, 13, 17, 19. Testing them: 11 -> 13 prime, and
17 -> 19 prime. TWO survive, so the data narrows n without pinning it.
The answer is D.

Same rule had already failed twice in the same set: x^2 = 49 (I called
it sufficient, but x = +/-7), and a two-digit number with digit sum 9
(nine candidates, and the second statement restated the first).

**Why:**
In my own words: "I didn't think about 11." I found a candidate that
satisfied both statements and stopped there. I never enumerated the
rest, so I never discovered a second survivor. Narrowing the field a
lot felt like sufficiency.

**Antidote:**
Before writing A, B, C or E, finish the sentence out loud:
"...therefore the answer is exactly ____, and nothing else."
If I cannot name the single value, I have not shown sufficiency —
I have shown narrowing, which scores as D.
When the candidate set is small and enumerable (primes in a range,
two-digit multiples, roots of a quadratic), LIST THEM ALL and count
the survivors. Stopping at the first hit is the bug.

## Mistake — Data Sufficiency / number properties — reasoning-error

**What happened:**
"Is n even, given n is divisible by 6?" — I answered D (not sufficient
even together). "Is m divisible by 4, given m is divisible by 8?" —
I answered B, which credits the wrong statement entirely. Both are
sufficient from statement I alone.

**Why:**
Not yet confirmed with a stated cause. Recorded because it fired twice
in one sitting, once inverted, which rules out a single slip.

**Antidote:**
Divisibility implication runs one way only — from the LARGER divisor
to its factors:
    divisible by 6  => divisible by 2 and by 3     (always)
    divisible by 8  => divisible by 4 and by 2     (always)
    divisible by 2  => divisible by 4              (NOT always: 2, 6, 10)
    divisible by 3  => divisible by 6              (NOT always: 3, 9, 15)
Test the doubtful direction with the smallest counterexample before
answering. For "divisible by 3 => even?", the number 3 settles it in
one second.
