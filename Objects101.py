import time
import random

class Person(object):
    alive = True
    innocent= True
    onTheRun=False
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.birthdate = time.time

    def greet(self):
        print "Hello "
    def kill(self, person):
        person.alive=False
        self.innocent=False
        self.onTheRun=True
        # print "%s just killed %s" % (self.longname(),person.longname())

    def longname(self):
        return self.fname + " " + self.lname

    def birthdate(self, format=""):
        return self.fname + " " + self.lname

janice = Person("Janice", "Smith")

# janice.greet()
bob = Person("Bob", "Jones")
#
if (random.randint(0,10))%2:
    murderer = bob
    victim = janice
else:
    murderer = janice
    victim = bob

print "%s killed %s. %s is now on the run" % (murderer.fname, victim.fname, murderer.fname)
# print "Janice alive: ", janice.alive
