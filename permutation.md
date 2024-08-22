순열은 순서를 가짐

```python
import itertools

arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
print(list(nPr))

# 결과 : [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```

조합은 순서가 없음

```python
import itertools

arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr))

# 결과 : [('A', 'B'), ('A', 'C'), ('B', 'C')]
```
