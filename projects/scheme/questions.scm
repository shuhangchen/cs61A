(define (cons-all first rests)
  (if (null? rests)
      nil
      (cons (cons first (car rests)) (cons-all first (cdr rests))))
)


;; Problem 18
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN Question 18
  (define (enumerate-index s num)
    (if (null? s)
	s
	(cons (cons num (cons (car s) nil)) (enumerate-index (cdr s) (+ num 1)))
	))
  (if (null? s)
      s
      (enumerate-index s 0)
  )
)
  ; END Question 18

;; Problem 19
;; List all ways to make change for TOTAL with DENOMS

;; define a test

(define (cons-lists lis1 lis2)
  (if (null? lis1)
      lis2
      (cons (car lis1) (cons-lists (cdr lis1) lis2)))
)

(define (list-change total denoms)
  (cut-all-0  (filter contains-0 (list-change-rough total denoms)))
)

(define (small-list-change  total denoms)
  (cond ((null? denoms) (list (list -1)))
	((< total 0) (list (list -1)))
	((= total 0) (list (list 0)))
	(else (cons-lists (cons-all (car denoms) (small-list-change (- total (car denoms)) denoms)) (small-list-change total (cdr denoms)))))
)

(define (list-change-rough total denoms)
  ; BEGIN Question 19
  (if (< total (car denoms))
      (list-change-rough total (cdr denoms))
      (small-list-change total denoms))
)

(define (cut-all-0 lists)
  (if (null? lists)
      nil
      (cons (cut-0 (car lists)) (cut-all-0 (cdr lists)))))

(define (cut-0 list)
  (if (null? list)
      nil
      (if (= 0 (car list))
	  (cut-0 (cdr list))
	  (cons (car list) (cut-0 (cdr list))))))

(define (contains-0 list)
  (if (null? list)
      false
      (or (= 0 (car list)) (contains-0 (cdr list)))))
	 
(define (filter fn lists)
  (if (null? lists)
      nil
      (if (fn (car lists))
	  (cons (car lists) (filter fn (cdr lists)))
	  (filter fn (cdr lists)))))



  ; END Question 19
(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cddr x) (cdr (cdr x)))
(define (cadar x) (car (cdr (car x))))

; Some utility functions that you may find useful to implement.
(define (map proc items)
  (if (null? items)
      nil
      (cons (proc (car items)) (map proc (cdr items)))))

(define (zip pairs)
  (if (null? pairs)
      (list nil nil)
      (let ((lis (zip (cdr pairs)))
	    (pair (car pairs)))
	(list (cons (car pair) (car lis))
	      (cons (cadr pair) (cadr lis))))))


;; Problem 20
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (analyze expr)
  (cond ((atom? expr)
         ; BEGIN Question 20
	 expr
         ; END Question 20
         )
        ((quoted? expr)
         ; BEGIN Question 20
	 expr
         ; END Question 20
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN Question 20
	   (cons form (cons params (map analyze body)))
           ; END Question 20
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN Question 20
	   (cons (cons 'lambda (cons (car (zip values)) (map analyze body))) (map analyze (cadr (zip values))))
           ; END Question 20
           ))
        (else
         ; BEGIN Question 20
         ; (cons (analyze (car expr)) (analyze (cdr expr)))
	 ; expr
	 (cons (analyze (car expr)) (map analyze (cdr expr)))
         ; END Question 20
         )))

;; Problem 21 (optional)
;; Draw the hax image using turtle graphics.
(define (hax d k)
  ; BEGIN Question 21
  'REPLACE-THIS-LINE
  )
  ; END Question 21

