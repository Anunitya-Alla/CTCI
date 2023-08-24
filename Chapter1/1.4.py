from collections import defaultdict
import math
import unittest, pdb, time
def isPermutation_count(a : str) -> bool:

    #TC: O(n) SC:O(n)

    charList = [char.lower() for char in a if char.isalpha() ]
    n = len(charList)
 
    counter = defaultdict()

    for i in range(len(charList)): 
        #pdb.set_trace()
        if charList[i] in counter:
            counter[charList[i]] += 1
        else: 
            counter[charList[i]] = 1

    # odd, even = 0, 0
    # for char,count in counter.items():

    #     if count %2 == 0: 
    #         even += 1
    #     else: 
    #         odd += 1
    #         if odd > 1 :
    #             return False

    return sum(val%2 for val in counter.values()) < 2


class Test(unittest.TestCase):
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("a-bba!", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]
    test_functions = [
        
        isPermutation_count,
    ]

    def test_pal_perm(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for isperm in self.test_functions:
                    start = time.perf_counter()
                    assert (
                        isperm(text) == expected
                    ), f"{isperm.__name__} failed for value: {text}"
                    function_runtimes[isperm.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()
