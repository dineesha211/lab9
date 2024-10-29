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
n=L-1
o=M-1
for i in range(n):
   h.append(0)
print("h=",h)
k=[]
for i in range(0,len(x),L):
	k.append(x[i:i+L])
print(k)
for i in range(len(k)):
	for j in range(o):
		k[i].append(0)
print(k)
y=[]
for i in range (len(k)):
  y.append(list(circular_convolution(k[i],h)))
print(y)
output = y[0][:]
for i in range(1,len(y)):
       o_l=o
       for j in range(o_l):
          output[-(o_l - j)] += y[i][j]
       output.extend(y[i][o_l:])
print("Y:",output[:-2])

'''x1=[1,2,3,1]
x2=[2,3,1,2]
x3=[3,1,2,3]
for i in range(o):
   x1.append(0)
   x2.append(0)
   x3.append(0)
print("x1=",x1)
print("x2=",x2)
print("x3=",x3)
y1=circular_convolution(x1,h)
print("y1=",y1)
y2=circular_convolution(x2,h)
print("y2=",y2)
y3=circular_convolution(x3,h)
print("y3=",y3)'''

