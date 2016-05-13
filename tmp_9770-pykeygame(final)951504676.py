import keyword as k
import time as t

#making a list of keys from the keyword module
keys = k.kwlist

       
#title stuff
print('')
print('Python Keyword Game!')
print('')
t.sleep(1)
print('Guess all the python keywords!')
print('')
print('type h for a hint')
print('type r for rules')
print('')
t.sleep(2)


#other variables and empty list
words = 33
count = 1
used = []
hints = 0
wrong = 0
plat = False
hintNum = 0


#hitchhikers guide to the game
rules = """\nRules:\nGuess keywords. Incorrect words
and hints used count against you.
Hints are limited per word.
Correct words guessed twice do not
count against you. 
There are six trophies. Have fun!\n"""


#the trophies
tro = 'Trophy: '
ta = "Noob\nMade it to ten!"
tb = "Pythonista!\nMade it to twenty."
tc = "Padawan\nMade it to thirty!"
td = "Elit3 h4x0r\nNamed them all!"
te = "Guido would be proud\nNo hints, no mistakes!"
tf = "Platinum\nKeyword Master!"
line ='____________________________'


#main game loop
while words != 0:
    hintWord = [keys[0]]
    nextLetter = hintWord[0][hintNum]
    g = input('Guess a word: ')
    if g in keys:
#removes from kw list and puts in used
        keys.remove(g)
        used.append(g)
        words = words - 1
        print(str(count)+". "+ str(g))
        count = count + 1
        if count == 10:
            print(line)
            print(tro + ta)
            print(line)
        if count == 20:
            print(line)
            print(tro + tb)
        if count == 30:
            print(line)
            print(tro + tc)
            print(line)
        print('Correct! Guess again\n')
        hintNum = 0
    elif g == "h":
        wrong = wrong + 1
        if hintNum == 0:
            print('Next word starts with ' + hintWord[0][hintNum])
            hintNum = hintNum + 1
        elif hintNum < int(len(keys[0])/2):
            print('Next letter is ' + hintWord[0][hintNum])
            hintNum = hintNum + 1
        elif wrong == 5:
            print(line + '\nNot looking so good\n' + line)
        elif wrong == 10:
            print(line + '\nAre you even trying?\n' + line)
        elif wrong == 15:
            print(line + "\nMan, you're really bad at this!\n" + line)
        elif wrong == 20:
            print(line + "\nMaybe programming isn't for you.\n" + line)    
        elif wrong == 30:
            print(line + "\nAre you being serious right now?\n" + line)             
        elif wrong == 35:
            print(line + "\nWhat are you doing with your life?\n" + line)     
        
        else:
            print('Too many hints for this word.')        
       
    elif g == "r":
        print(rules)
        
    elif g in used:
        print('Already used. Try again.\n')
                         
    else:
        print('WRONG\n')
        wrong = wrong + 1
        if wrong == 5:
            print(line + '\nNot looking so good\n' + line)
        elif wrong == 10:
            print(line + '\nAre you even trying?\n' + line)
        elif wrong == 15:
            print(line + "\nMan, you're really bad at this!\n" + line)
        elif wrong == 20:
            print(line + "\nMaybe programming isn't for you.\n" + line)    
        elif wrong == 30:
            print(line + "\nAre you being serious right now?\n" + line)             
        elif wrong == 35:
            print(line + "\nWhat are you doing with your life?\n" + line)     
        
#winner winner chicken dinner        
print('You win!')
print(tro + td)
print('You got ' + str(wrong) + ' wrong.')
print('You used ' + str(hints) + ' hints.')
if wrong == 0:
    plat = True
    print(line)
    print('Special Trophy: ' + te)
    print(line)
    if plat == True:
        print(line)
        print(tro + tf)
        print(line)