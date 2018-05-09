class Solution:
        def shortestToChar(self, S, C):
                StrLen = len(S)
                key = S.find(C)
                output=[]
                #print(key)
                for i, c in enumerate(S):
                        #print(i)
                        if C==c:
                                key = i
                                output.append(0)
                        else:
                                output.append(abs(key-i))
                for i in range(StrLen-1, 0, -1):
                        if output[i] == 0:
                                key = i
                        else:
                                diff = abs(key-i)
                                if diff < output[i]:
                                        output[i] = diff

                print(*output)

def main():
        foo = Solution()
        S = "loveleetcode"
        C = 'e'
        foo.shortestToChar(S, C)

if __name__ == "__main__":
        main()