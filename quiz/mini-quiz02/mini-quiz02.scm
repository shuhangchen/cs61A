(define (deep-map fn s)
  'YOUR-CODE-HERE
  (cond ((null? s) s)
	((pair? (car s)) (cons (deep-map fn (car s)) (deep-map fn (cdr s))))
	(else (cons (fn (car s)) (deep-map fn (cdr s)))))
)

