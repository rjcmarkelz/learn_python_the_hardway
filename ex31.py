print """You enter a dark room with two doors. 
Do you go through door 1 or door 2?"""

door = raw_input("Choose a door: ")

if door == "1":
	print "There is a giant bear here eating cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")

	if   bear == "1":
		print "Not the best choice...the bear eats your face off!"
	elif bear == "2":
		print "You idiot! You startled the bear and he eats your legs off!"
	else:
		print "Well, doing %s is a good idea. The bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss of Cthulhul's face"
	print "You slowly go insane. What do you do?"
	print "1. Blueberries!"
	print "2. Yellow jackets!"
	print "3. Garg narg underpants head!"

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives but your mind is jello."
	else:
		print "The insanity rots your eyes into a pool of muck."

else:
	print """You cannot even count? You stumble around and fall on a knife and die."""






