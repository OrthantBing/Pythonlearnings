if __name__ == '__main__':
    string = raw_input()
    count = len(string) // 3
    originalstring = "SOS" * count
    print len([i for i in xrange(len(originalstring)) if string[i] != originalstring[i]])
