def sum_divisors(n):
  # Return the sum of all divisors of n, not including n
  result = 0
  i = 1
  while i < n:
    if n%i == 0:
      
      result += i
    i+=1
  return result

print(sum_divisors(6)) # Should be 1+2+3=6
print(sum_divisors(12)) # Should be 1+2+3+4+6=16
