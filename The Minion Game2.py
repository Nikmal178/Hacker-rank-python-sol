# take the string input
string = str(input().upper())

def minionGame(string):
    Kevin_score = 0
    Stuart_score = 0
    n = len(string)
    vowels = 'AEIOU'
    for i in range(n):
        if string[i] not in vowels:   # checks if the character at position i at the string is a consonant
            Stuart_score += n - i     
        elif string[i] in vowels:
            Kevin_score += n - i   
    # for a string = 'BANANA'. For i = 0, String[0] = 'B'. n = 6
    # All possible combinations of the characters after B are 'B', 'BA', 'BAN', 'BANA', 'BANAN', 'BANANA'. 
    # Stuart_score = 6 - 0 = 6
    # Next, i = 1, string[1] = 'A', a vowel. 
    # Possible combinations are: 'A', 'AN', 'ANA', 'ANAN', 'ANANA'
    # Kevin_score = 6 - 1 = 5

    # displaying the score

    if Kevin_score > Stuart_score:
        print("Kevin {}".format(Kevin_score))
    elif Stuart_score > Kevin_score:
        print("Stuart {}".format(Stuart_score))
    else:
        print("Draw")        


minionGame(string)        