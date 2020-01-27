

def arabicToRoman(input):
    if type(input) != int:
        print("Invalid number, input a positive integer.")
        return ''
    if int(input) > 4999:
        print("Too big a number for the Romans")
        return ''

    str_input = str(input)
    return _arabicToRoman(str_input, len(str_input))


def _arabicToRoman(input, length):
    if length == 0:
        return ''
    if length == 1:
        if input[0] == '9':
            return 'IX'
        elif input[0] >= '5':
            return 'V' + ('I'*(int(input[0])-5))
        elif input[0] == '4':
            return 'I' + 'V'
        elif input[0] > '0':
            return 'I'*int(input[0])
        else:
            return _arabicToRoman(input[1:], length-1)
    elif length == 4 and input[0]:
        return 'M' * int(input[0]) + _arabicToRoman(input[1:], length-1)
    elif length == 3:
        if input[0] == '9':
            return 'CM' + _arabicToRoman(input[1:], length-1)
        elif input[0] >= '5':
            correctInput = int(input[0])-5
            recursiveCall = _arabicToRoman(input[1:], length-1)
            return 'D' + ('C' * correctInput) + recursiveCall
        elif input[0] == '4':
            return 'C' + 'D' + _arabicToRoman(input[1:], length-1)
        elif input[0] > '0':
            return 'C'*int(input[0]) + _arabicToRoman(input[1:], length-1)
        else:
            return _arabicToRoman(input[1:], length-1)
    elif length == 2:
        if input[0] == '9':
            return 'XC' + _arabicToRoman(input[1:], length-1)
        elif input[0] >= '5':
            correctInput = int(input[0])-5
            recursiveCall = _arabicToRoman(input[1:], length-1)
            return 'L' + ('X' * correctInput) + recursiveCall
        elif input[0] == '4':
            return 'X' + 'L' + _arabicToRoman(input[1:], length-1)
        elif input[0] > '0':
            return 'X'*int(input[0]) + _arabicToRoman(input[1:], length-1)
        else:
            return _arabicToRoman(input[1:], length-1)
    else:
        return 'Sorry, try again!'


print(arabicToRoman(4999))
