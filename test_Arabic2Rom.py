from Arabic2Rom import arabicToRoman


def testMax():
    assert arabicToRoman(4999) == 'MMMMCMXCIX'


def testSmallNumber():
    assert arabicToRoman(6) == 'VI'

def testMediumNumber():
    assert arabicToRoman(869) == 'DCCCLXIX'


def testBigNumber():
    assert arabicToRoman(3987) == 'MMMCMLXXXVII'


def testTooBig():
    assert arabicToRoman(8000) == ''


def testString():
    assert arabicToRoman('I love the romans') == ''


def testDecimalNumber():
    assert arabicToRoman(3.14) == ''


def testNumberandString():
    assert arabicToRoman('aloha345hi') == ''