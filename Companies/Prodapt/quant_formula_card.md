# Quant formula card — Prodapt (read the morning of the drive)

Covers every quant setup that appears in Prodapt's sample paper.
Written 4 Aug 2026, the day before the drive.

## 0. The one technique: ASSUME 100

The paper's quant is nearly all percentage RELATIONSHIPS, and it never
asks for the actual income/cost — only the change. So the base value is
free to choose. Choose 100.

    Spends 60% of income. Income +21%, expenditure +5%. Change in savings?

    algebra:     S = 0.4I -> 1.21I - 0.63I = 0.58I -> (0.58-0.4)/0.4   ~60s
    assume 100:  100 - 60 = 40 saved
                 121 - 63 = 58
                 18/40 = 45%                                            ~15s

## 1. CP / PROFIT / SP

    SP = CP + Profit

A percentage is meaningless without its BASE. Almost every trap here is
a switched base.

    "profit of 20%"            20% OF CP (CP is the default base)  SP = 1.2 CP
    "profit is 320% of cost"   profit = 3.2 CP                     SP = 4.2 CP
    "sold at 20% above cost"   same as profit of 20%               SP = 1.2 CP
    "profit is 20% OF SP"      profit = 0.2 SP, so CP = 0.8 SP
    "discount of 10%"          10% OF MP, never of CP              SP = 0.9 MP

METHOD — write three lines before any arithmetic:

    CP     = 100
    profit =            <- fill from the phrasing
    SP     =            <- CP + profit

Then re-read what is ASKED, and check which base the answer wants.

    Missed this on 4 Aug: "profit is 150% of cost" read as
    "SP is 150% of cost". Correct: profit = 150, SP = 250, not 150.
    Then divided cost by SP when the question asked for PROFIT as % of SP.

Conversions:

    profit x% on cost  ->  as % of SP  =  x / (100 + x)
    profit y% of SP    ->  on cost     =  y / (100 - y)

Marked price:

    MP - discount = SP = CP + profit
    successive discounts a% then b%  =  a + b - ab/100
    (or just multiply: MP x 0.9 x 0.95)

## 2. SIMPLE INTEREST

    SI = P x r x t / 100          A = P + SI

## 3. COMPOUND INTEREST

    A = P(1 + r/100)^t            CI = A - P

Two-year shortcut — avoid squaring, use a + b + ab/100 with both = r:

    effective 2-yr rate = 2r + r^2/100
        r = 5%   ->  10.25%
        r = 10%  ->  21%
        r = 20%  ->  44%

FRACTIONAL PERIODS (the paper asks 2 yr 4 mo) — compound the WHOLE
years, then apply SIMPLE interest on the resulting AMOUNT for the
leftover. Compounding does not happen mid-period.

    A = P(1 + r/100)^n x (1 + r*f/100)      f = leftover IN YEARS

    Two errors made on 4 Aug, both in the tail:
      - wrote r*6/100 for six months. f must be in YEARS: 6/12 = 0.5
      - applied the tail factor to the INTEREST instead of the AMOUNT.
        The tail is earned on the whole balance, principal included.

    Worked: CI on 8000 at 10% for 2 yr 6 mo
        2 yrs at 21%   ->  interest 1680,  amount 9680
        6 mths at 5%   ->  9680 x 0.05 = 484
        A = 10,164,  CI = 2,164

SANITY CHECK: a part-year tail can never exceed the whole-year
interest, and can never be negative. If it does, stop and redo.

CI - SI difference (asked constantly, instant):

    2 years:  P(r/100)^2
    3 years:  P(r/100)^2 x (3 + r/100)

## 4. WEIGHTED AVERAGE INTEREST

Rates CANNOT be averaged directly unless the principals are equal.
Convert every rate to RUPEES first, then it is plain subtraction.

    1. total interest = average rate x total principal
    2. subtract the interest from the known parts
    3. what is left / remaining principal = the missing rate

    Worked: 12,000 in three parts, 5% on 4,000, 8% on 5,000, r on the
    rest, overall average 7%.
        remainder      = 3,000
        total interest = 840
        known parts    = 200 + 400 = 600
        left           = 240  ->  240/3000 = 8%
        check: 200+400+240 = 840 = 7% of 12,000  OK

## 5. INCOME - EXPENDITURE - SAVINGS

Assume income 100. Savings = 100 - expenditure. Apply both increases,
then compare new savings with old savings. Never symbolic.

## 6. AVERAGES LOGIC

"Average of n numbers is zero — at most how many exceed zero?"  n - 1.
One sufficiently negative number offsets all the rest. Not n, since
they could not then sum to zero. Tests reasoning, not computation.

## 7. PROBABILITY

Simple favourable/total. 6 defective of 15 -> 6/15 = 2/5.

## 8. SYLLOGISM

DRAW THE CIRCLES. Do not reason verbally.
    "No A are B" + "No B are C"  =>  nothing follows about A and C.
    "No B is C"                  =>  "Some C are not B" DOES follow.

## Standing checks for tomorrow

- Every percentage: name its BASE before computing.
- Every profit question: write CP / profit / SP as three lines first.
- Every CI question: is the period whole? If not, tail is SIMPLE, on
  the AMOUNT, with f in YEARS.
- Every answer: does the magnitude make sense? Three misses on 4 Aug
  would all have been caught by a two-second plausibility check.
