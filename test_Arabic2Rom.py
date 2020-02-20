

from Arabic2Rom import arabicToRoman


def testLegalInput():
    assert arabicToRoman(1)=="I"
    assert arabicToRoman(2)=="II"
    assert arabicToRoman(3)=="III"
    assert arabicToRoman(4)=="IV"
    assert arabicToRoman(5)=="V"
    assert arabicToRoman(9)=="IX"
    assert arabicToRoman(10)=="X"
    assert arabicToRoman(13)=="XIII"
    assert arabicToRoman(14)=="XIV"
    assert arabicToRoman(15)=="XV"
    assert arabicToRoman(19)=="XIX"
    assert arabicToRoman(869) == 'DCCCLXIX'
    assert arabicToRoman(3987) == 'MMMCMLXXXVII'
    assert arabicToRoman(4999) == 'MMMMCMXCIX'



def testIllegal():
    assert arabicToRoman('aloha345hi') == ''
    assert arabicToRoman(3.14) == ''
    assert arabicToRoman('I love the romans') == ''
    assert arabicToRoman(8000) == ''
