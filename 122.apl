⍝ https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/

      fn←{+/2÷⍨(|-⊢)2-/⍵}

⍝ tests
      tests←(7 1 5 3 6 4)(1 2 3 4 5)(7 6 4 3 1)
      fn¨tests
7 4 0
