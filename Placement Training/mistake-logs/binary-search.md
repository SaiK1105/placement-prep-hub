# Binary Search — mistake log

## Mistake — Binary Search (LC 704, Classic) — off-by-one

**What happened:**
Wrote `h = len(nums) - 1` and `h = mid - 1` (both from the INCLUSIVE
convention) but `while l < h` (from the EXCLUSIVE one). On
`nums = [5], target = 5` the loop condition `0 < 0` is false, the body
never runs, and it returns -1.

**Why:**
I had the shape of binary search memorized without noticing that the
three moving parts — how `h` is initialized, the loop condition, and
how `h` moves — are not independent choices. They come as a set.

**Antidote:**
Before writing the loop, pick a row and say which one out loud:

    convention   init h      loop cond   move h
    inclusive    len-1       l <= h      h = mid - 1
    exclusive    len         l <  h      h = mid

Then check all three cells came from that row. If `h` can be a real
index, `l == h` is still a live range and the condition must be `<=`.

## Mistake — Binary Search (LC 34, First/Last Position) — implementation-error

**What happened:**
Two minutes after correctly reasoning out loud that a hit should NOT
return — "keep searching left, `h = mid`" — I typed the opposite:

    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        l = mid + 1        # inverted: bigger mid should move h, not l

Both errors are the memorized exact-match template, not the lower-bound
search I had just derived.

**Why:**
In my own words: "I defaulted to the standard binary search template I
memorized." The reasoning was correct and recent; the fingers reached
for the stored shape anyway. The template even overrode direction — I
moved `l` on `nums[mid] > target`, which no convention permits.

**Antidote:**
The moment I catch myself typing `return mid` inside a binary search,
stop and ask: "am I looking for A match, or THE BOUNDARY?"

  - A match      -> `return mid` is fine (LC 704)
  - The boundary -> there is NO early return; the loop runs to l == h
    and the answer is `l` (LC 35, LC 34, First Bad Version, Minimum in
    Rotated Sorted Array, Capacity To Ship Packages)

Boundary searches have exactly two branches and one return, at the end.
If I have written three branches, I have written the wrong algorithm.

**Signature of this bug:** it passes on arrays with no duplicates and
fails the moment the target repeats — which is precisely the input the
problem was built around.
