def count(args):
    summa = 0
    for i in args:
        if isinstance(i, list):
            summa += count(i)
        elif isinstance(i, tuple):
            summa += count(i)
        elif isinstance(i, set):
            summa += count(i)
        elif isinstance(i, dict):
            k, v = i.keys(), i.values()
            summa += count(k)
            summa += count(v)
        elif isinstance(i, int):
            summa += i
        elif isinstance(i, str):
            summa += len(i)
    return summa
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = count(data_structure)
print(result)