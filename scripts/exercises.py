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


def partition(arr, low, high):
    i = (low-1) 
    pivot = arr[high]   

    for j in range(low, high):

        if arr[j] <= pivot:

            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[high] = arr[high], arr[i+1]
    
    return (i+1)
    

def quickSort(arr, low, high):

    if len(arr) == 1:
        return arr

    if low < high:

        pi = partition(arr, low, high)

        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 


if __name__ == '__main__':
    print(reverseWords("Hello, John"))

    print(printthepattern(3))

    arr = [10, 7, 5, 3, 2, 4]
    n = len(arr)
    print(quickSort(arr, 0, n-1))

    
