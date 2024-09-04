(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (ascending? lst)(or (null? (cdr lst))(and (<= (car lst) (cadr lst))) (ascending? (cdr (lst)))))

(define (interleave lst1 lst2)
  (cond ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else (cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2)))))))

(define (my-filter func lst)
  (cond ((null? lst) '())
        ((func (car lst)) 
            (cons (car lst) (my-filter func (cdr lst)))) 
        (else (my-filter func (cdr lst))))) 

(define (no-repeats lst)
  (define (helper seen lst)
    (cond ((null? lst) '())
          ((member (car lst) seen) (helper seen (cdr lst)))
          (else (cons (car lst) (helper (cons (car lst) seen) (cdr lst)))))) 
  (helper '() lst)) 
