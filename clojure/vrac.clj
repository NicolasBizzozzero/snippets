(ns snippets.clojure.vrac
    (:gen-class))


(def PI 3.14159265358979323846264338327950288419716939937510582097494459230781)

(def π PI)


(defn abs
    [n]
    (max n (- n)))

(abs 1)
;; => 1

(abs -1)
;; => 1

(abs 0)
;; => 0


(defn floor
    [n]
    (int (Math/floor n)))

(floor 4.0)
;; => 4

(floor 4.9)
;; => 4

(floor -4.5)
;; => -5


(defn ceil
    [n]
    (int (Math/ceil n)))

(ceil 4.0)
;; => 4

(ceil 4.9)
;; => 5

(ceil -4.5)
;; => -4


(defn delta
    [n1 n2]
    (abs (- n1 n2)))

(delta 4 5)
;; => 1

(delta 5 4)
;; => 1


(def ∆ delta)


(defn round
    [n]
    (let [res-floor (∆ n (floor n))
          res-ceil (∆ n (ceil n))]
        (if (<= res-floor res-ceil)
            (floor n)
            (ceil n))))

(round 4.4)
;; => 4

(round 4.6)
;; => 5

(round 4.5)
;; => 4


(defn sum
    [& ints]
    (reduce + 0 ints))

(sum 1 2 3)
;; => 6

(sum 1)
;; => 1


(defn mean
    [& ints]
    (* (apply sum ints) (/ (count ints))))

(mean 1 2 3)
;; => 2N

(mean 1 2 3 4)
;; => 5/2

(mean 1)
;; => 1


(defn median
    [& ints]
    (nth (sort ints) (quot (count ints) 2)))

(median 1 2 3)
;; => 2

(median 3 1 2)
;; => 2

(median 1 2 3 4)
;; => 3

(median 1)
;; => 1


(defn divisible?
    [dividend divisor]
    (zero? (mod dividend divisor)))

(divisible? 10 5)
;; => true

(divisible? 10 6)
;; => false

(divisible? 10 10)
;; => true

(divisible? 10 -1)
;; => true


(defn not-divisible?
    [dividend divisor]
    (not (zero? (mod dividend divisor))))

(not-divisible? 10 5)
;; => false

(not-divisible? 10 6)
;; => true

(not-divisible? 10 10)
;; => false

(not-divisible? 10 -1)
;; => false


(defn setify
    [s]
    (into #{} s))


(defn vectify
    [s]
    (into [] s))
