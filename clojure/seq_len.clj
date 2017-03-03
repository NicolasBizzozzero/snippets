(defn len [sequence]
    (loop [sequence sequence, res 0]
        (if (seq sequence)
            (recur (rest sequence) (inc res))
            res)))

(len '(1 2 3))
;; => 3

(len '())
;; => 0

(len [1 2 3])
;; => 3

(len [])
;; => 0

(len ["a" "b" "c"])
;; => 3


(defn get-last [sequence]
  (loop [sequence sequence]
    (if (= (len sequence) 1)
      (first sequence)
      (recur (rest sequence))))))

