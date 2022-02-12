#WAP given string is palindrome
def palindrome(n):
   val = ''
   val=val+n[::-1]
   if (val == n):
      print("palindrome")
   else:
      print("Not palindrome")
str1=input()
palindrome(str1)
