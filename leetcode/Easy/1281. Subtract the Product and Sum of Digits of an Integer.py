
"Given an integer number n, return the difference between the product of its digits and the sum of its digits."



class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add, mul = 0, 1
        while n>0:
            temp_a = n % 10
            add += temp_a
            mul *= temp_a
            n //= 10
        return mul - add
        
        
