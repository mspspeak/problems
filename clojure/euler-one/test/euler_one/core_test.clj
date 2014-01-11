(ns euler-one.core-test
  (:use clojure.test
        euler-one.core))

(deftest a-test
  (testing "divisible-by test pass"
    (is (divisible-by 15 3))))

(deftest b-test
  (testing "divisible-by test pass"
    (is (divisible-by 18 9))))

(deftest c-test
  (testing "divisible-by test pass"
    (is (divisible-by 180 6))))


(deftest fn-test-1st
  (testing "divisible-by test pass"
    (is ((divisible-by-x-or-y 3 5) 9))))

(deftest fn-test-2nd
  (testing "divisible-by test pass"
    (is ((divisible-by-x-or-y 3 5) 25))))
