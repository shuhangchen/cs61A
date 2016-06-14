test = {
  'name': 'iterators',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class Sad:
          ...     def __init__(self, green):
          ...         self.green = green
          ...     def __next__(self):
          ...         frog = self.green
          ...         if frog > 50:
          ...             raise StopIteration
          ...         self.green += frog
          ...         return frog
          ...     def __iter__(self):
          ...         self.green *= self.green
          ...         return self
          >>> s = Sad(1)
          >>> next(s)
          1
          >>> next(s)
          2
          >>> s.green
          4
          >>> slst = []
          >>> for i in s:
          ...     slst.append(i)
          >>> slst
          [16, 32]
          >>> s.green
          64
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> class Such:
          ...     def __init__(self, iteration):
          ...         self.iteration = iteration
          ...     def __next__(self):
          ...         if self.iteration == 0:
          ...             raise StopIteration
          ...         self.iteration //= 2
          ...         return self.iteration
          ...     def __iter__(self):
          ...         while self.iteration < 30:
          ...             yield self.iteration
          ...             self.iteration += 10
          >>> s = Such(16)
          >>> next(s)
          8
          >>> next(s)
          4
          >>> slst = []
          >>> for j in s:
          ...    slst.append(j)
          >>> slst
          [4, 14, 24]
          >>> next(s)
          17
          >>> for j in s:
          ...    slst.append(j)
          >>> slst
          [4, 14, 24, 17, 27]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'type': 'wwpp'
    }
  ]
}
