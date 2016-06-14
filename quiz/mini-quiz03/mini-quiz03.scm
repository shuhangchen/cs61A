; Load this file into an interactive session with:
; python3 scheme -load quiz03.scm

(define (rle s)
  (rle-with-header s nil)
)


(define (rle-with-header s header)
  (if (null? s)
      nil
      (if (null? header)
	  (combine (list (car s) 1) (rle-with-header (cdr s) (list (car s) 1)))
	  (if (= (car header) (car s))
	      (combine (list (car s) (+ (car (cdr header)) 1)) (rle-with-header (cdr s) (list (car s) (+ (car (cdr header))))))
	      (combine (list (car s) 1) (rle-with-header (cdr s) (list (car s) 1)))))))

(define (combine list lists)
  (if (null? lists)
      (cons list nil)
      (if (= (car list) (car (car lists)))
	  lists
	  (cons list lists))))


(define s (cons 1 (cons 1 (cons 2 nil))))

(rle s)
