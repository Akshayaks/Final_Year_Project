#!/usr/bin/env python
import sys
sys.path.append('/home/lenovo/Dev/venv/src/elearnerapp/elearnerapp')
# from youTubeSearch import Ysearch

class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


class Topics(object):
	def __init__(self,name,topics):
		self.name = name
		self.topics = topics
	# def display_topics(self):
	# 	print(self.name)
	# 	print(self.topics)
	# def display_data(self):
	# 	for i in self.topics:
	# 		data_list=Ysearch(i)
	# 		for j in data_list:
	# 			print(j)
	
class Node(object):
	def __init__(self,name,units):
		self.name = name  #This is the main three topics
		self.units = units  #This will be a dictionary with units and topics
	# def display_units(self):
	# 	print(self.name)
	# 	for i in self.units:
	# 		print(i)
	# 		for j in self.units[i]:
	# 			j.display_topics()
	# 			print("\n")
	# 		print("\n")
        
def Readfile(filename):
	lineList = [line.rstrip('\n') for line in open(filename)]
	return lineList


root = Tree()

Introduction = Topics("Introduction", Readfile("/home/lenovo/Dev/venv/src/elearnerapp/Syllabus/Basics_unit1.txt"))
Planning = Topics("Planning", Readfile("/home/lenovo/Dev/venv/src/elearnerapp/Syllabus/Basics_unit2.txt"))
Organising = Topics("Organising", Readfile("/home/lenovo/Dev/venv/src/elearnerapp/Syllabus/Basics_unit3.txt"))
Directing = Topics("Directing", Readfile("/home/lenovo/Dev/venv/src/elearnerapp/Syllabus/Basics_unit4.txt"))
Controlling = Topics("Controlling", Readfile("/home/lenovo/Dev/venv/src/elearnerapp/Syllabus/Basics_unit5.txt"))

Dict1 = {'Easy': [Introduction, Planning], 'Medium': [Organising, Directing], 'Hard': [Controlling]}
root.data = Node("Basics of Management",Dict1)
 


root.left = Tree()

Perspectives = Topics("Perspectives", Readfile("/home/lenovo/Dev/venv/src/elearnerapp/Syllabus/HR_unit1.txt"))
BestFit = Topics("BestFit", Readfile("/home/lenovo/Dev/venv/src/elearnerapp/Syllabus/HR_unit2.txt"))
Training = Topics("Training", Readfile("/home/lenovo/Dev/venv/src/elearnerapp/Syllabus/HR_unit3.txt"))
EmpInterest = Topics("EmpInterest", Readfile("/home/lenovo/Dev/venv/src/elearnerapp/Syllabus/HR_unit4.txt"))
Evaluation = Topics("Evaluation", Readfile("/home/lenovo/Dev/venv/src/elearnerapp/Syllabus/HR_unit5.txt"))

Dict2 = {'Easy' : [Perspectives, BestFit], 'Medium': [Training, EmpInterest], 'Hard': [Evaluation]}
root.left.data = Node("Human Resource Management",Dict2)


root.right = Tree()

Intro_marketing = Topics("Intro_marketing", Readfile("/home/lenovo/Dev/venv/src/elearnerapp/Syllabus/MM_unit1.txt"))
Strategy = Topics("Strategy", Readfile("/home/lenovo/Dev/venv/src/elearnerapp/Syllabus/MM_unit2.txt"))
MixDecisions = Topics("MixDecisions", Readfile("/home/lenovo/Dev/venv/src/elearnerapp/Syllabus/MM_unit3.txt"))
Behaviour = Topics("Behaviour", Readfile("/home/lenovo/Dev/venv/src/elearnerapp/Syllabus/MM_unit4.txt"))
Trends = Topics("Trends", Readfile("/home/lenovo/Dev/venv/src/elearnerapp/Syllabus/MM_unit5.txt"))

Dict3 = {'Easy' : [Intro_marketing], 'Medium' : [Strategy, MixDecisions], 'Hard' : [Behaviour, Trends]}
root.right.data = Node("Marketing Management",Dict3)
 

# root.data.display_units()
# print("\n")
# root.left.data.display_units()
# print("\n")
# root.right.data.display_units()
# Introduction.display_data()
# print("\n")
