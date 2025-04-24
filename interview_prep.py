word = "madam"

def check_palindrome(word):
     word.lower()
     if word == word[::-1]:
          print("Yes is palindrome")
     else: 
          print("No is not palindrome") 
     
     
check_palindrome(word)