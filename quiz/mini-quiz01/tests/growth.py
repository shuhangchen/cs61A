test = {
  'name': 'Memoization',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'O(n)',
          'choices': [
            'O(1)',
            'O(log(n))',
            'O(n)',
            'O(n^2)'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          def factorial(n):
            if n <= 1:
              return 1
            return n * factorial(n - 1)
          
          What is the order of growth in big-O notation of factorial(n)?
          """
        },
        {
          'answer': '10',
          'choices': [
            '1',
            '2',
            '10',
            '100'
          ],
          'hidden': False,
          'locked': False,
          'question': 'How many total calls to factorial are made if we call factorial(10)?'
        },
        {
          'answer': '100000',
          'choices': [
            '1',
            '2',
            '100000',
            '10000000000'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          memo_dict = {}
          def factorial_memo(n):
            if n <= 1:
              return 1
            if n not in memo_dict:
              memo_dict[n] = n * factorial_memo(n - 1)
            return memo_dict[n]
          
          How many total calls to factorial_memo are made if we call factorial_memo(100000)?
          """
        },
        {
          'answer': '2',
          'choices': [
            '1',
            '2',
            '100000',
            '10000000000'
          ],
          'hidden': False,
          'locked': False,
          'question': 'How many total calls to factorial_memo are made if we then call factorial_memo(100001)?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
