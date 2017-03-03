(fn fibo [n]
  (cond
    (= n 0) 0
    (= n 1) 1
    :else (loop [a 0, b 1, s 2, res 2]
            (if-not (= n s)
              (recur (b) (res) (inc s) (+ res b))
              res))))
