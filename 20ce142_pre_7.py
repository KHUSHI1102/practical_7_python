'''NAME : khushi tala
   ID   : 20Ce142
'''
T = int(input())                     #take number of test cases from user
for i in range(T):  
    n = input()                      #take string from user
    l = len(n)                       #length of n
    if l % 2 == 0:                   #check whether length divisible by two or not
        b, c = n[:l//2], n[l//2:]    #slicing
    else:
        b, c = n[:l//2], n[l//2+1:]  #slicing
    if sorted(b) == sorted(c):       #compare two sorted string
        print("YES")
    else:
        print("NO")
