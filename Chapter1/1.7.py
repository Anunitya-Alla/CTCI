from collections import defaultdict
import time, pdb, unittest

def rotateMatrix_python(a) : 
    a = zip(*a)
    a = [list(reversed(row)) for row in a]
    return a


class Test(unittest.TestCase):
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]
     
    test_functions = [rotateMatrix_python]

    def test_rotateMatrix(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for rotateMatrix in self.test_functions:
                    start = time.perf_counter()
                    res =  rotateMatrix(text) 
                    assert (
                        res == expected
                    ), f"{rotateMatrix.__name__} failed for value: {text}, {res}, {expected}"
                    function_runtimes[rotateMatrix.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()