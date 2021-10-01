class Solution:
    def isPalindrome( self, x: int) -> bool:
        n_str = str(x)
        r_str = n_str[::-1]
        if n_str == r_str:
            return True
        else:
            False
