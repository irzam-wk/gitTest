def fact(int1):
    fact = 1    
    while int1!=0:
        fact = fact*int1
        int1 = int1-1
    return fact
def main():
    a = input("Enter the no u want a fact of: ")
    a = int(a)
    result = fact(a)
    print("Factorial of ", a, " is: ", result)
    
if __name__ == "__main__":
    main()
