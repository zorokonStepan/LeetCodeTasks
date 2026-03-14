class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        numbers = set()
        numbers.add(n)
        while "1" not in numbers:
            n = str(sum(int(item) ** 2 for item in list(n)))
            if n in numbers:
                return False
            numbers.add(n)

        return True


if __name__ == "__main__":
    assert Solution().isHappy(11) is False
