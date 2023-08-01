class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def combinations(iterable, r):
                pool = tuple(iterable)
                n = len(pool)
                if r > n:
                    return
                indices = list(range(r))
                yield tuple(pool[i] for i in indices)
                while True:
                    for i in reversed(range(r)):
                        if indices[i] != i + n - r:
                            break
                    else:
                        return
                    indices[i] += 1
                    for j in range(i+1, r):
                        indices[j] = indices[j-1] + 1
                    yield tuple(pool[i] for i in indices)
        my_list = list(range(1,n+1))
        result = combinations(my_list,k)
        return result
