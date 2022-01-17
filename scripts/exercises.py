#!/usr/bin/env python3



def reverseWords(s):

    def reverseWord(word):
        new_word = ""
        
        for i in range(len(word) - 1, -1, -1):
            new_word += word[i]
        return new_word
    
    output = "" 
    for el in s.split(" "):
        if el[-1] in ['.', ',', ':', ';']:
            output += reverseWord(el[:-1])
            output += el[-1]
        
        else:
            output += reverseWord(el)

        if el != s.split(" ")[-1]:
            output += ' '

    return output


def printthepattern(pattern):

    final = []
    for el in range(pattern, 0, -1):
        for el2 in range(pattern, 0, -1):
            final.append([el2] * el)
        final.append(['$'])

    return [item for sublist in final for item in sublist]

    


if __name__ == '__main__':
    print(reverseWords("Hello, John"))

    print(printthepattern(3))
