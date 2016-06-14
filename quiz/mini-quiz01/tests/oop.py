test = {
  'name': 'OOP/Inheritance',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class A(object):
          ...   x, y = 0, 0
          >>> class B(A):
          ...   pass
          >>> class C(A):
          ...   pass
          >>> print(A.x, B.x, C.x)
          0 0 0
          >>> B.x = 2
          >>> print(A.x, B.x, C.x)
          0 2 0
          >>> A.x += 1
          >>> print(A.x, B.x, C.x)
          1 2 1
          >>> obj = C()
          >>> obj.y = 1
          >>> C.y == obj.y
          False
          >>> A.y = obj.y
          >>> print(A.y, B.y, C.y, obj.y)
          1 1 1 1
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
