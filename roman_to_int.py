class Solution(object):
    def roman_to_int(self, s):
        """
        :type s: str
        :rtype: int
        """
        """Convert from Roman numerals to an integer."""
        values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        numbers = []
        for char in s:
            numbers.append(values[char])
        total = 0
        for num1, num2 in zip(numbers, numbers[1:]):
            if num1 >= num2:
                total += num1
            else:
                total -= num1
        return total + num2

    def roman_to_int2(self, s):
        values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        numbers = []
        for char in s[::-1]:
            numbers.append(values[char])
        total = numbers[0]
        for num1, num2 in zip(numbers, numbers[1:]):
            if num1 <= num2:
                total += num2
            else:
                total -= num2
        return total
