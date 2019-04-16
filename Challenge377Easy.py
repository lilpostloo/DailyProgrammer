'''

python C:/wamp64/www/apps/lilpostloo/DailyProgrammer/Challenge377Easy.py
https://old.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/
 

'''
import math

def fit1(X,Y,x,y):
    i=math.floor(X/x)
    j=math.floor(Y/y)
    print(str(i*j))


fit1(25, 18, 6, 5)
fit1(10, 10, 1, 1)
fit1(12, 34, 5, 6)
fit1(12345, 678910, 1112, 1314) 
fit1(5, 100, 6, 1) 

def fit2(X,Y,x,y):
    i=math.floor(X/x)*math.floor(Y/y)
    j=math.floor(X/y)*math.floor(Y/x)
    ans = i if i>j else j
    print(ans)

print('\n')
fit2(25, 18, 6, 5)
fit2(12, 34, 5, 6)
fit2(12345, 678910, 1112, 1314)
fit2(5, 5, 3, 2)
fit2(5, 100, 6, 1)
fit2(5, 5, 6, 1)