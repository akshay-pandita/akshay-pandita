class Solution(object):
    def reverse(self, x):
        max_num = 1
        for _ in range(31):
            max_num = max_num * 2

        tmp_lst = []
        is_negative = False
        if x < 0:
            is_negative = True
            x = x * -1
        while x > 0:
            digit = x%10
            tmp_lst.append(int(digit))
            x = int(x/10)
        reversed_num = 0
        num_count = 0
        start = True
        while num_count < len(tmp_lst):
            if tmp_lst[num_count] == 0 and start:
                num_count = num_count + 1
                continue
            start = False
            reversed_num = reversed_num + tmp_lst[num_count]
            # print (reversed_num)
            # print (max_num)
            if reversed_num > max_num:
                return 0
            if num_count != len(tmp_lst) - 1:

                reversed_num = reversed_num * 10
                if reversed_num > max_num:
                    return 0
            num_count = num_count + 1
        if is_negative:
            reversed_num = reversed_num * -1
        return reversed_num

soln=Solution()
print (soln.reverse(1563847412))

