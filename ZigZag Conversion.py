class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        if numRows == 1 or numRows > n: 
            return s 
        
        interval = numRows*2 - 2
        output = s[0::interval]   
        
        for i in range(1, numRows-1):
            p, q = i, i + interval - i*2 
            
            while p < n:
                output += s[p]
                p += interval
                
                if q < n:
                    output += s[q]
                    q += interval 
    
        return output + s[numRows-1::interval]
