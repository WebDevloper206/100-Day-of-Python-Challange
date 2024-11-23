a = int(input("Enter any value between 5 and 9: "))

if(a<5  or a>9):
  raise  ValueError("Value should be between 5 and 9")

#Quick Quiz

a = str(input("Enter 'quit' to not raise an error"))

if(a != 'quit' ):
  raise ValueError("You should write 'quit' to not raise an error: ")