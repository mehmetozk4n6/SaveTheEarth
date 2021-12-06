#------------------------------------------------------------#
# Student Name: Mehmet ÖZKAN 
# Student ID: 
# BBM103 Introduction to Programming Laboratory I, Fall 2016 
# Assignment 3: Mission: Save the Earth
#------------------------------------------------------------#

# Importing the sys module that supports reading command-line arguments
from os import linesep
import sys


#-------------------------------------------------#
#                   Functions                     #
#-------------------------------------------------#

def read_dictionary(file_handle):
    """This function reads a text file with
       Binarian-English Dictionary, and returns it
       as a dictionary data structure, where keys
       are words in Binarian, and values are their
       English counterparts."""
    dictionary = {}
    with open(file_handle,"r") as file:
        dicitonarylist = file.readlines()
        for i in dicitonarylist:
            line = i.strip("\n")
            line = line.split(" ")
            value = line[0]
            key = line[1]
            dictionary[value] = key
    return dictionary 

def binarian_to_english(text):
    """This function translates a text in Binarian
       language to English and returns the translation."""
    astrophysicaldata = []
    metada = []
    data = []
    with open(text,"r") as file:
        binariantext = file.readlines()
    for n in binariantext:
        n = n.strip("\n")
        if n.startswith("+"):
            translator(astrophysicaldata,n,dic)
        elif n.startswith("#"):
            translator(metada,n,dic)
        else:
            translator(data,n,dic)
    return astrophysicaldata,metada,data

def translator(c,n,e):
    b = n.strip("+# ").split(" ")   
    for v in b:
        v = v.strip(",\n")
        if v in e:
            c.append(e[v])
        else:
            c.append(v)
    c.append("\n")

def english_to_binarian(text):
    """This function translates a text in English
       language to Binarian and returns the translation."""
    with open(text,"r") as file:
        message = file.read()
    bin_mess_text = []
    message_text = ""
    message = message.lower()
    messagesentences = message.split(".")
    for linewords in messagesentences:
        linewords = linewords.strip(".")
        translator(bin_mess_text,linewords,dic_eng_to_binarians)
    nub = 0
    for n in bin_mess_text:
        try:
            n = int(n)
            bin_mess_text[nub] = decimal_to_binary(n)
        except:
            pass
        nub += 1
    loadtext("message.txt",bin_mess_text)

def binary_to_decimal(number):
    """This function takes a binary number as input
       and returns its decimal value."""
    num = 0
    for i in number:
        try:
            i = int(i)
            a = bintodeci(i)
            number[num] = str(a)
        except:
            pass
        num += 1
    lightyearindex = number.index('light-years')
    lightyear = int(number[lightyearindex-1])
    dist_km = ly_to_km(lightyear)
    number[lightyearindex-1] = str(dist_km)
    number[lightyearindex] = "km"
    return number

def bintodeci(numb):
    numb = str(numb)
    len1 = len(numb)
    bin = 0
    num = 0
    while len1>0:
        len1 -=1
        bin += int(numb[num]) * (2**len1)
        num += 1
    return bin

def decimal_to_binary(number):
    """This function takes a decimal number as input
       and returns its binary value."""
    number = 53
    kalan = []
    while number > 2 :
        number = number / 2
        onezero = (number - int(number))*2 
        kalan.append(str(int(onezero)))
    kalan.append(str(int(number)))
    kalan = kalan[::-1]
    bin_num = ""
    for i in kalan:
        bin_num += i
    return bin_num

def ly_to_km(distance):
    """This function takes a distance in light-years
       and returns its value in kilometers."""
    km = distance*(9.4607e+12)
    return km

def loadtext(filename,text:list,c = "continue"):
    file =  open(filename,"w")
    if c == "capitalize":
        astrotext = "Data about Binarian planet:\n"
    else:
        astrotext = ""
    for i in text:
        if i == "\n":
            astrotext += i
        else:
            if c == "capitalize":    
                astrotext += i.capitalize() + " "
            else:
                astrotext += i + " "
    file.write(astrotext)
    file.close()

def dicconvertor(dictionary):
    dictionary1 = {}
    for i in dictionary:
        key = i
        value = dictionary[i]
        dictionary1[value] = key
    return dictionary1

result = "dictionary.txt"
dic = read_dictionary(result)
result1 = "binarian_transmission.txt"
i = binarian_to_english(result1)
astrophysicaldata1 = i[0]
metada1 = i[1]
data1 = i[2]
astrophysicaldata2 = binary_to_decimal(astrophysicaldata1)
loadtext("computations.txt",astrophysicaldata2,"capitalize")
dic_eng_to_binarians = dicconvertor(dic)
result2 = "peace_message.txt"
tobinarian_mes = english_to_binarian(result2)
with open("computations.txt","r") as file:
    a = file.read()
    print(a)

with open("message.txt","r") as file:
    a = file.read()
    print(a)




#-------------------------------------------------#
#                 Main Program                    #
#-------------------------------------------------#


############ Your code goes here ##################


# A couple of suggestions for starting:

#   1. Do not panic! This assignment is much easier than it seems. Trust me!
#   2. Take a deep breath and start with the simplest tasks first:
#       - read the input files and print them out to see if you are reading them correctly.
#   3. Store the contents of dictionary.txt in a dictionary data structure and try
#      accessing some of its elements.
#   4. Think about how you can use your dictionary to translate the message once you extract it.
#   5. Think about what you need to consider when extracting the message from the jumbled transmission:
#       - How will you check if a line starts with a special character or not?
#       - Try extraxcting relevant lines and printing them to check if you are doing it correctly.
#       - Once you have the relevant lines, think about how you will translate them word-by-word
#         using your dictionary.
#   6. Once you get started, it will get easier. Do one step at a time and check your results at each step.
#   7. Do not try to code everything at once hoping it will work in the end. In most cases, it will not. 
#	   Instead, divide your work into smaller independent parts which you will test separately.

#   I want everyone to try and complete this assignment. Even if it seems too hard for you at first,
#   I want you to get started and do as much as you can. When you get stuck, ask for advice on how to proceed.
#   The most important thing is that you believe that you can do this. If you work on the assignment
#   every day for at least 30 minutes, you will make progress fast. So don't wait until the last week to start.
#   Start now! Try to enjoy solving this to keep yourself motivated. And trust me when I tell you that:
#   YOU CAN DO THIS!
#   You just need to work on it.
#   Good luck! :)

