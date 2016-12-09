# exercises:Basics

# class Person(object):
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#
#     def greet(self, other_person):
#         print "Hello %s, I am %s!" % (other_person.name, self.name)
#
# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
# Jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
#
#
# sonny.greet(Jordan)
# Jordan.greet(sonny)
#
# print "Sonny contact info: %s, %s" % (sonny.email, sonny.phone)
# print "Jordan contact info: %s, %s" % (Jordan.email, Jordan.phone)
#

# ###Make your own class
# class Vehicle(object):
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
# car = Vehicle('Nissan', 'Leaf', '2015')

#####add a method
# class Vehicle(object):
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def print_info(self):
#         print self.make, self.model, self.year
#
# car = Vehicle('Nissan', 'Leaf', '2015')
#
# car.print_info()


#### add a method 2
# class Person(object):
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#
#     def greet(self, other_person):
#         print "Hello %s, I am %s!" % (other_person.name, self.name)
#
#     def print_contact_info(self):
#         print self.name, self.email, self.phone
#
# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
# Jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
#
# sonny.print_contact_info()

#
# # add an instance variable (attribute)
# class Person(object):
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = []
#
#     def greet(self, other_person):
#         print "Hello %s, I am %s!" % (other_person.name, self.name)
#
#     def print_contact_info(self):
#         print self.name, self.email, self.phone
#
# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
# jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
#
# jordan.friends.append(sonny)
# sonny.friends.append(jordan)
#
# print len(jordan.friends)

# add a add_friend method
# class Person(object):
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = []
#
#     def greet(self, other_person):
#         print "Hello %s, I am %s!" % (other_person.name, self.name)
#
#     def print_contact_info(self):
#         print self.name, self.email, self.phone
#
#     def add_friend(self, other_person):
#         self.friends.append(other_person)
#
# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
# jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
#
# jordan.add_friend(sonny)
#
# print len(jordan.friends)

# add a num_friends method
# class Person(object):
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = []
#
#
#     def greet(self, other_person):
#         print "Hello %s, I am %s!" % (other_person.name, self.name)
#
#     def print_contact_info(self):
#         print self.name, self.email, self.phone
#
#     def add_friend(self, other_person):
#         self.friends.append(other_person)
#
#     def num_friends(self):
#         print self.name + "has %s friends " % (len(self.friends))
#
# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
# jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
#
# jordan.add_friend(sonny)
#
# print jordan.num_friends

# count number of greetings
# class Person(object):
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = []
#         self.greeting_count = 0
#
#     def greet(self, other_person):
#         self.greeting_count = self.greeting_count + 1
#         print "Hello %s, I am %s!" % (other_person.name, self.name)
#
#     def print_contact_info(self):
#         print self.name, self.email, self.phone
#
#     def add_friend(self, other_person):
#         self.friends.append(other_person)
#
#
# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
# jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
#
# print sonny.greeting_count
# sonny.greet(jordan)
# print sonny.greeting_count
# sonny.greet(jordan)
# sonny.greeting_count


# __repr__
# class Person(object):
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = []
#         self.greeting_count = 0
#
#     def greet(self, other_person):
#         self.greeting_count = self.greeting_count + 1
#         print "Hello %s, I am %s!" % (other_person.name, self.name)
#
#     def print_contact_info(self):
#         print self.name, self.email, self.phone
#
#     def add_friend(self, other_person):
#         self.friends.append(other_person)
#
#     def __repr__(self):
#         return " %s " % (self.name)
#
#
# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
# jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
#
# print sonny.__repr__


# bonus challenge unique number of greetings
# __repr__
class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.num_unique_people_greeted ={}

    def greet(self, other_person):
        self.greeting_count = self.greeting_count + 1
        self.num_unique_people_greeted[other_person.name] = self.num_unique_people_greeted.get(other_person.name, 0) + 1
        print "Hello %s, I am %s!" % (other_person.name, self.name)

    def print_contact_info(self):
        print self.name, self.email, self.phone

    def add_friend(self, other_person):
        self.friends.append(other_person)

    def __repr__(self):
        return " %s " % (self.name)

    def get_num_unique_people_greeted(self):
        print self.num_unique_people_greeted

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
smee = Person('Smee', 'itssmee@aol.com', '392-314-3817')

sonny.get_num_unique_people_greeted()
sonny.greet(jordan)
sonny.get_num_unique_people_greeted()
sonny.greet(smee)
sonny.greet(smee)
sonny.greet(smee)
sonny.greet(smee)
sonny.get_num_unique_people_greeted()
