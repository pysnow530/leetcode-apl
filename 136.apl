      ⍝ https://leetcode-cn.com/problems/single-number/

      fn←{⊃⍵/⍨1=+/∘.=⍨⍵}

      fn¨(2 2 1)(4 1 2 1 2)
1 4
