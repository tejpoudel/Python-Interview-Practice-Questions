'''
Question 2
Given a string a, find the longest palindromic substring contained in a. Your function
definition should look like question2(a), and return a string.
'''

def question2(a):

    def solution(str, c1, c2):
        l = c1
        r = c2
        n = len(str)
        while ((l >= 0)  & (r <= n-1)):
            if (str[l] == str[r]):
                l-=1
                r+=1
            else:
                break
        return str[l+1:r]

    n = len(a)
    if (n==0): return ""
    longest = a[0]
    for i in range(0, n-1):
        p1 = solution(a, i, i)
        if (len(p1) > len(longest)):
            longest = p1
        p2 = solution(a, i, i+1)
        if (len(p2) > len(longest)):
            longest = p2
    return longest

assert question2('aa') == 'aa'
assert question2('aaaa') == 'aaaa'
assert question2('bananas') == 'anana'

#If Answer is correct
print('Tests passed for question 2')



