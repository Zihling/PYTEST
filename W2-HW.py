# hw1 四則運算
n1=int(input("Enter a number: "))
n2=int(input("Enter a number: "))
op=input("Enter an operator:+,-,*,/ :")
if   op =='+':  
    print(n1+n2)
elif op =='-':
    print(n1-n2)
elif op =='*':
    print(n1*n2)
elif op =='/':
    print(n1/n2)


#hw2 印出99乘法表
for x in range(1,10):      
    for y in range(1,10): 
        print("%d*%d=%d"%(x,y,x*y))