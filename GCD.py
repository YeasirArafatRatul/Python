def compute_gcd(x,y):
    #find the smaller 
    smaller = min(x,y)
    gcd = 1
    for i in range(1,smaller+1):
        if((x%i == 0) and (y%i==0)):
            #gcd will be alterted each time the condition is  true, so do
            #not need find the maximum.
            gcd = i
    return gcd

num1 = int(input("First number:"))
num2 = int(input("Second number:"))
gcd = compute_gcd(num1,num2)
print(gcd)
