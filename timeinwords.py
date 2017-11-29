import re
def intlen(n):
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

def numinwords(time):
    words = {
                1: 'one',
                2: 'two',
                3: 'three',
                4: 'four',
                5: 'five',
                6: 'six',
                7: 'seven',
                8: 'eight',
                9: 'nine',
                10: 'ten',
                11: 'eleven',
                12: 'twelve',
                13: 'thirteen',
                14: 'fourteen',
                15: 'fifteen',
                16: 'sixteen',
                17: 'seventeen',
                18: 'eighteen',
                19: 'nineteen',
                20: 'twenty',
                30: 'thirty',
                40: 'fourty',
                50: 'fifty',
                60: 'sixty',
                70: 'seventy',
                80: 'eighty',
                90: 'ninty'
            }

    if time in words:
        return words[time]
    else:
        lista = []
        length = intlen(int(time))
        for i in xrange(1,length+1):
            val = time % (10 ** i)
            time = time - val
            lista.append(words[val])

        return " ".join(map(str, reversed(lista)))

def timeinwords(string):
    hours, mins = map(int,re.match(r'(\d{1,2}):(\d{2})',string).groups())
    string = ""
    if mins == 0:
        string += numinwords(hours) + " o' clock"
    elif mins < 30:
        if mins == 01:
            string += numinwords(mins) + " minute past %s" % numinwords(hours)
        elif mins == 15:
            string += "quarter past %s" % numinwords(hours)
        else:
            string += numinwords(mins) + " minutes past %s" % numinwords(hours)
    else:
        if mins == 30:
            string += "half past %s" % numinwords(hours)
        elif mins == 45:
            string += "qarter to %s" % numinwords(hours + 1)
        else:
            rmins = 60 - mins
            string += numinwords(rmins) + " minutes to %s" % numinwords(hours + 1)

    return string


