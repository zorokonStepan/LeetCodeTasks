"""
    Given an integer n, return the number of prime numbers that are strictly less than n.
"""
from utils.utils import timer


class Solution:
    def __init__(self):
        self.prime_numbers = []

    @timer
    def countPrimes(self, n: int) -> int:
        count_primes = 0
        for num in range(n):
            if self.is_prime(num):
                count_primes += 1
        return count_primes

    def is_prime(self, num: int) -> bool:
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False

        if self.prime_numbers:
            divisors = self.prime_numbers + list(
                range(self.prime_numbers[-1], int(num**0.5) + 1, 2)
            )
        else:
            divisors = range(int(num**0.5) + 1, 2)

        for divisor in divisors:
            if num % divisor == 0:
                return False

        self.prime_numbers.append(num)
        return True


if __name__ == "__main__":
    assert Solution().countPrimes(4) == 2
    assert Solution().countPrimes(10) == 4
    assert Solution().countPrimes(499979) == 41537  # 63.48615789413452
    assert Solution().countPrimes(5_000_000) == 348_513  #
