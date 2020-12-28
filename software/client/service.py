#This is the main program that facilitates running the others. In other words, the logic loop.

#check for updates
import updateservice.py

#Program loop
while True:
	import imagecompressor
	import sendtoserver


#program cannot be killed by student