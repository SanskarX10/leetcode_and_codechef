"Given a roman numeral, convert it to an integer."



class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        val_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        val_list = list(s)
        for i in range(len(val_list) - 1):
            x = val_dic.get(val_list[i])
            y = val_dic.get(val_list[i + 1])
            if x < y:
                sum += (-1 * x)
            else:
                sum += x
        sum += val_dic.get(val_list[-1])
        return sum
        
