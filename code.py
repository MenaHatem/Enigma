class spindle:

    def __init__(self, rotor_I, rotor_II, rotor_III, rotor_IV, rotor_V, reflector):
    
        self.rotor_I = rotor_I
        self.rotor_II = rotor_II
        self.rotor_III = rotor_III
        self.rotor_IV = rotor_IV
        self.rotor_V = rotor_V
        self.reflector = reflector

def inputs (r, rotor, p, position):

    i = 0
    global message
    number = ["first" , "second" , "third"]

    # for i in range (0,3):

    #     while (r != "I" or r != "II" or r != "III" or r != "IV" or r != "V"):

    #         print ("I, II, III, IV, V" , "\n")
    #         #sleep (0.5)
    #         r = str (input ("Please choose your " + number[i] + " rotor: "))
    #         r = r.upper()
    #         print ("\n")
    #         #sleep (0.5)

    #         if (r == "I" or r == "II" or r == "III" or r == "IV" or r == "V"):

    #             rotor.append(r)
    #             break

    #         else:

    #             print ("Incorrect choice")
    #             #sleep (0.5)
    #             print ("Please try again" , "\n")
    #             #sleep (0.5)   

    # for i in range (1,4):

    #     print ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z" , "\n")
    #     #sleep (0.5)
    #     cond = []

    #     while (cond == [] or len(cond) != 1):

    #         p = input (f"Choose the position of rotor {i} by writing the letter: ").lower()
    #         print ("\n")
    #         cond = findall("[a-z]" , p) 
            
    #         if (cond != [] and len(cond) == 1):

    #             position.append(p)
    #             #sleep (0.5)

    #         else:

    #             print ("Choose one of the alphabet letters")
    #             #sleep (0.5)
    #             print ("Please try again" , "\n")
    #             #sleep (0.5)
 
    # print ("You are now going to enter each plugboard setting as follows")
    # # sleep (0.5)
    # print ("Example: ab, cd, etc..." , "\n")
    # # sleep (0.5)
    
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
                           
    # message = input ("Please enter your message: ")
    # #message = list (message)
    # # sleep (0.5)

def plugboard_algorithm (user):

    global letter

    plugboard_1 = []
    plugboard_2 = []

    for x in range (0,len(user)):

        plugboard_1.append(user[x][0])
        plugboard_2.append(user[x][1])

    for i in range (0,len(plugboard_1)):

        if (letter == plugboard_1[i]):

            print (plugboard_1[i])
            letter = plugboard_2[i]
            print(letter)

        elif (letter == plugboard_2[i]):

            print (plugboard_2[i])
            letter = plugboard_1[i]
            print(letter)

    print (plugboard_1)
    print (plugboard_2)

def rotor (alphabets,letter,rotor_1,rotor_2,rotor_3,option):

    place = 0
    global letter_2
 
    place = alphabets[letter] - 1
    print (place)

    letter = rotor_1[place]
    print (rotor_1[place])
    print ("---------------------------")

    place = alphabets[letter] - 1
    print (place)

    letter = rotor_2[place]
    print (rotor_2[place])
    print ("---------------------------")

    if (option == 1):

        place = alphabets[letter] - 1
        print (place)

        letter_2 = rotor_3[place]
        print (letter_2)
        print ("---------------------------")

    elif (option == 2):

        place = alphabets[letter] - 1
        print (place)

        letter_3 = rotor_3[place]
        print (letter_3)
        print ("---------------------------")
        encrypted.append(letter_3)

def reflector (alphabets,letter,ref):

    global letter_3

    place = alphabets[letter] - 1
    print (place)

    letter_3 = ref[place]
    print (letter_3)
    print ("---------------------------")
        

        





spindle.rotor_I = ['c', 'i', 'm', 'f', 'z', 'g', 's', 'b', 'v', 'd', 'p', 't', 'w', 'k', 'r', 'u', 'y', 'q', 'l', 'a', 'e', 'x', 'j', 'n', 'o', 'h']
spindle.rotor_II = ['r', 'n', 'd', 'o', 'x', 'u', 'p', 'q', 'a', 'f', 'k', 'c', 'l', 'b', 's', 'i', 'j', 'h', 't', 'z', 'y', 'v', 'm', 'e', 'g', 'w']
spindle.rotor_III = ['y', 'h', 'k', 'q', 'd', 'z', 'n', 'f', 'v', 's', 'b', 'x', 'o', 'l', 'c', 'a', 'g', 'i', 'p', 'u', 't', 'j', 'w', 'r', 'm', 'e']
spindle.rotor_IV = ['a', 'q', 's', 'x', 'b', 'k', 'r', 'd', 'y', 'm', 'v', 'g', 'o', 'j', 'c', 't', 'i', 'e', 'p', 'l', 'h', 'n', 'w', 'z', 'u', 'f']
spindle.rotor_V = ['n', 'p', 'h', 'x', 'e', 'd', 'r', 'f', 'l', 'z', 'm', 'w', 'j', 'c', 'a', 'b', 't', 'y', 'o', 'i', 'v', 'q', 'g', 's', 'k', 'u']      
spindle.reflector = ['o', 'l', 'i', 'c', 't', 'x', 'y', 'e', 'j', 'z', 'f', 'n', 'w', 'b', 'p', 's', 'h', 'q', 'u', 'd', 'm', 'g', 'k', 'a', 'v', 'r']

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

rotors = []
rot = ""
positions = []
pos = ""
encrypted = []
user_plugboard = []
plug = ""

inputs (rot, rotors, pos, positions)

for i in range (0,len(message)):

    letter = message[i]
    plugboard_algorithm (user_plugboard)
    rotor (alphabet,letter,spindle.rotor_I,spindle.rotor_II,spindle.rotor_III,1)
    reflector (alphabet,letter_2,spindle.reflector)
    rotor (alphabet,letter_3,spindle.rotor_III,spindle.rotor_II,spindle.rotor_I,2)
    letter = encrypted[i]
    plugboard_algorithm (user_plugboard)
    encrypted[i] = letter

print(encrypted)








