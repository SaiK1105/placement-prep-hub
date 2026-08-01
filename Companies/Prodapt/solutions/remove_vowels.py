# Prodapt sample paper — Coding Q3: removeVowels(N, S)
# Solved 2026-08-01. O(n) time, O(n) space (one slice). All asserts pass.
#
# "Output a new string after removing all the vowels from S that occurs
#  at the end of S." Both cases count. Output is guaranteed non-empty.
# 1 <= N <= 1e5.
#
# THE TRAP IS THE SENTENCE. Two readings:
#   (a) remove every vowel in S          -> "Programme" -> "Prgrmm"
#   (b) remove the TRAILING RUN of vowels -> "Programme" -> "Programm"
# It is (b). And it's a RUN, not one character: "India" -> "Ind",
# because dropping the 'a' exposes an 'i' that must also go.
#
# WHY NOT `S = S[:-1]` IN A LOOP: each slice copies the whole string,
# so N=1e5 becomes O(n^2). Count first, slice once.
#
# THE `[:-0]` LANDMINE: -0 == 0 in Python, so S[:-0] is S[:0] == "".
# If nothing needs removing and you slice by a count of 0, you return
# an empty string. Hence the `if n > 0` guard below. Tracking the cut
# POSITION instead of the count avoids the special case entirely:
#     i = len(S)
#     while i > 0 and S[i-1] in VOWELS: i -= 1
#     return S[:i]

VOWELS = "AEIOUaeiou"


def RemoveVowels(N, S):
    n = 0
    for i in range(1, N):
        if S[-i] in VOWELS:
            n += 1
        else:
            break
    if n > 0:
        return S[:-n]
    else:
        return S


if __name__ == "__main__":
    assert RemoveVowels(7, "Program") == "Program"      # ends in a consonant
    assert RemoveVowels(5, "India") == "Ind"            # run of two
    assert RemoveVowels(9, "Programme") == "Programm"   # interior vowels survive
    assert RemoveVowels(5, "HellO") == "Hell"           # uppercase vowel
    assert RemoveVowels(9, "beautiful") == "beautiful"  # vowel-dense, ends in 'l'
    assert RemoveVowels(3, "bea") == "b"
    assert RemoveVowels(1, "b") == "b"
    assert RemoveVowels(6, "aeioub") == "aeioub"        # leading vowels untouched

    print("all tests pass")

# KNOWN LIMITATION of `range(1, N)`: i runs 1..N-1, so S[-i] reaches
# S[1] but NEVER CHECKS S[0]. On an all-vowel string like "aeiou" this
# counts 4 and returns "a" instead of "". That input is excluded by the
# problem's "output will not be empty" guarantee, so this is correct AS
# SPECIFIED — but it leans on that guarantee. The cut-position version
# in the header comment does not.
