#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
    i = 0
    while i<=j:
        print " ",
        i+=1


def findAdmin():
    f = open("link.txt","r");
    link = raw_input("Website:")
    print "\n\nPossible : \n"
    while True:
        sub_link = f.readline()
        if not sub_link:
            break
        req_link = "http://"+link+"/"+sub_link
        req = Request(req_link)
        try:
            response = urlopen(req)
        except HTTPError as e:
            continue
        except URLError as e:
            continue
        else:
            print "YES => ",req_link

def Credit():
    Space(9); print "  _   _   _   _   _   _   _   _   _   _  "
    Space(9); print " / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ " 
    Space(9); print "( N | O | B | - | L | O | A | D | E | R )" 
    Space(9); print " \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ " 
    Space(9); print "                                           " 
    Space(9); print "-----------------------------------------                                                             "
    
    Space(9); print "       [+]Moded BY Mask m3n[+]"
    Space(9); print "                                                                "
    
    Space(9); print "         [+]Version 1.0[+]   "
Credit()
findAdmin()
