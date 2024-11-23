import time
name = input('Enter Your Name: ')
recenttime = time.strftime('%H:%M:%S')
Recenttime = int(time.strftime('%H'))
name= name.capitalize()
if(4<=Recenttime<12):
    print('Good Morning!',name,'its',recenttime)
elif(12>=Recenttime<17):
    print('Good Evening!',name,'its',recenttime)
else:
    print('Good Night!',name,'its',recenttime)