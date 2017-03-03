(defn my-inc
    "Return `n` incremented by one."
    [n]
    (+ n 1))

(my-inc 4)
;; => 5

(defn map
  "Applique la fonction `f` sur toute la séquence `s`."
  [f s]
  (if (seq s)
    (lazy-seq (cons (f (first s)) (map f (rest s))))
    ()))

(defn filter
  [p? s]
  (if (seq s)
    (if (p? (first s))
      (lazy-seq (cons (first s) (filter p? (rest s))))
      (recur p? (rest s)))
    ()))



(defn max
  [& ints]
  )

(defn min
  [& ints]
  )

(defn med
  [& ints]
  )

(defn sum
  [& ints]
  )




(defn produit
    "Le produit d'une séquence finie d'entiers."
    [s]
    (loop [s s, res 1]
        (if (seq s)
            (recur (rest s) (* res (first s)))
            res)))

(defn my-take
    "Prends les `n` premiers termes de `s`."
    [n s]
    (loop [n n, s s, res []]
        (if (and (seq s) (> n 0))
            (recur (dec n) (rest s) (conj res (first s)))
            res)))


(defn compter-les-bleus
    [s]
    (reduce (fn [res element]
                (if (= element :bleu)
                  (inc res)
                  res)) 0 s))

(compter-les-bleus [:bleu :rouge :noir :bleu :vert])


(defn my-reduce
    "La séquence s doit être finie"
    [f init s]
    (loop [s s, res init]
        (if (seq s)
            (recur (rest s) (f res (first s)))
            res)))





;; Calcul des n premiers entiers en strict:

(defn divisible-par?
    "Retourne true si `n` est divisible par un des `entiers`."
    [n entiers]
      (loop [s entiers]
        (and (seq s) (or (= (mod n (first s)) 0)
                         (recur (rest s))))))

(divisible-par? 3 #{2 4 7})
;; => nil
(divisible-par? 3 #{3 4 7})
;; => true
(divisible-par? 3 #{})
;; => nil
(divisible-par? 2 #{2})
;; => true

(defn premiers
    "Génère une séquence des `n` plus petits nombres premiers."
    [n]
    (loop [i 2, res #{}]
      (if (< (count res) n)
        (recur
          (inc i)
          (if (divisible-par? i res)
            res
            (conj, res i)))
      res)))

(premiers 10)
;; => #{2 3 5 7 11 13 17 19 23 29}



;; Calcul des n premiers entiers en lazy:

(defn naturels
  "Génère une séquence des entiers naturels successifs à partir de 0. Si `n` est ajouté, on commence à générer à partir de `n`."
  ([] (naturels 0))
  ([n] (lazy-seq (cons n (naturels (inc n))))))

(take 5 (naturels))
;; => (0 1 2 3 4)
(take 5 (naturels 10))
;; => (10 11 12 )






(defn premiers-lazy
  "Génère les nombres premiers à la demande."
  ([] (premiers-lazy 2 #{}))
  ([n prs]
    (if (divisible-par? n prs)
      (premiers-lazy (inc n) prs)
      (lazy-seq (cons n (premiers-lazy (inc n ) (conj prs n)))))))

(take 5 (premiers-lazy))
;; => (2 3 5 7 11)
(into #{} (take 6 (premiers-lazy)))
;; => #{2 3 5 7 11 13}








;; les combinateurs de séquence
;; On prends une séquence pour obtenir une séquence

(take 6 (map (fn [x] (* x x)) (naturels 1)))
(take 6 (map #(* % %) (naturels 1)))
;; => (1 4 9 16 25 3)

;;(filter p? s) Génère la sous-séquence paresseuse des éléments de la séquence s pour lesquels le prédicat p? retourne ni false ni nil.

(take 6 (filter even? (naturels 1)))
;; => (2 4 6 8 10 12)

(take 6 (filter #(> % 10) (premiers-lazy)))
;; => (11 13 17 19 23 29)


((defn drop-n [s n]
    (loop [s s, res []]
        (if (empty? s)
             res
             (if (= (first s) n)
                  (recur (rest s) (res))
                  (recur (rest s) (conj res (first s))))))))




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
      (recur (rest sequence)))))

