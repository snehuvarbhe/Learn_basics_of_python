#This prgram returns the number of digits present in a number
number=int(input("Enter the number to count digits"))
count=0
while(number>0):
    count=count+1
    number=int(number/10)
print("Total digits are:",count)