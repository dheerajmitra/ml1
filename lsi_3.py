import numpy as np
import random
from numpy import linalg as LA
import math
from numpy.linalg import inv
from numpy import diag
r9=int(input("enter the no. of document"))
to=[]
d=[]
for i in range(r9):
    ki=i+1
    to.append(input("enter the document:"))
for i in range(r9):
    d.append(to[i].split())

a1=[]

q=input("please enter the query")
#making query array
a4=q.split()

#making A matrix
for k9 in range(r9):       
    c=1
    for i in range(len(d[k9])):
        for j in range(len(a1)):
            if d[k9][i]==a1[j]:
                c=0
        if c==0:
            c=1
        else:
            a1.append(d[k9][i])



#sorted the A matrix in increasing order of alphabets
a1=np.sort(a1)
print(a1)
#making of A matrix from d1,d2,d3
print(d[0][1])
da=[]
for k in range(r9):
    da.append([])

for k in range(r9):
    f3=d[k]
    for i in range(len(a1)):
         dr=0
         for j in range(len(f3)):
             if d[k][j]==a1[i]:
                  dr+=1
         da[k].append(dr)
   

    
#print(da) #matrix from by d1,d2.d3 is A



q1=[]
for i in range(len(a1)):
     t=0
     for j in range(len(a4)):
       if a4[j]==a1[i]:
            t+=1
     q1.append(t)


#singular value decomposition start
x1=np.array(da)
x2=np.transpose(x1)
print(x1)
print(x2)
print(q1)

x3=np.matmul(x1,x2)#this is array AA^t

#finding Eigen value
v = LA.eig(x3)
eval=v[0]#this is eigen values
evact=v[1]#this is eigen vector
print(evact)

#finding Singular matrix
s=[]
for k in range(r9):
 s.append(math.sqrt(eval[k]))

e1=[]
#for k in range(r9):
e1= diag(s)
    

sing=np.array(e1)#this is singular matrix
#print(sing)
#findig inverse of singular matrix
singI=inv(sing)
print(singI)

#finding eigen matrix and eigen 
evact1=np.array(evact)
#print(evact1)
evactT=np.transpose(evact1)
#print(evactT)


#finding matrix U and it transpose
u1=np.matmul(x2,evact1)
u=np.matmul(u1,singI)
#print(u)
u2=np.transpose(u)
#print(u2[0])
u3=np.array(u2)
#back to lsi example
#finding Uk,Sk,Vk,V^tk
#a0=int(input("enter the ranko f apporximation")
rk=r9-1
       
uk1=np.delete(u3, rk, 0)

uk=np.transpose(np.array(uk1))
#print(uk)
#print(sing[0][0])
singu=np.delete(sing, rk, 0)

singk=np.delete(singu, rk, 1)
singk1=np.array(singk)
singki=inv(singk1)

vo=np.delete(evactT, rk, 0)
va=np.array(vo)
vt=np.transpose(va)
#print(q1)
print(vt)

#finding Q transpose
q2=np.array(q1)
qt=np.transpose(q2)
print(qt)

#finding final q matrix
Q=np.matmul(qt,uk)
Q1=np.matmul(Q,singki)
print(Q1)


#finding sinm(q,d) for different d1,d2,d3 statements
def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return math.sqrt(dotproduct(v, v))

def sin(v1, v2):
  return (dotproduct(v1, v2) / (length(v1) * length(v2)))
df=[]
for i in range(r9):
    df.append(sin(Q1,vt[i]))
    print(df[i])


#sorting the satements in ascending order
df1=sorted(df,reverse=True)
print("ranking are done in this way:")
for j in range(len(df1)):
    for i in range(len(df)):
        if df1[j]==df[i]:
            print(to[i])
      
