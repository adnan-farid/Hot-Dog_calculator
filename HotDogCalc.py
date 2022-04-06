#define constants and inputs
import math
numPpl = int(input('Enter the number of people attending your cookout: '))
numHDgiven = int(input('Enter the number of hotdogs each person will get at your cookout: '))
numBuns = 10
numHD = 8
#Use normal division here, will round up later 
numHDn = ((numPpl * numHDgiven)/ numHD)
numBN = ((numPpl * numHDgiven)/numBuns)
#Modulo is used to acquire the remainders of the operation
numHDleftover = numPpl * numHDgiven % numHD
numBleftover = numPpl * numHDgiven % numBuns

#math.ceiling is used to round up
print('You will need at least ' + str(math.ceil(numHDn)) + ' hot dog packages.')
print('You will need at least ' + str(math.ceil(numBN)) + ' packages of hot dog buns.')
#if/elif statements used to correct grammar in case their is none of either item left
if numHDleftover != 0:
   print('You will have at least ' + str(numHDleftover) + ' hot dogs left over.')
elif numHDleftover == 0:
   print("You will have no hot dogs left over if you don't purchase extra.")
if numBleftover != 0:
   print('You will have at least ' + str(numBleftover) + ' hotdog buns left over.')
elif numBleftover == 0:
    print("You will have no hot dog buns left over if you don't purchase extra.")
