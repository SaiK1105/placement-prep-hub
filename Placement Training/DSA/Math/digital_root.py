# Digital Root — repeatedly sum digits until a single digit remains
# Verified 2026-07-19 (Tredence OA prep, "easy arithmetic" slot)
#
# Pattern: split digits -> aggregate -> repeat until condition
# Termination: for n > 9, digit_sum(n) < n (max 4-digit sum is 36 < 1000),
#              so n strictly decreases each iteration.
# Boundary: loop condition is n > 9, NOT n > 10 (n = 10 must enter the loop).
# String-free digit extraction: read last digit n % 10, drop it n // 10
#              (str(n) crashes on negatives: int("-") -> ValueError).


def digital_root(n: int) -> int:
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n


def digital_root_no_str(n: int) -> int:
    while n > 9:
        s = 0
        while n:
            s += n % 10
            n //= 10
        n = s
    return n


if __name__ == "__main__":
    assert digital_root(9875) == 2      # 9875 -> 29 -> 11 -> 2
    assert digital_root(10) == 1        # boundary: must enter loop
    assert digital_root(9) == 9         # single digit untouched
    assert digital_root_no_str(9875) == 2
    print("all tests pass")
