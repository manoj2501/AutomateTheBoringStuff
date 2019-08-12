#! python3.7
# program to search for an address
# name map.py
import webbrowser
import sys,requests,pyperclip

# command line 
if len(sys.argv )>1  :

    address = ' '.join(sys.argv[1:])
else :
    address =pyperclip.paste()
webbrowser.open("https://www.fb.com/"+address)