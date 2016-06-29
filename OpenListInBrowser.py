import webbrowser
import sys

path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
bp = 50

if len(sys.argv) < 2:
	print("Please supply an input list or -h")
	sys.exit(0)

if(sys.argv[1] == "-h" or sys.argv[1] == "--help"):
	print("Replace the path variable in the script with your browser's. "
		"Problems has previously been encountered with IE and I would suggest"
		" using Chrome. The path also has to use \"/\" and not \"\\\"."
		"Examples:"
		"python openips.py list.txt"
		"python openips.py list.txt https")
	sys.exit(0)

https = False
if(len(sys.argv) == 3):
	if(sys.argv[2] == "https"):
		https = True

f = open(sys.argv[1], 'r')
i = 1
for line in f:
	if(i % bp == 0):
		input("Press enter to get " + str(bp) + " more")
	if(https):
		line = "https://" + line
	webbrowser.get(path + ' %s').open_new_tab(line)
	i += 1
