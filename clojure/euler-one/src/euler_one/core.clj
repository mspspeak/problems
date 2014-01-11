(ns euler-one.core
  (:gen-class))


; If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
; Find the sum of all the multiples of 3 or 5 below 1000.

(defn divisible-by [a b] (= (mod a b) 0))

(defn divisible-by-x-or-y [x y] #(or (divisible-by % x) (divisible-by % y)))

(defn -main
  "Sum the numbers below 1000 disible by 3 or 5"
  [& args]
  ;; work around dangerous default behaviour in Clojure
  (alter-var-root #'*read-eval* (constantly false))
  (println (reduce + (filter (divisible-by-x-or-y 3 5) (range 1000))) ))
