class spindle:

    def __init__(self, rotor_I, rotor_II, rotor_III, rotor_IV, rotor_V, reflector_I, reflector_II, reflector_III, reflector_IV):
    
        self.rotor_I = rotor_I
        self.rotor_II = rotor_II
        self.rotor_III = rotor_III
        self.rotor_IV = rotor_IV
        self.rotor_V = rotor_V
        self.reflector_I = reflector_I
        self.reflector_II = reflector_II
        self.reflector_III = reflector_III
        self.reflector_IV = reflector_IV

def inputs (r, rotor, p, position, ref, user_plugboard):

    i = 0
    c = 0
    global choice
    global message
    global refl
    choice_2 = ""
    number = ["first" , "second" , "third"]

    while (c != 1 or c != 2):

        try:

            print ("1. Encrypt a message" , "\n")
            #sleep (1)
            print ("2. Decrypt a message" , "\n")
            #sleep (1)
            c = int (input ("Please choose an option from above: "))
            print ("\n")   
            sleep (1)

            if (c == 1 or c == 2):

                choice = c
                break

            else:

                print ("Choose either 1 or 2 ")
                sleep (1)
                print ("Please try again" , "\n")
                sleep (1)

        except ValueError:

            print ("Choose either 1 or 2 ")
            sleep (1)
            print ("Please try again" , "\n")
            sleep (1)

    for i in range (0,3):

        while (r != "I" or r != "II" or r != "III" or r != "IV" or r != "V"):

            print ("I, II, III, IV, V" , "\n")
            sleep (1)
            r = str (input ("Please choose your " + number[i] + " rotor: "))
            r = r.upper()
            print ("\n")
            sleep (1)

            if (r == "I" or r == "II" or r == "III" or r == "IV" or r == "V"):

                rotor.append(r)
                break

            else:

                print ("Incorrect choice")
                sleep (1)
                print ("Please try again" , "\n")
                sleep (1)  
    
    for i in range (0,len(rotor)):

        if (rotor[i] == "I"):

            rotor[i] = spindle.rotor_I 

        elif (rotor[i] == "II"):

            rotor[i] = spindle.rotor_II

        elif (rotor[i] == "III"):

            rotor[i] = spindle.rotor_III 

        elif (rotor[i] == "IV"):

            rotor[i] = spindle.rotor_IV

        elif (rotor[i] == "V"):

            rotor[i] = spindle.rotor_V 
    
    for i in range (1,4):

        p = 0

        while (p not in range (1,27)):

            try:

                print ("('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5), ('F', 6), ('G', 7), ('H', 8), ('I', 9), ('J', 10)") 
                print ("('K', 11), ('L', 12), ('M', 13), ('N', 14), ('O', 15), ('P', 16), ('Q', 17), ('R', 18), ('S', 19), ('T', 20)")
                print ("('U', 21), ('V', 22), ('W', 23), ('X', 24), ('Y', 25), ('Z', 26)" , "\n")
                sleep (1)
                p = int( input (f"Choose the position of rotor {i} by writing the number of the letter: "))
                print ("\n")

                if (p in range (1,27)):

                    position.append(p)
                    sleep (1)

                else:

                    print ("Only a number within 1 to 26 is allowed")
                    sleep (1)
                    print ("Please try again" , "\n")
                    sleep (1)

            except ValueError:

                print ("Only a number within 1 to 26 is allowed")
                sleep (1)
                print ("Please try again" , "\n")
                sleep (1)

 
    while (choice_2 != "Y" or choice_2 != "N"):

        choice_2 = input ("Do you want to use the built-in plugboard settings? [Y/N] ").upper()
        sleep (1)

        if (choice_2 == "Y"):

            user_plugboard = ["ab" , "cd" , "ef" , "gh" , "ij" , "kl" , "mn" , "op" , "qr" , "st" , "uv" , "wx" , "yz" , 
                              "AB" , "CD" , "EF" , "GH" , "IJ" , "KL" , "MN" , "OP" , "QR" , "ST" , "UV" , "WX" , "YZ" ,
                              "09" , "18" , "27" , "36" , "45" ]
            break

        elif (choice_2 == "N"):

            print ("You are now going to enter the 13 plugboard settings as follows")
            sleep (1)
            print ("Example: ab, cd, etc..." , "\n")
            sleep (1)
            
            for g in range (1,4):

                plug = ""

                while (plug == "" or len(plug) != 2 or plug[0] == plug[1]):

                    plug = input (f"Plugboard setting number {g}: ")
                    print ("\n")
                    sleep (1)

                    if (len(plug) == 2):

                        if (plug[0] == plug[1]):

                            print ("Do not repeat letters")
                            sleep (1)
                            print ("Please try again" , "\n")
                            sleep (1)

                        else:

                            user_plugboard.append(plug)
                            print(user_plugboard)
                            sleep (1)

                    else:

                        print ("Do not enter more than two characters")
                        sleep (1)
                        print ("Please try again" , "\n")
                        sleep (1)

            break

        else:

            print ("Please enter Y or N")
            sleep (1)
            print ("Please try again" , "\n")
            sleep (1)

    while (ref != 1 or ref != 2 or ref != 3 or ref != 4):

        try:

            print ("1. Reflector B")
            #sleep (1)
            print ("2. Reflector B thin")
            #sleep (1)
            print ("3. Reflector C")
            #sleep (1)
            print ("4. Reflector C thin" , "\n")
            #sleep (1)
            ref = int (input ("Please choose your reflector: "))
            print ("\n")   
            sleep (1)

            if (ref >= 1 and ref <= 4):

                break

            else:

                print ("A number from 1 to 4 is only allowed")
                sleep (1)
                print ("Please try again" , "\n")
                sleep (1)

        except ValueError:

            print ("A number from 1 to 4 is only allowed")
            sleep (1)
            print ("Please try again" , "\n")
            sleep (1)
                     
    if (ref == 1):

        refl = spindle.reflector_I

    elif (ref == 2):

        refl = spindle.reflector_II

    elif (ref == 3):

        refl = spindle.reflector_III

    elif (ref == 4):

        refl = spindle.reflector_IV
    
    message = input ("Please enter your message: ")
    sleep (1)

def plugboard_algorithm (user):

    global letter
    plugboard_1 = []
    plugboard_2 = []

    for x in range (0,len(user)):

        plugboard_1.append(user[x][0])
        plugboard_2.append(user[x][1])

    for i in range (0,len(plugboard_1)):

        if (letter == plugboard_1[i]):

            letter = plugboard_2[i]

        elif (letter == plugboard_2[i]):

            letter = plugboard_1[i]

def rotor (alphabets,letter,rotors,order,option_1,option_2):

    if (order == 1):

        rotor_1 = rotors[0]
        rotor_2 = rotors[1]
        rotor_3 = rotors[2]

    elif (order == 2):

        rotor_1 = rotors[2]
        rotor_2 = rotors[1]
        rotor_3 = rotors[0]

    place = 0
    global letter_2
 
    if (option_1 == 1):

        place = alphabets[letter]

        for i in rotor_1:

            if (place == rotor_1[i]):

                letter = i

        place = alphabets[letter]

        for i in rotor_2:

            if (place == rotor_2[i]):

                letter = i

        if (option_2 == 1):

            place = alphabets[letter]

            for i in rotor_3:

                if (place == rotor_3[i]):

                    letter_2 = i

        elif (option_2 == 2):

            place = alphabets[letter]

            for i in rotor_3:

                if (place == rotor_3[i]):

                    letter_3 = i
                    encrypted.append(letter_3)

    elif (option_1 == 2):

        place = rotor_1[letter]

        for i in alphabets:

            if (place == alphabets[i]):

                letter = i

        place = rotor_2[letter]

        for i in alphabets:

            if (place == alphabets[i]):

                letter = i

        if (option_2 == 1):

            place = rotor_3[letter]

            for i in alphabets:

                if (place == alphabets[i]):

                    letter_2 = i

        elif (option_2 == 2):

            place = rotor_3[letter]

            for i in alphabets:

                if (place == alphabets[i]):

                    letter_3 = i
                    encrypted.append(letter_3)

def reflector (alphabets,letter,option):

    global letter_3

    if (option == 1):

        place = alphabets[letter] 

        for i in refl:

            if (place == refl[i]):

                letter_3 = i

    elif (option == 2):

        place = refl[letter] 

        for i in alphabets:

            if (place == alphabets[i]):

                letter_3 = i
        
spindle.rotor_I = {'H': 1  , 'M': 2  , '9': 3  , '3': 4  , 't': 5  , 'A': 6  , '0': 7  , 's': 8  , 'E': 9  , 'F': 10 , 
                   'L': 11 , 'K': 12 , 'W': 13 , 'r': 14 , 'v': 15 , 'a': 16 , 'c': 17 , 'R': 18 , 'd': 19 , 'G': 20 , 
                   'o': 21 , 'Z': 22 , 'h': 23 , 'Q': 24 , 'p': 25 , 'I': 26 , '5': 27 , 'x': 28 , 'U': 29 , '8': 30 , 
                   '6': 31 , 'b': 32 , '2': 33 , 'C': 34 , 'J': 35 , 'O': 36 , 'P': 37 , '1': 38 , '4': 39 , 'z': 40 , 
                   'T': 41 , 'm': 42 , 'X': 43 , 'i': 44 , 'n': 45 , 'V': 46 , 'D': 47 , 'B': 48 , 'S': 49 , 'l': 50 , 
                   'Y': 51 , 'j': 52 , 'g': 53 , 'y': 54 , 'f': 55 , 'w': 56 , 'q': 57 , 'k': 58 , 'u': 59 , '7': 60 , 
                   'N': 61 , 'e': 62}

spindle.rotor_II = {'8': 1  , 'h': 2  , 'r': 3  , '4': 4  , 'F': 5  , 'O': 6  , 'u': 7  , 'b': 8  , 'c': 9  , 'E': 10 ,
                    '0': 11 , 'P': 12 , 'g': 13 , 'Q': 14 , '1': 15 , 'Z': 16 , 'R': 17 , 'U': 18 , 'M': 19 , 'm': 20 , 
                    'y': 21 , 'I': 22 , 'o': 23 , 'D': 24 , 'V': 25 , 'p': 26 , '5': 27 , 'K': 28 , 'v': 29 , '2': 30 , 
                    '7': 31 , 't': 32 , 'j': 33 , 'q': 34 , 's': 35 , 'i': 36 , '9': 37 , 'C': 38 , 'k': 39 , 'e': 40 , 
                    'N': 41 , 'T': 42 , 'L': 43 , 'Y': 44 , 'G': 45 , 'a': 46 , 'X': 47 , 'w': 48 , 'B': 49 , 'H': 50 , 
                    'W': 51 , '6': 52 , 'n': 53 , '3': 54 , 'l': 55 , 'x': 56 , 'd': 57 , 'A': 58 , 'J': 59 , 'z': 60 , 
                    'S': 61 , 'f': 62}

spindle.rotor_III = {'2': 1  , 'Q': 2  , 'U': 3  , 'O': 4  , 'i': 5  , 'H': 6  , 'r': 7  , 'P': 8  , '9': 9  , 'W': 10 , 
                     'I': 11 , 'v': 12 , 'z': 13 , '1': 14 , 'l': 15 , 'S': 16 , 's': 17 , 'b': 18 , 'n': 19 , 'k': 20 , 
                     'p': 21 , 'V': 22 , 'F': 23 , '6': 24 , 'T': 25 , 'X': 26 , 't': 27 , 'L': 28 , 'D': 29 , 'A': 30 , 
                     'y': 31 , 'q': 32 , 'J': 33 , 'R': 34 , '8': 35 , 'M': 36 , '7': 37 , 'o': 38 , 'Y': 39 , 'm': 40 , 
                     '0': 41 , 'g': 42 , 'f': 43 , 'u': 44 , '3': 45 , 'e': 46 , 'j': 47 , 'c': 48 , 'B': 49 , 'h': 50 , 
                     '4': 51 , 'Z': 52 , 'a': 53 , 'w': 54 , 'd': 55 , 'C': 56 , 'K': 57 , 'E': 58 , 'N': 59 , '5': 60 , 
                     'x': 61 , 'G': 62}

spindle.rotor_IV = {'u': 1  , 'v': 2  , 'P': 3  , 'd': 4  , 'C': 5  , 'r': 6  , 'f': 7  , 'i': 8  , 'g': 9  , 'x': 10 ,
                    'J': 11 , '8': 12 , 'k': 13 , 'Z': 14 , '9': 15 , 'D': 16 , 'n': 17 , 'w': 18 , '0': 19 , 'X': 20 ,
                    'F': 21 , 'K': 22 , 'z': 23 , 'O': 24 , 'c': 25 , 'o': 26 , 'Y': 27 , 's': 28 , 'l': 29 , '5': 30 , 
                    'p': 31 , 'W': 32 , '7': 33 , 'U': 34 , 'j': 35 , 'E': 36 , 'b': 37 , 'B': 38 , 'S': 39 , 'R': 40 , 
                    'H': 41 , 'y': 42 , 'T': 43 , 'I': 44 , 'A': 45 , '3': 46 , '2': 47 , 'e': 48 , 'L': 49 , 'M': 50 , 
                    'Q': 51 , 'h': 52 , '1': 53 , '6': 54 , 'V': 55 , 'G': 56 , 'q': 57 , 'a': 58 , 'm': 59 , '4': 60 , 
                    't': 61 , 'N': 62}

spindle.rotor_V = {'L': 1  , 'Y': 2  , 'N': 3  , '1': 4  , 'k': 5  , 'z': 6  , 'p': 7  , '2': 8  , '3': 9  , 'h': 10 , 
                   'W': 11 , 'V': 12 , 'i': 13 , 'S': 14 , '7': 15 , 'b': 16 , '8': 17 , 'R': 18 , 'o': 19 , 'f': 20 , 
                   't': 21 , 'P': 22 , 'B': 23 , 'Z': 24 , 'n': 25 , 'X': 26 , 'C': 27 , '9': 28 , 'w': 29 , 'U': 30 , 
                   'I': 31 , 'J': 32 , '5': 33 , 'H': 34 , 'd': 35 , 'r': 36 , 'c': 37 , 'M': 38 , 'a': 39 , '6': 40 , 
                   'm': 41 , 'K': 42 , 'G': 43 , '0': 44 , 'j': 45 , 'g': 46 , 'l': 47 , 'q': 48 , 's': 49 , 'T': 50 , 
                   'e': 51 , '4': 52 , 'A': 53 , 'Q': 54 , 'F': 55 , 'y': 56 , 'E': 57 , 'u': 58 , 'v': 59 , 'O': 60 , 
                   'x': 61 , 'D': 62} 

spindle.reflector_I = {'i': 1  , '1': 2  , '8': 3  , 'N': 4  , 'x': 5  , '9': 6  , 'y': 7  , 'w': 8  , 'J': 9  , 'B': 10 , 
                       'h': 11 , 'r': 12 , 'a': 13 , 'G': 14 , 'L': 15 , 'k': 16 , 'E': 17 , 'S': 18 , 'q': 19 , 'X': 20 , 
                       's': 21 , 'O': 22 , 'M': 23 , '7': 24 , 'l': 25 , '6': 26 , 'v': 27 , 'U': 28 , 'F': 29 , '3': 30 , 
                       'z': 31 , 'V': 32 , 'n': 33 , 't': 34 , 'Z': 35 , 'p': 36 , '0': 37 , 'A': 38 , 'd': 39 , 'c': 40 , 
                       'P': 41 , 'T': 42 , '4': 43 , '5': 44 , 'H': 45 , '2': 46 , 'f': 47 , 'b': 48 , 'Y': 49 , 'W': 50 , 
                       'D': 51 , 'j': 52 , 'u': 53 , 'Q': 54 , 'm': 55 , 'C': 56 , 'K': 57 , 'g': 58 , 'o': 59 , 'I': 60 , 
                       'e': 61 , 'R': 62}   

spindle.reflector_II = {'J': 1  , 'I': 2  , 'F': 3  , 'e': 4  , '4': 5  , 'g': 6  , 'X': 7  , '2': 8  , 'd': 9  , 'W': 10 , 
                        'p': 11 , 'Q': 12 , '8': 13 , 'U': 14 , 'Y': 15 , 'P': 16 , 'n': 17 , 'l': 18 , 'w': 19 , 'u': 20 , 
                        'o': 21 , 't': 22 , '5': 23 , 'k': 24 , 's': 25 , 'a': 26 , '1': 27 , 'z': 28 , 'q': 29 , 'h': 30 , 
                        'r': 31 , 'y': 32 , 'R': 33 , 'S': 34 , 'M': 35 , 'H': 36 , 'j': 37 , 'O': 38 , 'N': 39 , '7': 40 , 
                        'b': 41 , 'K': 42 , 'C': 43 , 'G': 44 , '0': 45 , 'L': 46 , 'B': 47 , 'Z': 48 , '3': 49 , 'i': 50 , 
                        'V': 51 , 'T': 52 , 'f': 53 , 'v': 54 , 'm': 55 , 'D': 56 , 'E': 57 , '6': 58 , 'c': 59 , 'A': 60 , 
                        'x': 61 , '9': 62}


spindle.reflector_III = {'h': 1  , 'C': 2  , 'm': 3  , 'V': 4  , 't': 5  , 'e': 6  , 'z': 7  , 'r': 8  , 'B': 9  , 'k': 10 , 
                         'n': 11 , 'q': 12 , 'Y': 13 , '7': 14 , 's': 15 , 'F': 16 , 'Q': 17 , 'Z': 18 , 'X': 19 , '2': 20 , 
                         'U': 21 , 'l': 22 , 'O': 23 , 'P': 24 , '5': 25 , 'I': 26 , 'H': 27 , '6': 28 , 'j': 29 , 'T': 30 , 
                         'i': 31 , 'd': 32 , 'M': 33 , 'f': 34 , '1': 35 , 'J': 36 , 'D': 37 , 'K': 38 , 'o': 39 , 'S': 40 , 
                         'p': 41 , 'A': 42 , 'R': 43 , 'x': 44 , 'v': 45 , '8': 46 , 'y': 47 , 'b': 48 , '3': 49 , '4': 50 , 
                         'u': 51 , '0': 52 , 'W': 53 , 'g': 54 , 'G': 55 , 'w': 56 , 'c': 57 , 'L': 58 , 'a': 59 , 'E': 60 , 
                         'N': 61 , '9': 62}   

spindle.reflector_IV = {'1': 1  , 'a': 2  , 'j': 3  , '4': 4  , 'e': 5  , 'O': 6  , 'F': 7  , 'y': 8  , 'V': 9  , 'd': 10 , 
                        'n': 11 , 'E': 12 , 'z': 13 , 'c': 14 , '8': 15 , 'k': 16 , '7': 17 , 'Z': 18 , 'i': 19 , 'Y': 20 , 
                        '2': 21 , 'B': 22 , 'J': 23 , '5': 24 , 'u': 25 , '9': 26 , 'H': 27 , 'p': 28 , '0': 29 , 'A': 30 , 
                        'L': 31 , 'x': 32 , 'b': 33 , 't': 34 , 'h': 35 , 'o': 36 , 'S': 37 , '6': 38 , 'l': 39 , 'N': 40 , 
                        'v': 41 , 'U': 42 , 'C': 43 , 'G': 44 , 'T': 45 , 's': 46 , 'K': 47 , 'P': 48 , 'R': 49 , 'M': 50 , 
                        'Q': 51 , 'g': 52 , '3': 53 , 'I': 54 , 'm': 55 , 'W': 56 , 'q': 57 , 'X': 58 , 'r': 59 , 'f': 60 , 
                        'D': 61 , 'w': 62 } 

from time import sleep

print ("Hello there :)")
sleep (1)
name = input ("What is your name? ")
sleep (1)
print ("Nice to meet you " + name.capitalize() + " :)" , "\n")
sleep (1)

alphabet = { "a": 1  , "b": 2  , "c": 3  , "d": 4  , "e": 5  , "f": 6  , "g": 7  , "h": 8  , "i": 9  , "j": 10 , 
             "k": 11 , "l": 12 , "m": 13 , "n": 14 , "o": 15 , "p": 16 , "q": 17 , "r": 18 , "s": 19 , "t": 20 ,
             "u": 21 , "v": 22 , "w": 23 , "x": 24 , "y": 25 , "z": 26 , "A": 27 , "B": 28 , "C": 29 , "D": 30 , 
             "E": 31 , "F": 32 , "G": 33 , "H": 34 , "I": 35 , "J": 36 , "K": 37 , "L": 38 , "M": 39 , "N": 40 , 
             "O": 41 , "P": 42 , "Q": 43 , "R": 44 , "S": 45 , "T": 46 , "U": 47 , "V": 48 , "W": 49 , "X": 50 , 
             "Y": 51 , "Z": 52 , "0": 53 , "1": 54 , "2": 55 , "3": 56 , "4": 57 , "5": 58 , "6": 59 , "7": 60 , 
             "8": 61 , "9": 62}

rotors = []
rot = ""
positions = []
pos = ""
ref = 0
encrypted = []
user_plugboard = []
plug = ""
word = ""

inputs (rot, rotors, pos, positions, ref, user_plugboard)

if (choice == 1):

    for i in range (0,len(message)):

        letter = message[i]
        plugboard_algorithm (user_plugboard)
        rotor (alphabet,letter,rotors,1,1,1)
        reflector (alphabet,letter_2,1)
        rotor (alphabet,letter_3,rotors,2,1,2)
        letter = encrypted[i]
        plugboard_algorithm (user_plugboard)
        encrypted[i] = letter

    for a in range (0,len(encrypted)):

        word = word + encrypted[a]

    print (f"Here is your encrypted word {name.capitalize()}: {word}")    

elif (choice == 2):

    for i in range (0,len(message)):

        letter = message[i]
        plugboard_algorithm (user_plugboard)
        rotor (alphabet,letter,rotors,1,2,1)
        reflector (alphabet,letter_2,2)
        rotor (alphabet,letter_3,rotors,2,2,2)
        letter = encrypted[i]
        plugboard_algorithm (user_plugboard)
        encrypted[i] = letter

    for a in range (0,len(encrypted)):

        word = word + encrypted[a]

    print (f"Here is your decrypted word {name.capitalize()}: {word}")     








