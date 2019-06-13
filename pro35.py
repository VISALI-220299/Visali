import sys,string
def cfreq(s) :
    dic4 = {}
    for c in s :
        dic4[c] = dic4.get(c,0) + 1
    return dic4

s = input()
n = len(s)
dic4 = cfreq(s)
Lk = list(dic4.keys())
#print(dic4,Lk)

for j in range(n-2,-1,-1) :
    #print('len = ', j+1)
    for c in Lk :
        k = 0
        for i in range(0,n-j) :
            li, ri = i,j+i
            s2 = s[li:ri + 1]
            #print(c,s2)
            if c in s2 :
                k += 1
        if k == n-j :
            #print('c,k',c,k)
            c2 = c
            k2 = k
            len2 = j+1
print(len2)
