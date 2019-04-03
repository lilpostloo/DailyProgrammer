# python C:\wamp64\www\apps\lilpostloo\Challenge375Intermediate\run.py


'''

values: 0 = face down, 1 = face up, 2 = removed
algorithm:
  loop through the sequence 
    remove 1st faced-up card from left and flipAdjacentCards
    repeat until all cards removed or no more changes(ie 'no solution')



'''

import time
import copy
start = time.time()

ans = []

def flipAdjacentCards(j,arrClone):

  if j<len(arrClone) and j>-1:
    arrClone[j] = abs(arrClone[j]+-1) if arrClone[j] !=2 else 2

  return arrClone

def removeCard(arr,ans):
  arrClone = copy.deepcopy(arr)
  for i,x in enumerate(arr):
    if x == 1:
      arrClone[i] = 2
      ans.append(i)
      arrClone = flipAdjacentCards(i+1,arrClone)
      arrClone = flipAdjacentCards(i-1,arrClone)
      break

  return arrClone,ans

def run(input):
  ans = []
  arr = [int(x) for x in input]
  while sum(arr) != len(arr)*2:
    #print(arr)
    arr2,ans = removeCard(arr,ans)
    if arr2 == arr:
      #print(arr)
      ans = ['no solution']
      break
    else:
      arr = arr2


  #print(arr)
  print('solution:',ans)
  #print('end\n')

run('0100110')
run('01001100111')
run('001011011101001001000')
run('1010010101001011011001011101111')
run('1101110110000001010111011100110')
run('010111111111100100101000100110111000101111001001011011000011000')
 
end = time.time()
print('Finished in',end - start,'seconds')