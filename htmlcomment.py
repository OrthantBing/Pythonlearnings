from HTMLParser import HTMLParser
import re

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if re.search(r'\n',data):
            print ">>> Multi-line Comment"
            print data
        else:
            print ">>> Single-line Comment"
            print data

    def handle_data(self, data):
        print ">>> Data"
        print data
