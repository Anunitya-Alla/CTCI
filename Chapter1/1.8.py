import unittest
import time, pdb
from collections import defaultdict

def zeroMatrix_algo(a ):

    zeroRow = set()
    zeroCol = set()
    #pdb.set_trace()
    for i in range(len(a)):
        
        row = a[i]
        if 0 in row:
            zeroRow.add(i)
            zeroCol.add(a[i].index(0))
    
    for row in zeroRow:
        a[row] = [0] * len(a)

    for col in zeroCol:
        for i in range(len(a[0])):
            a[i][col] = 0
    return a

class Test(unittest.TestCase):
    test_cases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]
    test_functions = [zeroMatrix_algo]

    def test_is_zeroMatrix(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for zeroMatrix in self.test_functions:
                    start = time.perf_counter()
                    res = zeroMatrix(text)
                    print(text)
                    assert (
                        res == expected
                    ), f"{zeroMatrix.__name__} failed for value: {expected}"
                    function_runtimes[zeroMatrix.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()
  