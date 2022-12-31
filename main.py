from replit import clear
def add(n1,n2):
    nums.append(n1+n2)
    return n1+n2
def subtract(n1,n2):
    nums.append(n1-n2)
    return n1-n2
def multiply(n1,n2):
    nums.append(n1*n2)
    return n1*n2
def divide(n1,n2):
    if(n2==0):
        return "invalid second number"
    nums.append(n1/n2)
    return n1/n2
    
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
nums=[]
end=False

print("WELCOME TO THE CALCULATOR!")
num1=float(input("please input the first number:\n"))
for i in operations:
    print(i)
op=input("please select an operation:\n")
num2=float(input("please input the second number:\n"))
print(f"{num1} {op} {num2} = {operations[op](num1,num2)}")
while(end!=True):
    answer=input("Would you like to continue?Y/N \n")
    if(answer.lower()=="n"):
        end=True
    else:
        clear()
        for i in operations:
         print(i)
        op=input("please select an operation:\n")
        new_num=float(input("please input the new number:\n"))
        print(f"{nums[-1]} {op} {new_num} = {operations[op](nums[-1],new_num)}")
    