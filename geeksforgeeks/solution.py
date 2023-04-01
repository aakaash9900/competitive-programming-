#User function Template for python3

class Solution:
    def minOperations(self, N):
        n=N//2
        res=(n)*(n+1)
        if (N%2!=0):
            return res
        else:
            return res-n
