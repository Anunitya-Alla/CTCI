from collections import defaultdict
import unittest, time, pdb
def stringCompress_algo(a: str) -> str:

    #Tc: Sc: O(n)

    if len(a) < 3 : return a # Would not compress te string

    #pdb.set_trace()
    lastSeen = a[0]
    count = 1
    res = []
    for i in range(1,len(a)):

        if len(res) > len(a) : return a

        if a[i] == lastSeen:
            count += 1
        else:
            res.append(lastSeen + str(count) )
            lastSeen = a[i]
            count = 1
    
    res.append(lastSeen + str(count))
   
    res = "".join(res)
    return min(a, res, key=len)

class Test(unittest.TestCase):
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]
    test_functions = [
        stringCompress_algo,
    ]

    def test_stringCompress(self):
            num_runs = 1000
            function_runtimes = defaultdict(float)

            for _ in range(num_runs):
                for text, expected in self.test_cases:
                    for str_comp in self.test_functions:
                        start = time.perf_counter()
                        assert (
                            str_comp(text) == expected
                        ), f"{str_comp.__name__} failed for value: {text}"
                        function_runtimes[str_comp.__name__] += (
                            time.perf_counter() - start
                        ) * 1000

            print(f"\n{num_runs} runs")
            for function_name, runtime in function_runtimes.items():
                print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()
