# References: https://www.geeksforgeeks.org/converting-arabicArray-number-lying-between-1-to-3999-to-roman-numerals/


arabicArray = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
romanNumeralArray = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]

def arabicToRoman(userInput):
    if type(userInput) != int:
        print("Invalid number, userInput a positive integer.")
        return ''
    if int(userInput) > 4999:
        print("Too big a number for the romanNumeralArray")
        return ''


    romanNumberResult = ''
    index = len(arabicArray) - 1

    while userInput:
        temp = int(userInput / arabicArray[index])
        userInput = userInput % arabicArray[index]
        
        while temp:
            temp = temp - 1
            romanNumberResult = romanNumberResult + romanNumeralArray[index]
        
        index = index - 1
    return romanNumberResult