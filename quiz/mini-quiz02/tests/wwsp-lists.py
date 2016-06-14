test = {
  'name': 'What Would Scheme Print?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': '(() 1 . 2)',
          'choices': [
            '(() (1 . 2))',
            '(() 1 . 2)',
            '(() 1)',
            '(() . 1)',
            '((1 . 2) . 1)',
            'Error'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          scm> (define lst (list () '(1 . 2) '(1 2 . (3))))
          lst
          scm> (cons (car lst) (car (cdr lst)))
          _______
          """
        },
        {
          'answer': '(2)',
          'choices': [
            '(2)',
            '((2))',
            '(2 3)',
            '((2 3))',
            '((2 3 1) . 2)',
            '(1 1 . 2)',
            'Error'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          scm> (cons (cdr (car (cdr lst))) (car lst))
          _______
          """
        },
        {
          'answer': '(() ((1 . 2) (1 2 3)))',
          'choices': [
            '(((1 . 2) (1 2 3)))',
            '(() ((1 . 2) (1 2 3)))',
            '((1 . 2) (1 2 3))',
            'Error'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          scm> (list (car lst) (cdr lst))
          _______
          """
        },
        {
          'answer': '((1 . 2) (1 2 3))',
          'choices': [
            '(((1 . 2) (1 2 3)))',
            '(() ((1 . 2) (1 2 3)))',
            '((1 . 2) (1 2 3))',
            'Error'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          scm> (append (car lst) (cdr lst))
          _______
          """
        },
        {
          'answer': '(((1 . 2) (1 2 3)))',
          'choices': [
            '(((1 . 2) (1 2 3)))',
            '(() ((1 . 2) (1 2 3)))',
            '((1 . 2) (1 2 3))',
            'Error'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          scm> (cons (cdr lst) (car lst))
          _______
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
