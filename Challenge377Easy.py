'''

python C:/wamp64/www/apps/lilpostloo/DailyProgrammer/Challenge377Easy.py
https://old.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/
 

'''
import math

def fit1(X,Y,x,y):
    i=math.floor(X/x)
    j=math.floor(Y/y)
    print(str(i*j))

def fit2(X,Y,x,y):
    i=math.floor(X/x)*math.floor(Y/y)
    j=math.floor(X/y)*math.floor(Y/x)
    ans = i if i>j else j
    print(ans)


def fit3(X,Y,Z,x,y,z):
    list1 = [x,y,z]
    ans = 0  
    for i,a in enumerate(list1):
        for j,b in enumerate(list1):
            for k,c in enumerate(list1):
                if j!=k and k!=i and j!=i:
                    tempAns=math.floor(X/a)*math.floor(Y/b)*math.floor(Z/c)
                    ans = tempAns if tempAns>ans else ans
    print(ans)
 



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