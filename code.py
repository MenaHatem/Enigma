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

def inputs (r, rotor, p, position, ref):

    i = 0
    c = 0
    global choice
    global message
    global refl
    number = ["first" , "second" , "third"]
    numbers = ["0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]

    while (c != 1 or c != 2):

        try:

            # print ("1. Encrypt a message" , "\n")
            # #sleep (0.5)
            # print ("2. Decrypt a message" , "\n")
            # #sleep (0.5)
            c = int (input ("Please choose an option from above: "))
            print ("\n")   
            #sleep (0.5)

            if (c == 1 or c == 2):

                choice = c
                break

            else:

                print ("Choose either 1 or 2 ")
                #sleep (0.5)
                print ("Please try again" , "\n")
                #sleep (0.5)

        except ValueError:

            print ("Choose either 1 or 2 ")
            #sleep (0.5)
            print ("Please try again" , "\n")
            #sleep (0.5)

    for i in range (0,3):

        while (r != "I" or r != "II" or r != "III" or r != "IV" or r != "V"):

            print ("I, II, III, IV, V" , "\n")
            #sleep (0.5)
            r = str (input ("Please choose your " + number[i] + " rotor: "))
            r = r.upper()
            print ("\n")
            #sleep (0.5)

            if (r == "I" or r == "II" or r == "III" or r == "IV" or r == "V"):

                rotor.append(r)
                break

            else:

                print ("Incorrect choice")
                #sleep (0.5)
                print ("Please try again" , "\n")
                #sleep (0.5)   

    for i in range (1,4):

        print ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z" , "\n")
        #sleep (0.5)
        cond = []

        while (cond == [] or len(cond) != 1):

            p = input (f"Choose the position of rotor {i} by writing the letter: ").lower()
            print ("\n")
            cond = findall("[a-z]" , p) 
            
            if (cond != [] and len(cond) == 1):

                position.append(p)
                #sleep (0.5)

            else:

                print ("Choose one of the alphabet letters")
                #sleep (0.5)
                print ("Please try again" , "\n")
                #sleep (0.5)
 
    print ("You are now going to enter the 13 plugboard settings as follows")
    # sleep (0.5)
    print ("Example: ab, cd, etc..." , "\n")
    # sleep (0.5)
    
    for g in range (1,4):

        cond = []

        while (cond == [] or len(cond) != 2 or cond[0] == cond[1]):

            plug = input (f"Plugboard setting number {g}: ").lower()
            print ("\n")
            cond = findall("[a-z]" , plug)
            # sleep (0.5)

            if (len(cond) == 2):

                if (cond[0] == cond[1]):

                    print ("Do not repeat letters")
                    #sleep (0.5)
                    print ("Please try again" , "\n")
                    #sleep (0.5)

                else:

                    user_plugboard.append(plug)
                    #sleep (0.5)

            else:

                print ("Choose one of the alphabet letters")
                #sleep (0.5)
                print ("Please try again" , "\n")
                #sleep (0.5)

    while (ref != 1 or ref != 2 or ref != 3 or ref != 4):

        try:

            # print ("1. Reflector B")
            # #sleep (0.5)
            # print ("2. Reflector B thin")
            # #sleep (0.5)
            # print ("3. Reflector C")
            # #sleep (0.5)
            # print ("4. Reflector C thin" , "\n")
            # #sleep (0.5)
            ref = int (input ("Please choose your reflector: "))
            print ("\n")   
            #sleep (0.5)

            if (ref >= 1 and ref <= 4):

                break

            else:

                print ("A number from 1 to 4 is only allowed")
                #sleep (0.5)
                print ("Please try again" , "\n")
                #sleep (0.5)

        except ValueError:

            print ("A number from 1 to 4 is only allowed")
            #sleep (0.5)
            print ("Please try again" , "\n")
            #sleep (0.5)
                     
    if (ref == 1):

        refl = spindle.reflector_I

    elif (ref == 2):

        refl = spindle.reflector_II

    elif (ref == 3):

        refl = spindle.reflector_III

    elif (ref == 4):

        refl = spindle.reflector_IV
    
    message = input ("Please enter your message: ")

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

    for i in range (0,len(rotors)):

        if (rotors[i] == "I"):

            rotors[i] = spindle.rotor_I 

        elif (rotors[i] == "II"):

            rotors[i] = spindle.rotor_II

        elif (rotors[i] == "III"):

            rotors[i] = spindle.rotor_III 

        elif (rotors[i] == "IV"):

            rotors[i] = spindle.rotor_IV

        elif (rotors[i] == "V"):

            rotors[i] = spindle.rotor_V

    if (order == 1):

        rotor_1 = rotors[0]
        rotor_2 = rotors[1]
        rotor_3 = rotors[2]

    elif (order == 2):

        rotor_1 = rotors[2]
        rotor_2 = rotors[1]
        rotor_3 = rotors[0]

    print(letter)
    place = 0
    global letter_2
 
    if (option_1 == 1):

        place = alphabets[letter]
        print (place)

        for i in rotor_1:

            if (place == rotor_1[i]):

                letter = i
                print (i)
                print ("---------------------------")

        place = alphabets[letter]
        print (place)

        for i in rotor_2:

            if (place == rotor_2[i]):

                letter = i
                print (i)
                print ("---------------------------")

        if (option_2 == 1):

            place = alphabets[letter]
            print (place)

            for i in rotor_3:

                if (place == rotor_3[i]):

                    letter_2 = i
                    print (i)
                    print ("---------------------------")

        elif (option_2 == 2):

            place = alphabets[letter]
            print (place)

            for i in rotor_3:

                if (place == rotor_3[i]):

                    letter_3 = i
                    print (i)
                    print ("---------------------------")
                    encrypted.append(letter_3)

    elif (option_1 == 2):

        print (letter)
        place = rotor_1[letter]
        print (place)

        for i in alphabets:

            if (place == alphabets[i]):

                letter = i
                print (i)
                print ("---------------------------")

        place = rotor_2[letter]
        print (place)

        for i in alphabets:

            if (place == alphabets[i]):

                letter = i
                print (i)
                print ("---------------------------")

        if (option_2 == 1):

            place = rotor_3[letter]
            print (place)

            for i in alphabets:

                if (place == alphabets[i]):

                    letter_2 = i
                    print (i)
                    print ("---------------------------")

        elif (option_2 == 2):

            place = rotor_3[letter]
            print (place)

            for i in alphabets:

                if (place == alphabets[i]):

                    letter_3 = i
                    print (i)
                    print ("---------------------------")
                    encrypted.append(letter_3)

def reflector (alphabets,letter,option):

    global letter_3

    if (option == 1):

        place = alphabets[letter] 
        print (place)

        for i in refl:

            if (place == refl[i]):

                letter_3 = i
                print (letter_3)
                print ("---------------------------")

    elif (option == 2):

        place = refl[letter] 
        print (place)

        for i in alphabets:

            if (place == alphabets[i]):

                letter_3 = i
                print (letter_3)
                print ("---------------------------")
 
        
spindle.rotor_I = { "c": 1 , "i": 2 , "m": 3 , "f": 4 , "z": 5 , "g": 6 , "s": 7 , "b": 8 , "v": 9 , "d": 10 , 
                    "p": 11 , "t": 12 , "w": 13 , "k": 14 , "r": 15 , "u": 16 , "y": 17 , "q": 18 , "l": 19 , "a": 20 ,
                    "e": 21 , "x": 22 , "j": 23 , "n": 24 , "o": 25 , "h": 26 }

spindle.rotor_II = { "r": 1 , "n": 2 , "d": 3 , "o": 4 , "x": 5 , "u": 6 , "p": 7 , "q": 8 , "a": 9 , "f": 10 , 
                     "k": 11 , "c": 12 , "l": 13 , "b": 14 , "s": 15 , "i": 16 , "j": 17 , "h": 18 , "t": 19 , "z": 20 ,
                     "y": 21 , "v": 22 , "m": 23 , "e": 24 , "g": 25 , "w": 26 }

spindle.rotor_III = { "y": 1 , "h": 2 , "k": 3 , "q": 4 , "d": 5 , "z": 6 , "n": 7 , "f": 8 , "v": 9 , "s": 10 , 
                      "b": 11 , "x": 12 , "o": 13 , "l": 14 , "c": 15 , "a": 16 , "g": 17 , "i": 18 , "p": 19 , "u": 20 ,
                      "t": 21 , "j": 22 , "w": 23 , "r": 24 , "m": 25 , "e": 26 }

spindle.rotor_IV = { "a": 1 , "q": 2 , "s": 3 , "x": 4 , "b": 5 , "k": 6 , "r": 7 , "d": 8 , "y": 9 , "m": 10 , 
                     "v": 11 , "g": 12 , "o": 13 , "j": 14 , "c": 15 , "t": 16 , "i": 17 , "e": 18 , "p": 19 , "l": 20 ,
                     "h": 21 , "n": 22 , "w": 23 , "z": 24 , "u": 25 , "f": 26 }

spindle.rotor_V = { "n": 1 , "p": 2 , "h": 3 , "x": 4 , "e": 5 , "d": 6 , "r": 7 , "f": 8 , "l": 9 , "z": 10 , 
                    "m": 11 , "w": 12 , "j": 13 , "c": 14 , "a": 15 , "b": 16 , "t": 17 , "y": 18 , "o": 19 , "i": 20 ,
                    "v": 21 , "q": 22 , "g": 23 , "s": 24 , "k": 25 , "u": 26 }

spindle.reflector_I = { "o": 1 , "l": 2 , "i": 3 , "c": 4 , "t": 5 , "x": 6 , "y": 7 , "e": 8 , "j": 9 , "z": 10 , 
                      "f": 11 , "n": 12 , "w": 13 , "b": 14 , "p": 15 , "s": 16 , "h": 17 , "q": 18 , "u": 19 , "d": 20 ,
                      "m": 21 , "g": 22 , "k": 23 , "a": 24 , "v": 25 , "r": 26 }

spindle.reflector_II = { "m": 1 , "k": 2 , "v": 3 , "y": 4 , "b": 5 , "r": 6 , "e": 7 , "g": 8 , "t": 9 , "x": 10 , 
                         "a": 11 , "w": 12 , "q": 13 , "i": 14 , "l": 15 , "d": 16 , "c": 17 , "n": 18 , "j": 19 , "p": 20 ,
                         "s": 21 , "f": 22 , "o": 23 , "h": 24 , "z": 25 , "u": 26 }

spindle.reflector_III = { "v": 1 , "l": 2 , "c": 3 , "o": 4 , "m": 5 , "u": 6 , "z": 7 , "h": 8 , "s": 9 , "q": 10 , 
                          "n": 11 , "e": 12 , "y": 13 , "j": 14 , "g": 15 , "p": 16 , "r": 17 , "x": 18 , "d": 19 , "a": 20 ,
                          "k": 21 , "w": 22 , "b": 23 , "i": 24 , "t": 25 , "f": 26 }

spindle.reflector_IV = { "p": 1 , "m": 2 , "d": 3 , "g": 4 , "o": 5 , "h": 6 , "t": 7 , "w": 8 , "a": 9 , "v": 10 , 
                         "e": 11 , "i": 12 , "x": 13 , "y": 14 , "k": 15 , "l": 16 , "r": 17 , "z": 18 , "u": 19 , "n": 20 ,
                         "f": 21 , "q": 22 , "j": 23 , "b": 24 , "c": 25 , "s": 26 }

from time import sleep
from re import findall

#print ("Hello there :)")
#sleep (0.5)
#name = input ("What is your name? ")
#sleep (0.5)
#print ("Nice to meet you " + name.capitalize() + " :)" , "\n")
#sleep (0.5)

alphabet = { "a": 1 , "b": 2 , "c": 3 , "d": 4 , "e": 5 , "f": 6 , "g": 7 , "h": 8 , "i": 9 , "j": 10 , 
             "k": 11 , "l": 12 , "m": 13 , "n": 14 , "o": 15 , "p": 16 , "q": 17 , "r": 18 , "s": 19 , "t": 20 ,
             "u": 21 , "v": 22 , "w": 23 , "x": 24 , "y": 25 , "z": 26 }

#choice = 0
rotors = []
rot = ""
positions = []
pos = ""
special_before = []
special_after = []
special_letter = ""
ref = 0
encrypted = []
user_plugboard = []
plug = ""

inputs (rot, rotors, pos, positions, ref)

if (choice == 1):

    for i in range (0,len(message)):

        print ("ENCRYPTION")
        letter = message[i]
        plugboard_algorithm (user_plugboard)
        rotor (alphabet,letter,rotors,1,1,1)
        reflector (alphabet,letter_2,1)
        rotor (alphabet,letter_3,rotors,2,1,2)
        letter = encrypted[i]
        plugboard_algorithm (user_plugboard)
        encrypted[i] = letter

    print(encrypted)

elif (choice == 2):

    for i in range (0,len(message)):

        print ("DECRYPTION")
        letter = message[i]
        plugboard_algorithm (user_plugboard)
        rotor (alphabet,letter,rotors,1,2,1)
        reflector (alphabet,letter_2,2)
        rotor (alphabet,letter_3,rotors,2,2,2)
        letter = encrypted[i]
        plugboard_algorithm (user_plugboard)
        encrypted[i] = letter

    print(encrypted)








