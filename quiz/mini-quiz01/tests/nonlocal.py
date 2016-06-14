test = {
  'name': 'Nonlocal',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> y = 4
          >>> def foo(x):
          ...     def bar():
          ...         nonlocal x, y
          ...         x = x + y
          ...         return x
          ...     return bar
          >>> # Remember for all WWPP questions, enter Error if it errors.
          >>> foo(3)()
          Error
          >>> def foo(x):
          ...     def bar(y):
          ...         nonlocal x, y
          ...         x = x + y
          ...         return x
          ...     return bar
          >>> foo(3)(4)
          Error
          >>> def foo(x):
          ...     def bar(y):
          ...         nonlocal x
          ...         x = x + y
          ...         return x
          ...     return bar
          >>> foo(3)(4)
          7
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
