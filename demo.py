#for x in range(0,N):
    #occurrance = 0
    #for y in range(0,N):
        #if a[x] == a[y]:
            #occurrance += 1
    #if (occurrance%2 != 0):
        #return a[x]
#return -1


def similarity(num1, num2):
    if ((num1 ^ num2) != 0):
        print("Numbers are not equal")
    else:
        print("Both numbers are equal")

n1 = int(input("Enter first number to compare: "))
n2 = int(input("Enter second number to compare: "))

similarity(n1, n2)

def oddity(arr):
    res = 0
    for element in arr:
        res = res^element
    return res

arr = []
n = int(input("Enter array size: "))

while(n):
    num = int(input("Enter number: "))
    arr.append(num)
    n -= 1
print(f"\n\nOdd occuring number is: {oddity(arr)}")

def oddity2(arr, size):
    xorof2 = arr[0]
    x = 0
    y = 0
    setbit = 0
    
    for i in range(1, size):
        xorof2 = xorof2^arr[i]
    
    setbit = xorof2 & ~(xorof2-1)
    
    for i in range(size):
        if(arr[i] & setbit):
            x = x^arr[i]
        else:
            y = y^arr[i]

arr = []

arr_size = int(input("Enter size of the array: "))
for i in range(0, arr_size):
    z = int(input("Enter element: "))
    arr.append(z)

oddity2(arr, arr_size)