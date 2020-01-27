
def arabicToRoman(input):
    if int(input) > 4999:
        return 'Too big a number for the Romans'
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
    elif length == 4 and input[0] :

        return 'M'*int(input[0]) + _arabicToRoman(input[1:], length-1)
    elif length == 3:
        if input[0] == '9':
            return 'CM' + _arabicToRoman(input[1:], length-1)
        elif input[0] >= '5':
            return 'D' + ('C'*(int(input[0])-5)) + _arabicToRoman(input[1:], length-1)
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
            return 'L' + ('X'*(int(input[0])-5)) + _arabicToRoman(input[1:], length-1)
        elif input[0] == '4':
            return 'X' + 'L' + _arabicToRoman(input[1:], length-1)
        elif input[0] > '0':
            return 'X'*int(input[0]) + _arabicToRoman(input[1:], length-1)
        else:
            return _arabicToRoman(input[1:], length-1)
    else:
        return 'Sorry, try again!'

print(arabicToRoman(4999))