print("WelCome to QuizGame")
play=input("Do You Want to Play? ")

if play.lower() != "yes":
    quit()
Score=0
ANS=input('''CHOSE CORRECT OPTION
Q1.Name of the screen that recognizes touch input is :
A.Recog screen
B.Point Screen
C.Touch Screen
D.Android Screen \n''')

if ANS.lower() =="c":
    print("Correct!")
    Score +=1
else:
    print("Incorrect!")

ANS=input('''CHOSE CORRECT OPTION
Q2.Identify the device through which data and instructions are entered into a computer
A.Software
B.Output device
C.Input device
D.Memory \n''')

if ANS.lower() =="c":
    print("Correct!")
    Score +=1
else:
    print("Incorrect!")

ANS=input('''CHOSE CORRECT OPTION
Q3.Computer Moniter is also known as :
A.DVU
B.UVD
C.CCTV
D.VDU \n''')

if ANS.lower() =="d":
    print("Correct!")
    Score +=1
else:
    print("Incorrect!")

ANS=input('''CHOSE CORRECT OPTION
Q4.Arrange in ascending order the units of memory TB, KB, GB, MB
A.TB>MB>GB>KB
B.MB>GB>TB>KB
C.TB>GB>MB>KB
D.GB>MB>KB>TB \n''')

if ANS.lower() =="c":
    print("Correct!")
    Score +=1
else:
    print("Incorrect!")

ANS=input('''CHOSE CORRECT OPTION
Q5 Which one of these stores more data than a DVD ?
A.Blue Ray Disk
B.Floppy
C.CD Rom
D.Red Ray Disk \n''')

if ANS.lower() =="a":
    print("Correct!")
    Score +=1
else:
    print("Incorrect!")

#print score   
print(" \nyou did " + str(Score) + " Question Correct!")
print("you got " + str((Score/5)*100) +"%.")