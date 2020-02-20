

def arabicToRoman(input):
    if type(input) != int: # error checking for other input types, like string
        print("Invalid number, input a positive integer.")
        return ''
    if int(input) > 4999: # error checking for edge cases of Roman Numerals
        print("Too big a number for the Romans")
        return ''

    str_input = str(input)
    return _arabicToRoman(str_input, len(str_input))


def _arabicToRoman(input, length): # recursive function
    if length == 0: # empty input
        return ''
    
    if length == 1: # base cases
        if input[0] == '9':
            return 'IX'
        elif input[0] >= '5':
            return 'V' + ('I'*(int(input[0])-5)) # roman number if arabic number is >=5
        elif input[0] == '4': # roman number if arabic number is 4
            return 'I' + 'V'
        elif input[0] > '0': # roman number if arabic number is > 0 but less than 4
            return 'I'*int(input[0])
        else:
            return _arabicToRoman(input[1:], length-1) # keep recursing the _arabicToRoman function until input length is 1
    
    elif length == 2: # keep recursing the _arabicToRoman function until input length is 1
        if input[0] == '9':
            return 'XC' + _arabicToRoman(input[1:], length-1)
        elif input[0] >= '5':
            correctInput = int(input[0])-5
            recursiveCall = _arabicToRoman(input[1:], length-1)
            return 'L' + ('X' * correctInput) + recursiveCall
        elif input[0] == '4':
            return 'X' + 'L' + _arabicToRoman(input[1:], length-1) # keep recursing the _arabicToRoman function until input length is 1
        elif input[0] > '0':
            return 'X'*int(input[0]) + _arabicToRoman(input[1:], length-1) # roman number for most significant arabic number + smaller arabic numbers that still need to be converted
        else:
            return _arabicToRoman(input[1:], length-1) # keep recursing the _arabicToRoman function until input length is 1
    
    elif length == 3: # keep recursing the _arabicToRoman function until input length is 1
        if input[0] == '9':
            return 'CM' + _arabicToRoman(input[1:], length-1) # roman number for most significant arabic number + smaller arabic numbers that still need to be converted
        elif input[0] >= '5':
            correctInput = int(input[0])-5
            recursiveCall = _arabicToRoman(input[1:], length-1)
            return 'D' + ('C' * correctInput) + recursiveCall # roman number for most significant arabic number + smaller arabic numbers that still need to be converted
        elif input[0] == '4':
            return 'C' + 'D' + _arabicToRoman(input[1:], length-1)
        elif input[0] > '0':
            return 'C'*int(input[0]) + _arabicToRoman(input[1:], length-1)
        else:
            return _arabicToRoman(input[1:], length-1)

    elif length == 4 and input[0]:
        return 'M' * int(input[0]) + _arabicToRoman(input[1:], length-1)
    
    else: # length is too big
        return 'Sorry, try again!'


#print(arabicToRoman(4999))
