      ⍝ https://leetcode-cn.com/problems/single-number-ii/

      fn←+/{⍺×1=≢⍵}⌸

      fn¨(2 2 3 2)(0 1 0 1 0 1 99)
3 99
