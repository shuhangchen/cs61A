test = {
  'name': 'no-repeats',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (no-repeats '(5 4 5 4 2 2))
          (5 4 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (no-repeats '(5 4 3 2 1))
          (5 4 3 2 1)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (no-repeats '(5 4 3 2 1 1))
          (5 4 3 2 1)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (no-repeats '(5 5 4 3 2 1))
          (5 4 3 2 1)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (no-repeats ())
          ()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (no-repeats '(12))
          (12)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (no-repeats '(1 1 1 1 1 1))
          (1)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw06)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
