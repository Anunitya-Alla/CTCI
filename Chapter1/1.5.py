import time, pdb
import unittest
from collections import defaultdict

def countEdits(a: str,  b: str) -> bool:

    if a == b: 
        return True
    
    arrA = list(a)
    arrB = list(b)

    edits = 0
    i, j  = 0, 0

    while i< len(arrA) and j< len(arrB):
        #pdb.set_trace()

        if arrA[i] != arrB[j]:
            if edits != 0 :
                return False 
            edits += 1
            if i+1 < len(arrA) and j+1 < len(arrB) and arrA[i+1] == arrB[j+1] :
                i += 1
                j += 1
            elif j+1 < len(arrB) and arrA[i] == arrB[j+1] : 
                j += 1 
            elif   i+1 < len(arrA) and arrA[i+1] == arrB[j] : 
                i +=1
            else : 
                i += 1
                j += 1
               
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
                    assert (
                        is_unique_chars(a,b) == expected
                    ), f"{is_unique_chars.__name__} failed for value: {a}, {b}"
                    function_runtimes[is_unique_chars.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":

    unittest.main()
     #res =  countEdits("A","b")
