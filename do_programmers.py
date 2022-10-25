from fractions import Fraction
import numpy as np
import math
print("a")


class programmers:
#1
    def plus(num1, num2):
        answer = num1 + num2 
        return answer 
    
    def compare_zahl(num1, num2):
        if num1 == num2:
            answer = 1
        else: answer = -1
        return answer 

    def minus(num1, num2):
        answer = num1 - num2
        return answer

    def multi(num1, num2):
        answer = num1 * num2
        return answer
    
    def Quotient(num1, num2):
        answer = int(num1/num2)
        return answer

    def Rest(num1, num2):
        answer = num1 % num2
        return answer
#2
    def Durchschnittswert_des_Arrays(numbers):
        sum = 0
        for i in range(len(numbers)):
            sum = sum + numbers[i]
        answer = sum / len(numbers)
        return answer
#3
    def Anzahl_Duplikate(array, n):
        answer = 0
        for i in range(len(array)):
            if array[i] == n:
                answer += 1
        return answer

#4
    def  Summe_gerader_Zahlen(n):
        answer = 0
        list = []
        for i in range(n+1):
            if i%2 == 0:
                list.append(i)
        for i in range(len(list)):
            answer = answer + list[i]
        return answer

#5
    def Bruch_Summe(denum1, num1, denum2, dnum2):
        answer = []
        a = Fraction(denum1, num1)
        b = Fraction(denum2, num2)
        c = a+b
        answer.append(c.numerator)
        answer.append(c.denominator)
        return answer

#6 
    def Medianwert(array):
        answer = int(np.median(array))
        return answer

#7 
    def Doppel_Array(numbers):
        for i in range(len(numbers)):
            numbers[i] = numbers[i] * 2
            answer = numbers
        return answer
    
#8 
    def Vergleich_Array(array, number):
        answer = 0
        for i in range(len(array)):
            if number < array[i]:
                answer += 1 
        return answer

#test code
if __name__ == "__main__":
    '''
    #1
    num1 = 1
    num2 = 2
    print("plus beispiel>>> num1 = %s, num2 = %s, num1 + num2 = %s" %(num1, num2, programmers.plus(num1,num2)))
    print("compare_zahl : %s" %(programmers.compare_zahl(num1, num2)))
    print(programmers.Rest(num1, num2))
    '''
    
    '''
    #2
    numbers = [1,2,3,4,5,6,7,8,9,10]
    print(programmers.Durchschnittswert_des_Arrays(numbers))
    '''

    '''
    #3
    array = [1,2,2,2,2,3,4]
    n = 2
    print(programmers.Anzahl_Duplikate(array, n))
    '''
    '''
    #4
    n = 10
    print(programmers.Summe_gerader_Zahlen(n))
    '''

    '''
    #5
    denum1 = 1
    num1 = 2
    denum2 = 3
    num2 = 4
    print(programmers.Bruch_Summe(denum1, num1, denum2, num2))
    '''
    
    #6 #7 #8
    array = [1,2,3,4,6]
    number = 4
    print(programmers.Medianwert(array))
    print(programmers.Doppel_Array(array))
    print(programmers.Vergleich_Array(array, number))

