"""
    Given a string s which represents an expression, evaluate this expression and return its value.

    The integer division should truncate toward zero.

    You may assume that the given expression is always valid. All intermediate results
    will be in the range of [-2**31, 2**31 - 1].

    Note: You are not allowed to use any built-in function which evaluates strings as
    mathematical expressions, such as eval().
"""


class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip().replace(" ", "")

        expression = []
        number = ""
        operators = {"+", "-", "*", "/"}

        for item in s:
            if item in operators:
                if number:
                    expression.append(int(number))
                    number = ""
                expression.append(item)
            else:
                number += item
        expression.append(int(number))

        while "*" in expression or "/" in expression:
            for ind in range(len(expression)):
                if expression[ind] == "*":
                    expression[ind - 1 : ind + 2] = [expression[ind - 1] * expression[ind + 1]]
                    break
                elif expression[ind] == "/":
                    expression[ind - 1 : ind + 2] = [expression[ind - 1] // expression[ind + 1]]
                    break

        while "+" in expression or "-" in expression:
            for ind in range(len(expression)):
                if expression[ind] == "+":
                    expression[ind - 1 : ind + 2] = [expression[ind - 1] + expression[ind + 1]]
                    break
                elif expression[ind] == "-":
                    expression[ind - 1 : ind + 2] = [expression[ind - 1] - expression[ind + 1]]
                    break

        return expression[0]


if __name__ == "__main__":
    assert Solution().calculate(" 3+5 / 2 ") == 5
