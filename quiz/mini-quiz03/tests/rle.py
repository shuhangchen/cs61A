test = {
  'name': 'rle',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (rle nil)
          ()
          scm> (define foo (cons-stream 6 (cons-stream 6 (cons-stream 6 nil))))
          foo
          scm> (car (rle foo))
          (6 3)
          scm> (cdr-stream (rle foo))
          ()
          scm> (define s (cons-stream 1 (cons-stream 1 (cons-stream 2 nil))))
          s
          scm> (car (rle s))
          (1 2)
          scm> (car (cdr-stream (rle s)))
          (2 1)
          scm> (cdr-stream (cdr-stream (rle s)))
          ()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (long-stream elem repetitions tail)
          ....   (if (= repetitions 0)
          ....       tail
          ....       (cons-stream elem (long-stream elem (- repetitions 1) tail))))
          long-stream
          scm> (define threes (long-stream 3 1000 nil))
          threes
          scm> (define twos (long-stream 2 1000 threes))
          twos
          scm> (define ones (long-stream 1 1000 twos))
          ones
          scm> (define compressed (rle ones))
          compressed
          scm> (car compressed)
          (1 1000)
          scm> (car (cdr-stream compressed))
          (2 1000)
          scm> (car (cdr-stream (cdr-stream compressed)))
          (3 1000)
          scm> (cdr-stream (cdr-stream (cdr-stream compressed)))
          ()
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'mini-quiz03)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
