"""
    Given an integer n, return the number of prime numbers that are strictly less than n.
"""
from utils.utils import timer


class Solution:
    @timer
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        p = 2
        while p * p < n:
            if is_prime[p]:
                for multiple in range(p * p, n, p):
                    is_prime[multiple] = False
            p += 1

        return sum(is_prime)


if __name__ == "__main__":
    assert Solution().countPrimes(4) == 2
    assert Solution().countPrimes(10) == 4
    assert Solution().countPrimes(499979) == 41537  # 0.032638
    assert Solution().countPrimes(5_000_000) == 348_513  # 0.364623
