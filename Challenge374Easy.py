'''

python C:/wamp64/www/apps/lilpostloo/DailyProgrammer/Challenge374Easy.py
https://old.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/

 

'''

import time
start = time.time()

def additive_persistence(input,count=0,total=0):
  count+=1
  for x in [int(x) for x in str(input)]:
    total += int(x)
  if total<10:
    return count
  else:
    return additive_persistence(total,count)  

def additive_persistence_small(input,count=0,total=0):
  for x in [int(x) for x in str(input)]:
    total += int(x)
  return count+1 if total<10 else additive_persistence_small(total,count+1)


def additive_persistence_bonus(input,total=0,count=1):
  res = input // 10
  lastDigit = input - res*10
  total+=lastDigit
  #print(lastDigit)
  if res>10:
    return additive_persistence_bonus(res,total,count)
  else:
    total += res
    if total>9:
      return additive_persistence_bonus(total,0,count+1)
    else:
      return count 

 
def additive_persistence_bonus_small(input,total=0,count=1):
  res = input // 10
  lastDigit = input - res*10
  total+=lastDigit
  total2 = total+res
  return additive_persistence_bonus(res,total,count) if res>10 else additive_persistence_bonus(total2,0,count+1) if total2>9 else count
 



 
  



def run(input):
  #print(additive_persistence(input))
  #print(additive_persistence_small(input))
  #print(additive_persistence_bonus(input))
  print(additive_persistence_bonus_small(input))
  
 
run(13)
run(1234)
run(9876)
run(199)




end = time.time()
print('Finished in',end - start,'seconds')