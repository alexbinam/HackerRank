# -*- coding: utf-8 -*-

#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
#
#For Example:
#
#Www.HackerRank.com → wWW.hACKERrANK.COM
#Pythonist 2 → pYTHONIST 2

def swap_case(s):
    temp = ""
    for i in s:
        if i.islower():
            temp += i.upper()
        elif i.isupper():
            temp += i.lower()
        elif i == ' ':
            temp+= i
        elif i.isnumeric:
            temp += i
    return temp