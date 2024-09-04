(define (over-or-under num1 num2) 
  (cond ((< num1 num2) -1)
        ((= num1 num2) 0)
        ((> num1 num2) 1)))

(define (make-adder num)
   (lambda (x) (+ x num)))

(define (composed f g)
  (lambda (x) (f (g x))))

(define (square n) (* n n))

(define (pow base exp)
  (cond ((= exp 0) 1)
        ((= base 1) 1)
        ((even? exp) (let ((half (pow base (/ exp 2))))
                       (* half half)))
        (else (* base (pow base (- exp 1))))))
