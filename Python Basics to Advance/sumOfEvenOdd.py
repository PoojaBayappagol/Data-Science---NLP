num=int(input("Enter a number: "))

even=0
odd=0

for i in range(1,num+1):
    if i%2==0:
        even=even+i
    else:   
        odd=odd+i
print("The sum of even numbers from 1 to",num,"is:",even)
print("The sum of odd numbers from 1 to",num,"is:",odd)