((defn drop-n [s n]
    (loop [s s, res []]
        (if (empty? s)
             res
             (if (= (first s) n)
                  (recur (rest s) (res))
                  (recur (rest s) (conj res (first s)))))))

[3 8 2 1] 2)