class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ugly = []
        beauty = []
        ans = [0]
        temp = 0
        for i in range(len(s)):
            if s[i] == '(':
                temp += 1
            else:
                if temp >= 1:
                    temp -= 1
                    if ugly == [] or ugly[-1][1] < temp:
                        ugly.append((2,temp))
                    else:
                        ugly.append((ugly[-1][0]+2, temp-1))
                    if temp == 0:
                        if beauty:
                            beauty.append(beauty[-1]+ugly[-1][0])
                        else:
                            beauty.append(ugly[-1][0])
                        ugly[-1] = (beauty[-1], 0)
                else:
                    beauty.clear()
                    ugly.sort(reverse=True)
                    if ugly != []:
                        ans.append(ugly[0][0])
                    ugly.clear()
                    temp = 0
        ugly.sort(reverse = True)
        if ugly != []:
            ans.append(ugly[0][0])
        return max(ans)

sol = Solution()
print(sol.longestValidParentheses(")()())"))