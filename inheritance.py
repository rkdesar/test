#!/usr/bin/python

class Person:
	
	def __init__(self,first,last):
		self.firstname = first
		self.lastname = last

	def Name(self):
		return self.firstname + " " + self.lastname

class Employee(Person):
	
	def __init__(self,first,last,staffnum):
		Person.__init__(self,first,last)
		self.staffnumber = staffnum
	def GetEmployee(self):
		return self.Name() + "," + self.staffnumber

x = Person("Marge", "Simpson")
y = Employee("Homer","simpson","1007")

print(x.Name())
print(y.GetEmployee())
