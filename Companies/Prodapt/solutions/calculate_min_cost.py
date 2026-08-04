# Prodapt sample paper — Coding Q2: calculateMinCost(N, K, S)
# Solved 2026-08-04, night before the drive. O(N^2*K) DP + O(N^3) cost
# precompute. N <= 200, K <= min(N,10). All asserts pass.
#
# Split S into exactly K contiguous parts. A part's cost = number of
# ways to choose two equal substrings inside it (overlaps allowed).
# Minimise the total cost across all K parts.
#
# THE STATE. Packing analogy: you're filling K boxes left to right.
# Once box k is sealed, later boxes never look inside it — all they
# know is "i characters are already used, k boxes are already filled".
# The exact earlier split (e.g. "ab"+"cd" vs "a"+"bcd" for the same
# 4 characters, 2 boxes) is invisible from that point on, because
# whatever comes next only depends on (i, k), never on the history
# that produced them. That's optimal substructure, and it's why
# dp[k][i] can be a table instead of trying every partition directly.
#
# THE CHOICE. To reach dp[k][i], the LAST box (box k) covers some
# S[j:i]. Boxes 1..k-1 must fit in the first j characters, each with
# at least 1 char, so j ranges from (k-1) up to (i-1).
#
#     dp[k][i] = min over j in [k-1, i-1] of
#                    dp[k-1][j] + cost(S[j:i])
#
# BASE CASES.
#     dp[0][0] = 0        empty string, zero boxes, nothing to pay
#     dp[0][i] = +inf      i>0     characters exist but no box claims
#                                  them -- impossible, must never win a min
#
# THE COST FUNCTION is a separate, independent piece — group a part's
# substrings by content; a group of size m contributes C(m,2) pairs.
# Verified against the paper's own worked example: cost("aaaa") == 10.
# Must NOT be recomputed inside the DP loop; precompute a table once.
#
# COMPLEXITY. cost() is O(L^3) for a part of length L (enumerate O(L^2)
# substrings, O(L) each to build/hash) — fine for a single part, but
# computing it fresh for every (j,i) pair inside the DP would blow the
# budget. Precomputing partCost[j][i] for all pairs up front is
# O(N^3) worst case, and the DP itself is O(N^2 * K) = 200*200*10 =
# 400k. Both comfortable for N <= 200.
#
# PARTIAL CREDIT STRATEGY (exam day): if the cost function proves
# unreliable under time pressure, submit the DP with even a naive cost
# call anyway. It passes small cases and only times out on large ones
# — which scores more than an empty function. Never leave this blank.

from collections import Counter
import math


def cost(part):
    n = len(part)
    counts = Counter()
    for i in range(n):
        for j in range(i + 1, n + 1):
            counts[part[i:j]] += 1
    total = 0
    for c in counts.values():
        total += c * (c - 1) // 2
    return total


def calculateMinCost(N, K, S):
    # partCost[j][i] = cost of the part S[j:i], for every valid (j, i)
    partCost = [[0] * (N + 1) for _ in range(N + 1)]
    for j in range(N):
        for i in range(j + 1, N + 1):
            partCost[j][i] = cost(S[j:i])

    dp = [[math.inf] * (N + 1) for _ in range(K + 1)]
    dp[0][0] = 0

    for k in range(1, K + 1):
        for i in range(k, N + 1):
            for j in range(k - 1, i):
                if dp[k - 1][j] + partCost[j][i] < dp[k][i]:
                    dp[k][i] = dp[k - 1][j] + partCost[j][i]

    return dp[K][N]


if __name__ == "__main__":
    # the paper's own worked example, as a single part
    assert calculateMinCost(4, 1, "aaaa") == 10

    # every part a single character -> no pairs possible anywhere
    assert calculateMinCost(4, 4, "aaaa") == 0

    # THE test that proves the DP is actually searching, not guessing:
    # "a"+"aaa" = 0+4 = 4, "aaa"+"a" = 4+0 = 4, "aa"+"aa" = 1+1 = 2.
    # The optimum splits the string EVENLY, and only the DP (trying
    # every j) finds that -- a greedy left-to-right split would not.
    assert calculateMinCost(4, 2, "aaaa") == 2

    # no repeated characters anywhere -> cost is 0 regardless of K
    assert calculateMinCost(5, 1, "abcde") == 0

    print("all tests pass")
