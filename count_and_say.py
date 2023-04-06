# Problem: https://leetcode.com/problems/count-and-say/

class Solution:
    def count_and_say(self, n: int) -> str:
        if n == 1:
            return "1"
        say = self.countAndSay(n - 1)

        new_string = ""
        cur = say[0]
        cnt = 0
        for num in say:
            if num == cur:
                cnt += 1
            else:
                new_string += str(cnt) + cur
                cnt = 1
                cur = num
        return new_string + str(cnt) + cur
