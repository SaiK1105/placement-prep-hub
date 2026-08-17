"""
TCS NQT — Day 1, Block 1.  Tier-A coding drill.   Budget: 90 min total.

  PROTOCOL (this is the whole point of the drill):
    1. Read ONE problem.  Start a clock.
    2. Write the ENTIRE solution in the stub.  Do not run anything.
    3. Dry-run it ON PAPER against the sample input.  Trace every variable.
    4. Re-read your code line by line looking for typos / wrong var names.
    5. ONLY THEN:  python day1_coding_drill.py 1
       If it fails, that counts as a "reset and retype" in the real exam.
       Note the failure in the log at the bottom of this file.

  Suggested clock:  Q1 20m · Q2 20m · Q3 25m · Q4 25m

  EXAM I/O RULES BEING REHEARSED HERE:
    - read STDIN with input(), write STDOUT with print()
    - print NOTHING extra (no "Enter a number:" prompts) — exact match
    - uppercase YES/NO when specified, f"{x:.2f}" when precision specified
"""

import sys, io, contextlib


# ══════════════════════════════════════════════════════════════════════
# Q1 — Balanced Brackets                                    [EASY · 20m]
# ══════════════════════════════════════════════════════════════════════
def q1():
    """
    A single line contains a string S made up only of the characters
    ( ) [ ] { }.

    If the string is balanced, print the number of matched pairs.
    Otherwise print -1.

    Constraints:  1 <= |S| <= 100000

    Sample Input 1        Sample Output 1
    {[()]}                3

    Sample Input 2        Sample Output 2
    ([)]                  -1
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════════════════════
# Q2 — Merge Two Sorted Arrays, Remove Duplicates           [EASY · 20m]
# ══════════════════════════════════════════════════════════════════════
def q2():
    """
    Line 1: N
    Line 2: N integers in ascending order
    Line 3: M
    Line 4: M integers in ascending order

    Print on line 1 the merged DISTINCT values in ascending order,
    space separated.  Print on line 2 the count of distinct values.

    Constraints:  1 <= N, M <= 100000 ;  -10^9 <= value <= 10^9

    Sample Input          Sample Output
    4                     1 2 3 4 5 7
    1 2 3 5               6
    4
    2 3 4 7
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════════════════════
# Q3 — Search a Sorted 2D Matrix                          [MEDIUM · 25m]
# ══════════════════════════════════════════════════════════════════════
def q3():
    """
    Line 1: R C
    Next R lines: C integers each.  Every row is sorted ascending left to
    right, and every column is sorted ascending top to bottom.
    Last line: K, the target.

    Print the 0-indexed row and column of K separated by a space.
    If K is not present, print "-1 -1".
    If K occurs more than once, print the occurrence with the smallest
    row index (and among those, the smallest column index).

    Constraints:  1 <= R, C <= 1000

    Sample Input          Sample Output
    3 3                   1 1
    1 4 7
    2 5 8
    3 6 9
    5
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════════════════════
# Q4 — Reverse the Second Half of a Linked List           [MEDIUM · 25m]
# ══════════════════════════════════════════════════════════════════════
def q4():
    """
    Line 1: N, the number of nodes.
    Line 2: N integers, the node values in order.

    Reverse the second half of the list and print the resulting values,
    space separated, on one line.

    If N is ODD, the middle node belongs to the SECOND half.

    Constraints:  1 <= N <= 100000

    Sample Input 1        Sample Output 1
    6                     1 2 3 6 5 4
    1 2 3 4 5 6

    Sample Input 2        Sample Output 2
    5                     1 2 5 4 3
    1 2 3 4 5
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════════════════════
#  HARNESS — you don't need to read below this line
# ══════════════════════════════════════════════════════════════════════

SOLUTIONS = {1: q1, 2: q2, 3: q3, 4: q4}

VISIBLE = {
    1: [("{[()]}", "3"), ("([)]", "-1")],
    2: [("4\n1 2 3 5\n4\n2 3 4 7", "1 2 3 4 5 7\n6")],
    3: [("3 3\n1 4 7\n2 5 8\n3 6 9\n5", "1 1")],
    4: [("6\n1 2 3 4 5 6", "1 2 3 6 5 4"), ("5\n1 2 3 4 5", "1 2 5 4 3")],
}


def run(fn, stdin_text):
    """Feed stdin_text to fn's input() calls, capture what it prints."""
    buf, real_stdin = io.StringIO(), sys.stdin
    sys.stdin = io.StringIO(stdin_text)
    try:
        with contextlib.redirect_stdout(buf):
            fn()
    finally:
        sys.stdin = real_stdin
    return buf.getvalue().strip()


def check(num, include_hidden=False):
    cases = list(VISIBLE[num]) + (list(HIDDEN[num]) if include_hidden else [])
    passed = 0
    for i, (stdin_text, expected) in enumerate(cases, 1):
        label = f"case {i}" + ("  [hidden]" if i > len(VISIBLE[num]) else "")
        try:
            got = run(SOLUTIONS[num], stdin_text)
        except Exception as e:
            print(f"  FAIL {label}: {type(e).__name__}: {e}")
            continue
        if got == expected.strip():
            print(f"  pass {label}")
            passed += 1
        else:
            print(f"  FAIL {label}")
            print(f"    stdin    {stdin_text!r}")
            print(f"    expected {expected.strip()!r}")
            print(f"    got      {got!r}")
    print(f"  {passed}/{len(cases)} passed\n")
    return passed == len(cases)


def _selftest():
    """One check that the harness itself works — asserts, no framework."""
    def echo():
        print(input().upper())
    assert run(echo, "yes") == "YES"
    def two_lines():
        n = int(input())
        print(" ".join(input().split()[:n]))
    assert run(two_lines, "2\na b c") == "a b"
    print("harness ok")


# ══════════════════════════════════════════════════════════════════════
#  ⛔ HIDDEN TEST CASES — do NOT scroll past here until your code is
#     written AND dry-run on paper.  Thinking of these yourself first
#     is the actual exercise.
# ══════════════════════════════════════════════════════════════════════

HIDDEN = {
    1: [
        ("()", "1"),
        ("(", "-1"),
        (")", "-1"),
        (")(", "-1"),
        ("((((", "-1"),
        ("{[]}()", "3"),
        ("[({})]", "3"),
        ("(()", "-1"),
    ],
    2: [
        ("1\n5\n1\n5", "5\n1"),
        ("3\n1 1 1\n3\n1 1 1", "1\n1"),
        ("2\n-5 0\n2\n0 9", "-5 0 9\n3"),
        ("3\n1 2 3\n3\n4 5 6", "1 2 3 4 5 6\n6"),
    ],
    3: [
        ("1 1\n7\n7", "0 0"),
        ("1 1\n7\n9", "-1 -1"),
        ("3 3\n1 4 7\n2 5 8\n3 6 9\n1", "0 0"),
        ("3 3\n1 4 7\n2 5 8\n3 6 9\n9", "2 2"),
        ("3 3\n1 4 7\n2 5 8\n3 6 9\n100", "-1 -1"),
        ("2 4\n1 2 3 4\n5 6 7 8\n6", "1 1"),
    ],
    4: [
        ("1\n9", "9"),
        ("2\n1 2", "1 2"),
        ("3\n1 2 3", "1 3 2"),
        ("4\n1 2 3 4", "1 2 4 3"),
        ("7\n1 2 3 4 5 6 7", "1 2 3 7 6 5 4"),
    ],
}


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "self"
    if arg == "self":
        _selftest()
    elif arg == "all":
        for n in SOLUTIONS:
            print(f"--- Q{n} ---")
            check(n, include_hidden=True)
    else:
        n = int(arg)
        print(f"--- Q{n} : visible cases ---")
        if check(n):
            print(f"--- Q{n} : hidden cases ---")
            check(n, include_hidden=True)


# ══════════════════════════════════════════════════════════════════════
#  FAILURE LOG — one line per failed first-compile.  This number is the
#  metric that matters, not whether you eventually solved it.
#
#  Q#  |  what broke on first run  |  would it have cost a retype?
#  ----|---------------------------|------------------------------
#
# ══════════════════════════════════════════════════════════════════════
