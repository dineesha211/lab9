import numpy as np
def circular_convolution(x1,x2):
    N=len(x1)
    y=np.zeros(N)
    for n in range(N):
        y[n] = sum(x1[m]*x2[(n-m)% N] for m in range(N))
    return y
x=[1,2,3,1,2,3,1,2,3,1,2,3]
h=[1,-1,1]
L=4
M=len(h)
l=len(x)
X=[]
for i in range(0,L):
   h.append(0)
for i in range(0,l,L):
   a=x[i:i+L]
   X.append(a)
X1=[]
for i in range(0,M):
      for j in range(L+M-2,M,-1):
          if(i==0):
                X[i].insert(0,0)
          else:
                 X[i].insert(0,X[i-1][j])
      F1=list(circular_convolution(X[i],h))
      X1.append(F1)
print(X1)
A=[]
for i in range(0,M):
      a=X1[i][M-1:]
      A.extend(a)
print(A)
