"""
Created on Tue Jun 25 08:08:29 2024

@author: AKISH KUJUR
"""
def getsum(n):
    List=[]
    for i in range(n):
        if i%3 == 0 or i%5 == 0:
            List.append(i)
    print(List)
    print(sum(List))

n=int(input("Enter the Number::"))
getsum(n)