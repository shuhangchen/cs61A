(define (cddr s)
  (cdr (cdr s)))

(define (nth s n)
  (if (empty? s)
      nil
      (if (= n 1)
	  (car s)
	  (nth (cdr s) (- n 1)))))

(define (cadr s)
  'YOUR-CODE-HERE
  (nth s 2)
)

(define (caddr s)
  'YOUR-CODE-HERE
  (nth s 3)
)

(define (square x) (* x x))

(define (pow b n)
  'YOUR-CODE-HERE
  (if (= n 1)
      b
      (if (even? n)
	  (square (pow b (/ n 2)))
	  (* b (square (pow b (/ (- n 1) 2)))))))

(define (ordered? s)
  'YOUR-CODE-HERE
  (if (null? (cdr s))
      true 
      (and (<= (car s) (cadr s)) (ordered? (cdr s)))))


(define (no-repeats s)
  'YOUR-CODE-HERE
  (no-repeats-set s nil)
)
	  
(define (no-repeats-set s set)
  (if (or (null? s) (null? (cdr s)))
      (if (null? s)
	  s
	  (if (in-list set (car s))
	      nil
	      s))
      (if (in-list set (car s))
	  (no-repeats-set (cdr s) set)
	  (cons (car s) (no-repeats-set (cdr s) (cons (car s) set)))))
)
(define (in-list s n)
  (if (null? s)
      false 
      (or (= n (car s)) (in-list (cdr s) n)))
)

(define (nodots s)
  'YOUR-CODE-HERE
  (if (not (pair? s))
      (if (null? s)
	  s
	  (cons s nil))
      (if (pair? (car s))
	  (cons (nodots (car s)) (nodots (cdr s)))
	  (cons (car s) (nodots (cdr s)))))
)

(define (cons-list a b)
  (if (null? a)
      b
      (cons (car a) (cons-list (cdr a) b)))
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) false)
	  ((= (car s) v) true) 
	  (else (contains? (cdr s) v))
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return len(s) == 0
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)
(define (add s v)
    (cond ((empty? s) (list v))
	  ((< (car s) v) (cons (car s) (add (cdr s) v)))
	  ((> (car s) v) (cons v s))
          (else s) ; replace this line
          ))
(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
	  ((< (car s) (car t)) (intersect (cdr s) t))
	  ((> (car s) (car t)) (intersect s (cdr t)))
          (else (cons (car s) (intersect (cdr s) (cdr t)))) ; replace this line
          ))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
	  ((< (car s) (car t)) (cons (car s) (union (cdr s) t)))
	  ((> (car s) (car t)) (cons (car t) (union s (cdr t))))
          (else (cons (car s) (union (cdr s) (cdr t)))) ; replace this line
          ))

; A data abstraction for binary trees where nil represents the empty tree
(define (tree label left right) (list label left right))
(define (label t) (car t))
(define (left t) (cadr t))
(define (right t) (caddr t))
(define (empty? s) (null? s))
(define (leaf label) (tree label nil nil))
(define (in? t v)
    (cond ((empty? t) false)
	  ((< (label t) v) (in? (right t) v))
	  ((> (label t) v) (in? (left t) v))
          (else true)
          ))

; Equivalent Python code, for your reference:
;
; def contains(s, v):
;     if s.is_empty:
;         return False
;     elif s.label == v:
;         return True
;     elif s.label < v:
;         return contains(s.right, v)
;     elif s.label > v:
;         return contains(s.left, v)
(define (as-list t)
    (cond ((empty? t) t)
	  ((empty? (left t)) (cons (label t) (as-list (right t))))
	  (else (cons-list (as-list (left t)) (cons (label t) (as-list (right t))))))
)

