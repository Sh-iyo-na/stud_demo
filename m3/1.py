# 1.Countdown Reminder Agent
# print("Countdown")
# for i in range(5,0,-1):
#     if i==1:
#         print(i)
#     else:
#         print(i, end='-> ')

# # 2. Attendance Processing Agent
# def attendance():
#     for i in range(1,11):
#         print(f"Student {i} is Checked")
# attendance()

# 3. Prime Number Checker Agent
# def prime_checker(id):
#     if id>1:
#         for i in range(2,id):
#             if id % i ==0:
#                 print(f"{id} is not a prime number")
#                 break
#         else:
#             print(f"{id} is a prime number")
#     else:
#         print(f"{id} is not a prime number")
# id=int(input("Enter id number: "))
# prime_checker(id)

# 4. Prime Number Discovery Agent
# def prime_discovery():
#     print("Prime Number Discovery")
#     for i in range(1,101):
#         if i>1:
#             for j in range(2,i):
#                 if i%j ==0:
#                     break
#             else:
#                 print(i, end=' ')
# prime_discovery()

# 5. Fibonacci Prediction Agent
# def fibonacci(n):
#     a,b=0,1
#     print("\nFibonacci Sequence:")
#     for i in range(n):
#         print(a, end=" ")
#         a,b=b,a+b
# n=int(input("\nEnter the number of terms for fibonacci sequence: "))
# fibonacci(n)

# 6.Alert Pyramid Agent
# def pyramid():
#     print("Alert Pyramid")
#     for i in range(1,6):
#         print("* "*i)
# pyramid()

# 7.Task Completion Agent
# def pattern():
#     print("Task completion agent")
#     for i in range(1,6):
#         for j in range(1,i+1):
#             print(j,end=' ')
#         print()
# pattern()

# 8. Data Summarization Agent
# def sum(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     print(f"Sum: {sum}")
# n=int(input("Enter the count to calculate the sum: "))
# sum(n)

# # 9.ID Reversal Agent
# def reverse(id):
#     rev=0
#     while id>0:
#         rev=(rev*10)+id%10
#         id=id//10
#     print(f"Reversed id: {rev}")
# id=int(input("Enter the id: "))
# reverse(id)

# # 10.Text Processing Agent
# def reverse(str):
#     rev=str[::-1]
#     print(f"Reversed message: {rev}")
# str=input("Enter the message: ")
# reverse(str)

# # 11. Number Validation Agent
# def armstrong(n):
#     sum=0
#     temp=n
#     power=len(str(n))
#     while temp>0:
#         digit=temp%10
#         sum+=digit**power
#         temp//=10
#     if n==sum:
#         print(f"{n} is an Armstrong number")
#     else:
#         print("Not an Armstrong number")
# n=int(input("Enter the number to check: "))
# armstrong(n)

# # 12. Palindrome Verification Agent
# def palindrome(s):
#     if s==s[::-1]:
#         print(f"{s} is palindrome")
#     else:
#         print("Not a palindrome")
# s=input("Enter the id: ")
# palindrome(s)

# # 13. Password Symmetry Agent
# def palindrome(s):
#     if s==s[::-1]:
#         print(f"{s} is palindrome")
#     else:
#         print("Not a palindrome")
# s=input("Enter the text: ")
# palindrome(s)