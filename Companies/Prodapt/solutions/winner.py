# Prodapt sample paper — Coding Q1: winner(erica, bob)
# Solved 2026-08-01. O(n) time, O(1) space. All asserts pass.
#
# Hackathon over n days. Each day offers one Easy, one Medium, one Hard
# question; each person solves exactly one. erica[i] / bob[i] are the
# difficulties solved on day i. Higher difficulty = more points.
# Return "Erica", "Bob" or "Tie". Constraint: 0 < n < 10.
#
# !! THE POINTS TABLE IS AN IMAGE IN THE PDF and could not be read.
#    E=1, M=3, H=5 is a PLACEHOLDER. Read the real table on the day and
#    change the one dict below — that is the only line that moves.
#
# The trap: this is NOT "who won more days". It compares two TOTALS.
# One hard problem outweighs two medium ones, so a person can lose most
# days and still win. The last assert below is the case where day-
# counting and total-comparison disagree.

POINTS = {"E": 1, "M": 3, "H": 5}


def winner(erica, bob):
    e_score = sum(POINTS[c] for c in erica)
    b_score = sum(POINTS[c] for c in bob)
    if e_score > b_score:
        return "Erica"
    elif e_score < b_score:
        return "Bob"
    return "Tie"


if __name__ == "__main__":
    # the paper's own example
    assert winner(["E"], ["E"]) == "Tie"

    assert winner(["H", "H", "M"], ["E", "E", "E"]) == "Erica"
    assert winner(["E", "E"], ["H", "M"]) == "Bob"

    # THE test that matters: Erica wins 2 of 3 days —
    #   day 0  M(3) vs E(1)  Erica
    #   day 1  M(3) vs E(1)  Erica
    #   day 2  E(1) vs H(5)  Bob
    # ...and the answer is still a Tie, 7-7. A day-counting bug
    # returns "Erica" here and passes every other case above.
    assert winner(["M", "M", "E"], ["E", "E", "H"]) == "Tie"

    print("all tests pass")
