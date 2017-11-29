import re

class ABBA:
    def __init__(self):
        pass

    def canObtain(self, initial, target):
        if initial == target:
            return "Possible"
        elif len(initial) > len(target):
            return "Impossible"
        elif (bool(re.search(initial,target)) or bool(re.search("".join(reversed(initial)),target))) != True:
            return "Impossible"
        else:
            if self.canObtain(initial + 'A', target) == "Possible" or self.canObtain("".join(reversed(initial)) + "B", target) == "Possible":
                return "Possible"
            else:
                return "Impossible"

if __name__ == "__main__":
    initial, target = raw_input().strip(), raw_input().strip()
    test = ABBA()
    print test.canObtain(initial, target)