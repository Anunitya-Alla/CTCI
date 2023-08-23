from collections import defaultdict
from collections import Counter
import unittest
import time
import pdb

def isPermutation_sorted(a: str, b : str) -> bool:

    # TC: O(nlogn) SC : O(c)
    if len(a) != len(b):
        return False
    return sorted(a) == sorted(b)


def isPermutation_Hashmap(a : str, b : str) -> bool:

    # TC:O(n) SC:O(a)

    if len(a) != len(b):
        return False
    
    Hashmap = defaultdict()
    #pdb.set_trace()  # Start debugger here

    for char in a:
        if char in Hashmap:
            Hashmap[char] +=   1
        else: 
            Hashmap[char] = 1
    
    for char in b:
        if char in Hashmap and Hashmap[char] != 0: 
            Hashmap[char] -= 1
            if Hashmap[char] == 0:
                Hashmap.pop(char)
        else :
            return False
            
    return not Hashmap

def isPermutation_counterArray(a : str, b : str) -> bool:

        # TC:O(n) SC:O(a)

    if len(a) != len(b):
        return False
    
    counter = [0] * 128

    for char in a:
        val  = ord(char)
        counter[val] += 1
    
    for char in b:
        val = ord(char)
        if counter[val] == 0 :
            return False
        counter[val] -= 1

    return True

def isPermutation_CounterDS(a : str, b : str) -> bool:

        # TC:O(n) SC:O(a)


    if len(a) != len(b):
        return False

    return Counter(a) == Counter(b) 


class Test(unittest.TestCase):
    # str1, str2, is_permutation
    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    test_functions = [
        isPermutation_sorted,
        isPermutation_Hashmap,
        isPermutation_counterArray,
        isPermutation_CounterDS

    ]

    def test_cp(self):
        # true check
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for a,b, expected in self.test_cases:
                for isPermutation in self.test_functions:
                    start = time.perf_counter()
                    assert (
                        isPermutation(a,b) == expected
                    ), f"{isPermutation.__name__} failed for value: {a}, {b}"
                    function_runtimes[isPermutation.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()