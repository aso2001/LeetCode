class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        res = []
        for i in range(n):
            if not (i + 1)%3 and not (i + 1)%5:
                res.append('FizzBuzz')
            elif not (i + 1)%3:
                res.append('Fizz')
            elif not (i + 1)%5:
                res.append('Buzz')
            else:
                res.append(str(i+1))
        return res