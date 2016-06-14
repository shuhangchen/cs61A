test = {
  'name': 'above_average',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select * from above_average order by height;
          28|grover
          35|eisenhower
          47|clinton
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read hw08.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
