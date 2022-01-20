#!/usr/bin/env python3
import numpy as np


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


def multiplication_table(number):
    return [number*i for i in range(11)]


def pallindrome_sum(num):
    total = 0
    for el in str(num): 
        total += int(el)

    if str(total) == str(total)[::-1]:
        return 1
    else:
        return 0


def reverse_digits(num):
    return int(str(num)[::-1])


def closest_number(N, M):
    if (N / M - np.floor(N / M)) > (np.ceil(N / M) - N / M):
        return int(np.ceil(N / M) * M)

    elif (N / M - np.floor(N / M)) < (np.ceil(N / M) - N / M):
        return int(np.floor(N/M) * M)
    else:
        if (N < 0 and M > 0) or (N > 0 and M < 0): 
            return int(np.floor(N/M) * M)
        else:
            return int(np.ceil(N / M) * M)


def factorial(N):
    result = 1
    for el in range(1, N + 1):
        result *= el
    return result


def largestPrimeFactor(N):

    def test_candidates(cand):
        primes = [1]
        for el in cand:
            for k in range(int(el/2), 0, -1):

                if k == 1:
                    primes.append(el)
                else:
                    if el % k == 0:
                        break

        return max(primes)

    cands = [N]
    for i in range(2, int(N/2) + 1): 
        if N % i == 0:
            cands.append(i)
            
    
    return test_candidates(cands)


def maxStock(A, n):
    
    keep = []; maxis = 0
    for i in range(n):
        for k in range(i + 1, n):
            profit = A[k] - A[i]

            if profit > 0: 
                if profit == maxis: 
                    keep.append((i, k))
                    maxis = profit

                elif profit > maxis:

                    if len(keep) >= 1:
                        for kept in keep:
                            if i <= kept[1]:
                                maxis = profit
                                keep = [(i,k)]
                            else:
                                maxis = profit + maxis
                                keep.append((i,k))
                            import pdb; pdb.set_trace()
                    else: 
                        maxis = profit
                        keep = [(i,k)]
                    # maxis = profit 
                    

                # import pdb;pdb.set_trace()
    import pdb; pdb.set_trace()


def maxStock2(A, n):
    
    profit = 0; attention = []
    
    for i in range(n):
        for k in range(i + 1, n):
            profit = A[k] - A[i]

            if profit < 0: 

                if k not in attention:
                    attention.append(k)
                    # if len(attention) == 0:
                    #     attention.append(k)
                    # else:
                    #     if k < min(attention):
                    #         attention.append(k)
                    #     else:
                    #         import pdb;pdb.set_trace()
                    
    attention.append(n)
    attention = [0] + attention
    keep = []; keep_all = []; all_profit = 0; maxis = 0
    import pdb;pdb.set_trace()
    for l in range(1, len(attention)):
        profit = 0

        for i in range(attention[l-1], attention[l], 1):
            for k in range(i + 1, attention[l]):

                profit = A[k] - A[i]
                if profit > 0:
                    if profit == maxis: 
                        keep.append((i, k))
                        maxis = profit

                    elif profit > maxis:
                        maxis = profit 
                        keep = [(i,k)]
                    

        all_profit += maxis

        for el in keep:
            keep_all.append(el)
    
    return list(set(keep_all))
                


if __name__ == '__main__':
    # print(reverseWords("Hello, John"))

    # print(printthepattern(3))

    # arr = [10, 7, 5, 3, 2, 4]
    # quickSort(arr, 0, len(arr)-1)
    # print(arr)

    # print(multiplication_table(9))
    # print(pallindrome_sum(75))
    # print(reverse_digits(122))

    # print(closest_number(15, -6))
    # print(factorial(4))
    # print(largestPrimeFactor(97))
    print(maxStock2([11,42,49,96,23,20,49,26,26,18,73,2,53,59,34,99,25,2], 18))

