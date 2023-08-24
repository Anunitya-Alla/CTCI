import time, pdb, math
import unittest
from collections import defaultdict

def countEdits(a: str,  b: str) -> bool:

    if a == b: 
        return True
    if abs(len(a) - len(b)) > 1:
        return False
    
    i, j = 0, 0
    edits = False

    short, long = (a,b) if len(a) < len(b) else (b,a)
    #pdb.set_trace()
    while i < len(short) and j < len(long): 
        if short[i] != long[j]:
            if edits:
                return False
            edits = True
            if len(short) == len(long):
                i += 1
        else:
            i += 1
        j += 1


    return True


class Test(unittest.TestCase):
    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),
    ]

    testable_functions = [countEdits]

    def test_one_away(self):

        for f in self.testable_functions:
            num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for a,b, expected in self.test_cases:
                for is_unique_chars in self.testable_functions:
                    start = time.perf_counter()
                    res = is_unique_chars(a,b)
                    assert (
                         res == expected
                    ), f"{is_unique_chars.__name__} failed for value: {a}, {b}, {res}, {expected}"
                    function_runtimes[is_unique_chars.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":

    unittest.main()
    #res =  countEdits("pale","ple")
