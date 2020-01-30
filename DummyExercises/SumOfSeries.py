"""Sum Of A Series"""
"""1+x^2/2+x^3/3+..."""
n=int(input("Enter the number of terms:"))
x=int(input("Enter the value of x:"))
sum_=1
for i in range(2,n+1):
    sum_= sum_ +((x**i)/i)
print("The sum of series is",round(sum_,2))
    