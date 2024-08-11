class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        negative = False
        started = False

        for c in s:
            if c == " " and not started:
                continue     
            if c.isdigit():
                ans = ans * 10 + int(c)
                print("negative:", negative, "ans:", ans)
                if negative:
                     if -ans <= -(1<<31):
                        return -(1<<31)
                elif ans >= (1<<31) - 1:
                    return (1<<31) - 1
            elif started:
                break
            elif c == "-":
                negative = True
            elif c == "+":
                negative = False
            else:
                break
            started = True

        if negative:
            ans = -ans
        return ans

            

