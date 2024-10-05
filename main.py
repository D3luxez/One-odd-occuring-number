#Program to find the element not making a peir
def oddoccuring(arr):
    res = 0
    for element in arr:
        res = res^element
    return res
arr = []
n = int(input("Enter array size: "))
#take array element input
while(n):
    num = int(input("Enter number: "))
    arr.append(num)
    n-=1
print("\n\n odd occuring number is : ",oddoccuring(arr))