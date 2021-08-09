# You can find information on how to convert numbers to a different base here:
# https://www.tutorialspoint.com/computer_logical_organization/number_system_conversion.htm

# You can find information on how to convert numbers to roman numerals here:
# https://www.romannumerals.org/converter


def binarify(num): 
  """convert positive integer to base 2"""
  if num<=0: return '0'
  digits = []
  while num > 0: 
    digits.append(num % 2) 
    num //= 2
  digits = digits[::-1]
  return ''.join(str(i) for i in digits)
# print(binarify(29))

def int_to_base(num, base):
  """convert positive integer to a string in any base"""
  if num<=0:  return '0' 
  digits = []
  if num<=0: return '0'
  digits = []
  while num > 0: 
    digits.append(num % base) 
    num //= base
  digits = digits[::-1]
  return ''.join(str(i) for i in digits)
  # return ''.join(digits)
# print(int_to_base(29,3))



# def base_to_int(string, base):
#   """take a string-formatted number and its base and return the base-10 integer"""
#   if string=="0" or base <= 0 : return 0 
#   result = 0 
#   for i in range(1,len(string)+1):
#     x_i = string[-i] * (base ** (i-1))
#     result += int(x_i)
#   return result 
# print(base_to_int("11101", 2))

def base_to_int(string,base):
  if string=="0" or base <= 0 : return 0 
  result = 0
  l = len(string) 
  for i in string:
    if int(i) >= base:
      print("ERROR: Number is not in correct base!!!")
      break
    l = l - 1  
    result = result + int(i) * (base ** l)
  return result 
# print(base_to_int("1002", 3)) # = 29




def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum in base 10"""
  # result = int_to_base(tmp, base1)
  result = base_to_int(str1, base1) + base_to_int(str2, base2)
  return result 
print(flexibase_add("1002", "11101", 3, 2))


def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  result = int_to_base(tmp, base1)
  return result 


##  tricky! 

def romanify(num):
  """given an integer, return the Roman numeral version"""
  result = ""
  m = num // 1000
  n = num % 1000 
  d = n // 500 
  n = n % 500
  c = n // 100 
  n = n % 100
  l = n // 50
  n = n % 50
  x = n // 10
  n = n % 10
  v = n // 5
  n = n % 5
  i = n

  




  return result


# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.