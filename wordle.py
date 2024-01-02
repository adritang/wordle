import sys
import random

class Draw:
        def correctLetter(self, letter):
                print('.' + letter + '. ',end='')

        def incorrectLetter(self, letter):
                print('?' + letter + '? ',end='')

        def semiLetter(self, letter):
                print('!' + letter + '! ',end='')

class Dictionary:
        def isInWord(self, letter, word):
                if str(letter) in str(word):
                    return True
                else:
                    return False
        def isRightSpot(self, letterA, letterB):
                return letterA == letterB
                        
        def isLetterIncorrect(self, letter, word):
                return not isLetterCorrect(letter, word)

        def generateWord(self, numChars):
                try:
                        with open('words.txt') as in_file:
                                loaded_txt = in_file.read().strip().split('\n')
                                print('Dictionary has',len(loaded_txt),'words.')
                                self.newlist = []
                                for i in range(len(loaded_txt)):
                                        if len(loaded_txt[i]) == numChars:
                                                self.newlist.append(loaded_txt[i])
                        print(len(self.newlist), 'words found')
                        return random.choice(self.newlist)
                                
                except IOError as e:
                        print("{}\nError opening {}. Terminationg program.".format(e,file), file=sys.stderr)
                        sys.exit(1)

        def isValidWord(self, word):
                return word in self.newlist


class User:
        def name(self, you):
                '''asdf'''

        def record(self, streak):
                '''asdf'''

class Game:

        def __init__(self):
                print('Good Luck. Type wordle.start(number of letters you want to begin. (key: . means correct letter, ? means incorrect letter, ! means letter in wrong place)')
                self.dict = Dictionary()
                self.draw = Draw()
                self.user = User()
        
        def start(self, numChars=5):
                self.numChars = numChars
                self.currentWord = self.dict.generateWord(self.numChars)


                '''TURN LOOP'''
                for turn in range(6):

                        '''ASK USER FOR WORD'''
                        guess = input('Your guess:')
                        if not self.dict.isValidWord(guess):
                                guess = input('Not an English word:')
                        
                        '''CHECK EACH LETTER AND PRINT FEEDBACK'''
                        for i in range(self.numChars):
                                if self.dict.isInWord(guess[i], self.currentWord):
                                        if self.dict.isRightSpot(guess[i], self.currentWord[i]):
                                                self.draw.correctLetter(guess[i])
                                        else:
                                                self.draw.semiLetter(guess[i])
                                else:
                                        self.draw.incorrectLetter(guess[i])
                                        
                        print()
                        if self.dict.isInWord(guess, self.currentWord):
                                print('You win!')
                                break
                        if turn == 5:
                                print('You lose!')
                                print(self.currentWord, 'was the answer dummy')




wordle = Game()

'''

---previous code/project outline----

IF ISINWORD THEN
  IF CORRECTSPORT(guess[i},currentword[i] THEN PRINT CORRECT
  ELSE PRINT SEMI
ELSE
  PRINT WRONG
                                if self.dict.isLetterCorrect(guess[i],self.currentword):
                                        self.draw.correctLetter(guess[i])
                                else if self.dict.
                        
                                

'''
'''

class Game:
        def __init__(self, letters, tries):
                self.numLetters = letters
                self.maxtries = tries


'''
'''
------------CHECKING WHETHER LETTER IS IN THE WORD
def isLetterCorrect(letter, word):
        if str(letter) in str(word):
            return True
        else:
            return False


def isLetterIncorrect(letter, word):
    return not isLetterCorrect(letter, word)

letter = input('enter a letter: ')
word = input ('word: ')
print(isLetterCorrect(letter, word))

print(isLetterIncorrect(letter, word))



-------------CHECKING IF THE LETTER IS IN THE RIGHT SPOT
def isLetterSpace(letter, spot, word):
    if str(letter) in str(word):
        if str(letter) == str(word[spot-1]):
            return True
        else:
            return False
    else:
        return False

--------------MAKING LOWERCASE
letter = input('enter a letter: ')
spot = input('enter a number: ')
word = input('enter a word: ')
print(isLetterSpace(letter, int(spot), word))



def isWord(word):
    if str(word.lower()) == 'word':
        return True
    else:
        return False

word = input('enter a word: ')
print(isWord(word))

'''

'''-------DRAW (IN)CORRECT LETTER
letters = [0, 1, 2, 3, 4]
def drawLetter(yourword, word):
        for x in letters:
                if str(yourword[0]) in str(word):
                    if str(yourword[0]) == str(word[0]):
                        print('.' + yourword[0] + '.' + yourword[1:])
                    else:
                        print('!' + yourword[0] + '!' + yourword[1:])
                else:
                    print('?' + yourword[0] + '?' + yourword[1:])

yourword = input('enter a word: ')
word = input ('enter another word: ')
print(drawLetter(yourword, word))
'''
