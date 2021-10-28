      ⍝ https://leetcode-cn.com/problems/reverse-integer/

      fn←{(×⍵)×10⊥⌽(|⍵)⊤⍨10⍴⍨⌈10⍟.2+|⍵}

      fn¨123 ¯123 120 0
321 ¯321 21 0
