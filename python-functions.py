def sum_to(n):
  return sum(range(n+1))

print(sum_to(6)) 
print(sum_to(10)) 


def largest(list):
    max = list[0]
    for n in list:
        if n > max:
            max = n
    return max


print(largest([1, 2, 3, 4, 0]))
print(largest([10, 4, 2, 231, 91, 54]))


def occurances(str1, str2):
  print(str1.count(str2))


occurances('fleep floop', 'e')   # returns 2
occurances('fleep floop', 'p')   # returns 2
occurances('fleep floop', 'oo')  # returns 1
occurances('fleep floop', 'fe')  # returns 0


def product(*num):
  sum = 1
  for n in num:
    sum = sum * n
  print(sum)


product(-1, 4)  # returns -4
product(2, 5, 5)  # returns 50
product(4, 0.5, 5)  # returns 10.0
