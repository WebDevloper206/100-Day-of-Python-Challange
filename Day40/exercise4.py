import random
import string
length = 3
generated_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))



st = input("Enter message: ")
words = st.split(" ")
opt = input("1 for Coding or 0 for Decoding: ")
opt = True if (opt=="1") else False
if(opt):
  nwords = []
  for word in words:
    if(len(word)>=3):
      stnew = generated_string + word[1:] + word[0] + generated_string
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))

else:
  nwords = []
  for word in words:
    if(len(word)>=3): 
      stnew = word[3:-3]
      stnew = stnew[-1] + stnew[:-1]
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))
  