;; `map` apply the unary function `inc` over each element of the sequence.
(map inc [1 2 3 4])
;; => (2 3 4 5)


;; `reduce` apply the binary function `+` over the element `0` and the
;; first element of the sequence, then apply the previous result to the
;; second element of the sequence, etc.
(reduce + 0 [1 2 3 4])
;; => 10


;; `filter` remove the element of the sequence for which the predicat is
;; `false`.
(filter odd? [1 2 3 4])
;; => (1 3)
