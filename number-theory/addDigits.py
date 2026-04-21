class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num1 = num//10
            num2 = num % 10
            num = num1 + num2
        return num
