import unittest, time, pdb
from collections import defaultdict

def Urlify_Replace(a : str, n: int) -> str:

    #Tc: Sc: O(1)
    return a[:int(n)].replace(" ", "%20")


def urlify_algo(string, n):

    charList = list(string)
    newindex = len(charList)

    for i in reversed(range(n)):
        if string[i] == " ":
            charList[newindex-3:newindex] = "%20"
            newindex -= 3
        else:

            charList[newindex-1] = charList[i]
            newindex -= 1



    return "".join(charList[newindex:]) 

class Test(unittest.TestCase):
    """Test Cases"""

    test_cases = {
        ("much ado about nothing      ", 22): "much%20ado%20about%20nothing",
        ("Mr John Smith       ", 13): "Mr%20John%20Smith",
        (" a b    ", 4): "%20a%20b",
        (" a b       ", 5): "%20a%20b%20",
    }
    test_functions = [Urlify_Replace, urlify_algo]

    def test_is_unique_chars(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases.items():
                for urlify in self.test_functions:
                    start = time.perf_counter()
                    assert (
                        urlify(*text) == expected
                    ), f"{urlify.__name__} failed for value: {text[0]}"
                    function_runtimes[urlify.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")

if __name__ == "__main__":
    unittest.main()
