# -*- coding: utf-8 -*-

#In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
#
#NOTE: String letters are case-sensitive.

def count_substring(string, sub_string):
    sub_length = len(sub_string) #3
    count = 0
    for i in range(0, len(string)):
        slice1 = string[i:i+sub_length]
        if slice1 == sub_string:
            count += 1
    return count

