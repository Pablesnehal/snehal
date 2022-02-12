def checkprime(n):
  if(n<=1):
    return "Not prime"
  else:
    for i in range(2,(n//2+1)):
      if(n%i==0):
        return "Not Prime"
      else:
        return "Prime"
def checkFactorial(n):
  fact=1
  for i in range(1,n+1):
    fact=fact*i
  return fact
def checkPalindrome(n):
  val=n
  rev=0
  while(n!=0):
     rem=n%10
     rev=rev*10+rem
     n=n//10
  if(rev==val):
    return "yes palindrome"
  else:
    return "Not palindrome"
def checkamstrong(n):
  val=n
  length=len(str(n))
  rev=0
  while(n!=0):
     rem=n%10
     rev=rev+(rem**length)
     n=n//10
  if(rev==val):
    return "yes "
  else:
    return "No"


while True:
    print("\nMAIN MENU")
    print("1. Check number is Prime or not")
    print("2. Check number of factorial")
    print("3. Check number is palindrome or not")
    print("4. Check number is amstrong or not")
    print("5. Exit")
    num = int(input("Enter the Choice:"))
    if (num==1):
      value=int(input())
      print(checkprime(value))
    if (num==2):
      value=int(input())
      print(checkFactorial(value))
    if (num==3):
      value=int(input())
      print(checkPalindrome(value))
    if (num==4):
      value=int(input())
      print(checkamstrong(value))
    if (num==5):
      break
