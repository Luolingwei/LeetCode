class Solution:
    def PhoneFind (self,N,K):
        # C=[[0]*(N+1) for _ in range(N+1)]
        # for j in range(1,N+1):
        #     C[1][j]=j*(j+1)/2
        T=[[float('inf')]*(K+1) for _ in range(N+1)]
        L=[[[] for _ in range(K+1)] for _ in range(N+1)]
        for j in range(1,N+1):
            T[j][1]=C[1][j]
            L[j][1]+=[''.join(str(digit) for digit in range(1,j+1))]
        for i in range(1,N+1):
            for j in range(1,K+1):
                for l in range(1,i):
                    if T[l][j-1]+C[l+1][i]<T[i][j]:
                        T[i][j]=T[l][j-1]+C[l+1][i]
                        L[i][j]=L[l][j-1]+[''.join(str(digit) for digit in range(l+1,i+1))]
        return T[N][K],L[N][K]

a=Solution()
print(a.PhoneFind(4,2))