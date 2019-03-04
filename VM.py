from math import *

class VM:
    def __init__(self):
        self.__o__ = 0 
        self.__resphi__ = 2 - ((1+ sqrt(5)) / 2)
    def __f__(self, x):
        return cos(x)
    def GoldenRatio(self, l, r, eps):
        x1 = l + self.__resphi__ * (r - l)
        x2 = r - self.__resphi__ * (r - l)
        f1 = self.__f__(x1)
        f2 = self.__f__(x2)
        while abs(r - l) > eps:
            if f1 < f2:
                r = x2
                x2 = x1
                f2 = f1
                x1 = l + self.__resphi__ * (r - l)
                f1 = self.__f__(x1)
            else:
                l = x1
                x1 = x2
                f1 = f2
                x2 = r - self.__resphi__ * (r - l)
                f2 = self.__f__(x2)
            self.__o__ += 1
            print(x1,x2,self.__o__)
        return(x1 + x2) /2
    def Rukzak(self, W, N, w):
        A = [[0]*W for i in range(N)]
        #print(A)
        for i in range(1, N):
            for j in range(1, W):
                if j >= w[i]:
                    A[i][j] = max(A[i - 1][j], A[i - 1][j - w[i]] + w[i])
                else:
                    A[i][j] = A[i - 1][j]
        return A#[N-1][W-1]
    


#a = VM()
#print(a.GoldenRatio(0,6.28,0.1))
#print(a.Rukzak(10,7,[1,4,8,9,6,4,10]))
