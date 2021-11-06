VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer():
    """ represents a player """
    def __init__(self,name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
        #print("Initialized {} as WOFPlayer",name)

    def addMoney(self,amt):
        self.prizeMoney += amt
        #print("Congrats {}! You've won ${}".format(self.name,self.prizeMoney))

    def goBankrupt(self):
        self.prizeMoney = 0
        #print("Sorry {}! You've gone Bankrupt".format(self.name))

    def addPrize(self,prize):
        self.prizes.append(prize)
        #print("Congrats {}!{} added to your prize list".format(self.name, prize))

    def __str__(self):
        return("{} (${})".format(self.name,str(self.prizeMoney)))
    
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    """ represents a human player"""
    def __init__(self,name):
        WOFPlayer.__init__(self,name)
        #print("initialized humanplayer - {}".format(name))

    def getMove(category,obscuredPhrase,guessed):
        move = input("Guess a letter, phrase, or type 'exit' or 'pass':")
        #print("{} got selected a move - {}".format(self.name,move))
        return move

# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    """ represents a computer player"""
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    
    def __init__(self,name,difficulty):
        WOFPlayer.__init__(self,name)
        self.difficulty = difficulty
        #print("Initialized Computer Player - {} with difficulty set to {}".format(name,difficulty))

    def smartCoinFlip(self):
        rand_number = random.randint(1, 10)
        if rand_number > self.difficulty:
            #print("Random Number: {}, SelfDifficulty: {}".format(rand_number,self.difficulty))
            return True
        elif rand_number <= self.difficulty:
            #print("Random Number: {}, SelfDifficulty: {}".format(rand_number,self.difficulty))
            return False

    def getPossibleLetters(self,guessed):
        letterlist = []
        #print("Guessed - ",guessed)
        if guessed != 'pass':
            letters = [letter for letter in guessed]
            rand_letter = random.choice(letters)
            if rand_letter not in guessed:                
                if self.prizeMoney >= VOWEL_COST:
                    if rand_letter in VOWELS:
                        letterlist.append(rand_letter)
                else:
                    if rand_letter not in VOWELS:
                        letterlist.append(rand_letter)
                    else:
                        return "pass" 
        else:
            return "pass"
        return letterlist

    def getMove(self, category, obsuredPhrase, guessed):
        if  self.smartCoinFlip() == True:
            gletters = self.getPossibleLetters(self.SORTED_FREQUENCIES)
            #print("Smart move - guessed letter - {}, lettercount = {}".format(gletters,len(gletters))
            if len(gletters) > 0:
                #print("Smart Move - Letter guessed: ",gletters)
                return gletters
            else:
                return 'pass'
        else:
            gletters = self.getPossibleLetters(LETTERS)
            #print("SDumb move - guessed letter - {}, lettercount = {}".format(gletters,len(gletters))
            if len(gletters) > 0:
                #print("Dumb Move - Letter guessed: ",gletters)
                return gletters
            else:
                return 'pass'

