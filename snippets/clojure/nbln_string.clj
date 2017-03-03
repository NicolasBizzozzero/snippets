;; http://www.braveclojure.com/organization/
;; https://clojure.org/reference/namespaces
;; https://clojure.github.io/clojure/clojure.test-api.html

(defn uppercase?
    "Return true if c is an uppercase character, false otherwise."
    [c]
    (.contains "ABCDEFGHIJKLMNOPQRSTUVXXYZ" c))

(defn lowercase?
    "Return true if c is a lowercase character, false otherwise."
    [c]
    (.contains "abcdefghijklmnopqrstuvwxyz" c))


(defn digit?
    "Return true if c is a digit character, false otherwise."
    [c]
    (.contains "0123456789" c))


(uppercase? "c")
