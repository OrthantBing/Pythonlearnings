from HTMLParser import HTMLParser
import re

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print tag
        for key,value in attrs:
            print "->",key,">",value
