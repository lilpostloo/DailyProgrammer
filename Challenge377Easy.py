'''

python C:/wamp64/www/apps/lilpostloo/DailyProgrammer/Challenge377Easy.py
https://old.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/
 

'''
from itertools import permutations
from functools import reduce

def fit1(X,Y,x,y):
    i=X//x
    j=Y//y
    print(i*j)

def fit2(X,Y,x,y):
    i=X//x*Y//y
    j=X//y*Y//x
    ans = i if i>j else j
    print(ans)


def fit3(X,Y,Z,x,y,z):
    list1 = [x,y,z]
    ans = 0  
    for i,a in enumerate(list1):
        for j,b in enumerate(list1):
            for k,c in enumerate(list1):
                if j!=k and k!=i and j!=i:
                    tempAns=X//a*Y//b*Z//c
                    ans = tempAns if tempAns>ans else ans
    print(ans)

def fit3_v2(X,Y,Z,x,y,z):
    print(max(list(map(lambda a:X//a[0]*Y//a[1]*Z//a[2],list(permutations([x,y,z]))))))

def fitn(dims,sides):
    ansList = []
    for i, dim in enumerate(dims):
        for j,side in enumerate(sides):
            ansList.append([dim//side,i,j])

    maxAns = 0
    for i, value1 in enumerate(ansList):
        ans = value1[0]
        usedDim = [value1[1]]
        usedSide = [value1[2]]
        for j, value2 in enumerate(ansList):
            if i!=j and value2[1] not in usedDim and value2[2] not in usedSide:
                ans *= value2[0]
                usedDim.append(value2[1])
                usedSide.append(value2[2])
        
        maxAns = ans if ans>maxAns else maxAns

    print(maxAns)

def fitn_v2(dims,sides):
    ansList = [[y[1]//x[1],y[0],x[0]]for y in enumerate(dims) for x in enumerate(sides)]
    maxAns = 0
    for i, value1 in enumerate(ansList):
        ans = value1[0]
        usedDim = [value1[1]]
        usedSide = [value1[2]]
        for j, value2 in enumerate(ansList):
            if i!=j and value2[1] not in usedDim and value2[2] not in usedSide:
                ans *= value2[0]
                usedDim.append(value2[1])
                usedSide.append(value2[2])
        
        maxAns = ans if ans>maxAns else maxAns

    print(maxAns)

fit1(25, 18, 6, 5)
fit1(10, 10, 1, 1)
fit1(12, 34, 5, 6)
fit1(12345, 678910, 1112, 1314) 
fit1(5, 100, 6, 1) 

print('\n')

fit2(25, 18, 6, 5)
fit2(12, 34, 5, 6)
fit2(12345, 678910, 1112, 1314)
fit2(5, 5, 3, 2)
fit2(5, 100, 6, 1)
fit2(5, 5, 6, 1)

print('\n')

fit3(10, 10, 10, 1, 1, 1)
fit3(12, 34, 56, 7, 8, 9)
fit3(123, 456, 789, 10, 11, 12)
fit3(1234567, 89101112, 13141516, 171819, 202122, 232425)

print('\n')

fitn([3, 4], [1, 2])
fitn([123, 456, 789], [10, 11, 12])
fitn([123, 456, 789, 1011, 1213, 1415], [16, 17, 18, 19, 20, 21])
print('\n')


fit3_v2(10, 10, 10, 1, 1, 1)
fit3_v2(12, 34, 56, 7, 8, 9)
fit3_v2(123, 456, 789, 10, 11, 12)
fit3_v2(1234567, 89101112, 13141516, 171819, 202122, 232425)


print('\n')

fitn_v2([3, 4], [1, 2])
fitn_v2([123, 456, 789], [10, 11, 12])
fitn([123, 456, 789, 1011, 1213, 1415], [16, 17, 18, 19, 20, 21])
