
myList = [29,24,25,26,27]

# WAP to add 50 and 60 to List1
myList.extend([50,60])
print('Extending list:',myList)

# WAP to remove 24 and 27 from List1.
myList.remove(24)
myList.remove(27)
print('After Removing list:',myList)

# WAP to sort List1 in ascending order.
myList.sort()
print('Sorted list:',myList)

# WAP to sort List1 in descending order
myList.sort(reverse=True)
print('Descending Sorted list:',myList)

#  WAP to search for 25 in List1.
index= myList.index(25)
print('Index of 25 in list:',index)

#  WAP to count the number of elements present in List1.
NumOfElement=len(myList)
print("No of element in list':'",NumOfElement)

#  WAP to sum all the elements in List1.
total= sum(myList)
print("sum of all elements in list':'",total)


# WAP to sum all ODD numbers in List1.
# WAP to sum all EVEN numbers in List1.

odd_sum=0
even_sum=0
for j in range(NumOfElement):
    if(myList[j]%2==0):
        even_sum=even_sum+myList[j]
    else:
        odd_sum=odd_sum+myList[j]
print("Even sum:",even_sum)
print("Odd sum:",odd_sum)

#  WAP to sum all PRIME numbers in List1.
def sumprime(list):
    sum =0
    flag =1
    for i in range(len(list)):
        num = list[i]
        for j in range(2, num):
            if list[i]%j ==0:
                flag = 0
                break
            else:
                flag = 1
        if num ==2:
            flag =1
        if flag ==1:
            sum =sum +list[i]
    return(sum)
print("sum of prime number in list is :",sumprime(myList))

#  WAP to clear all the elements in List1.
myList.clear()
print("Cleared list:", myList)

