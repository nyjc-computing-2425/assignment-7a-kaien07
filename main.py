# Write a function to convert numbers to text numerals

def text_numeral(num):
    """
    converts an integer to words

    Parameters
    --------
    num: int
        number to be converted
    --------

    Returns
    --------
    str
        formatted string of num converted to words
    """
    NUM_WORD = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }
    if num > 90:
        num -= 90
        word_num = f"{NUM_WORD.get(90)} {NUM_WORD.get(num)}"
    elif num <= 20 or num % 10 == 0:
        word_num = NUM_WORD.get(num)
    else:
        tens_place = int(str(num)[0]) * 10
        ones_place = num % 10
        word_num = f"{NUM_WORD.get(tens_place)} {NUM_WORD.get(ones_place)}"
    return word_num