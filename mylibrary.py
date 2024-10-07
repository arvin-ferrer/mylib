#!/usr/bin/python3

def menu():
    
    print("""\n
WELCOME TO ARVIN'S USELESS CODE LIBRARY
          
[1] Print all divisors of n
[2] Count all the number of zero in a list
[3] Find the GCF of two (2) numbers
[4] Find the LCM of two (2) numbers
[5] Find the LCM of three (3) numbers
[6] Is n a prime? 
[7] Generating primes between n and 2n
[8] Twin primes!!
[9] Enter n and you get nxn multiplication table
[10] Enter n and you get an isosceles triangle of height n
[11] Enter L and W and you get a box-shaped figure with L chars long and W chars thick
[12] Merry Christmas!
          
[0] Exit
          \n""")
    
def divisors():

    num = int(input("Enter an integer: "))

    for i in range(1, num+1):
        if num % i == 0:
            print(i)

def countzeroes():
    
    intnum = int(input("Enter an integer: "))
    listnum = input("Enter list of numbers: ")
    count = 0
    nums = listnum.split()
    if len(nums) != intnum:
        print("Integer is not equal to the list of numbers!")
  
    elif len(nums) == intnum:
        for i in nums:
            if i == "0":
                count += 1
        print(count)

def GCF():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    larger = num1
    emptyls = []
    if num1 > num2:
        larger = num1 
    else:
        larger = num2 
    for i in range(1, larger): 
        if (num1 % i == 0) and (num2 % i == 0):
           emptyls.append(i)
    
    print(f"GCF is {emptyls[-1]}")

def LCM():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    larger = num1
    gcf = []
    if num1 > num2:
        larger = num1 
    else:
        larger = num2 
    for i in range(1, larger):
        if (num1 % i == 0) and (num2 % i == 0):
           gcf.append(i)

    lcm = (num1*num2)/gcf[-1]
    return lcm

def LCM3():
    lcmOf2 = LCM()
    num3 = int(input("Enter third number: "))
    larger = lcmOf2
    gcf = []
    if lcmOf2 > num3:
        larger = lcmOf2
    else:
        larger = num3
    for i in range(1, int(larger)):
        if (lcmOf2 % i == 0) and (num3 % i == 0):
           gcf.append(i)
    lcm = (lcmOf2*num3)/gcf[-1]
    print(f"LCM is {int(lcm)}")

def prime():
    num = int(input("Enter an integer: "))
    noOfdivisor = 0
    for i in range(1, num+1):
        if num % i == 0:
            noOfdivisor +=1

    if noOfdivisor == 2:
        print(f"{num} is a prime")
    elif noOfdivisor > 2:
        print(f"{num} is a composite")
    else:
        print(f"{num} is neither a prime nor a composite")

def genprime():
    num = int(input("Enter an integer: "))
    count = 0
    primes = []
    for i in range(num, (2*num)+1):
        for j in range(1, i+1):
            if i % j  == 0:
                count +=1 
        if count == 2:
            primes.append(j)    
            count = 0
        else:
            count = 0
    print(primes)

def twinprimes():
    count = 0
    primes = []
    twinprimes = []
    for i in range(1, 128):
        for j in range(1, i+1):
            if i % j  == 0:
                count +=1 
        if count == 2:
            primes.append([j])    
            count = 0
        else:
            count = 0
    for k in range(1, len(primes)):
        twinprimes.append([primes[k][0], primes[k][0]+2])
    print(twinprimes)
    
def multiTable():
    n = int(input("Enter an integer: "))
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{(i*j):^2}",  end= " ")
        print("\n")

def triangle():
    n = int(input("Enter an integer: "))
    width = 4*n-2
    for i in range(1, n+1):
        print(f"{(" * "*i):^{width}}", end=" ")
        print("\n")

def box():
    l = int(input("Enter an integer: "))
    w = int(input("Enter an integer: "))
    for i in range(l):
        if i == 0:
            print("# "*w, end=" ")
        
        elif i == l-1:
            print("# "*w, end=" ")
        else:
            print("#", "  "*(w-2), end="#")
        print("\n", end="")



def christmas():
    n = int(input("How many stacks is your tree? "))
    for i in range(1,n+1):  
        for j in range(i,2 * i+1):
            print(" "*(2*n-j+1)+"#"*(j*2-1))
                



def main():
    menu()
    choice = True
    while choice:
        userchoice = input("\nEnter your choice: ")
        if userchoice == "1":
            divisors()
            menu()
        elif userchoice == "2":
            countzeroes()
            menu()
        elif userchoice == "3":
            GCF()
            menu()
        elif userchoice == "4":
            print(f"LCM is {int(LCM())}")
            menu()
        elif userchoice == "5":
            LCM3()
            menu()
        elif userchoice == "6":
            prime()
            menu()
        elif userchoice == "7":
            genprime()
            menu()
        elif userchoice == "8":
            twinprimes()
            menu()
        elif userchoice == "9":
            multiTable()
            menu()
        elif userchoice == "10":
            triangle()
            menu()
        elif userchoice == "11":
            box()
            menu()
        elif userchoice == "12":
            christmas()
            menu()
        elif userchoice == "0":
            print("Goodbye :)")
            break
main()