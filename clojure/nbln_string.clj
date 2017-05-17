(ns snippets.clojure.nbln-string
    (:gen-class))


(def UPPERCASE "ABCDEFGHIJKLMNOPQRSTUVXXYZ")

(def LOWERCASE "abcdefghijklmnopqrstuvwxyz")

(def NUMBER "0123456789")


(defn uppercase?
    "Return true if c is an uppercase character, false otherwise."
    [c]
    (.contains UPPERCASE c))

(uppercase? "c")
;; => false

(uppercase? "C")
;; => true

(uppercase? "3")
;; => false


(defn lowercase?
    "Return true if c is a lowercase character, false otherwise."
    [c]
    (.contains LOWERCASE c))

(lowercase? "c")
;; => true

(lowercase? "C")
;; => false

(lowercase? "3")
;; => false


(defn digit?
    "Return true if c is a digit character, false otherwise."
    [c]
    (.contains NUMBER c))

(digit? "3")
;; => true

(digit? "C")
;; => false
