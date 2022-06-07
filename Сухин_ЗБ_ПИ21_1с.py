def fact(x):
  if (x > 1):
    return x * fact(x - 1)
  return 1
  pass

def filter_even(li):
  return list(filter(lambda x: x%2 == 0, li))
  pass

def square(li):
  return map(lambda x: x**2, li)
  pass

def bin_search(li, element):
  first = 0
  last = len(li) - 1
  exit = -1

  while (first <= last) & (exit == -1):
    middle = (first + last) // 2
    if li[middle] == element:
      exit = middle
    else:
      if (element < li[middle]):
        last = middle - 1
      else:
        first = middle + 1

  return exit
  pass

def is_palindrome(string):
    string.lower()
    string.replace(" ", "")
    start = 0
    end = len(string) - 1
    result = "YES"

    while (start < len(string) - 1) & (result == "YES") & (start < end):
        while not str.isalpha(string[start]):
            start += 1
        while not str.isalpha(string[end]):
            end -= 1
        
        if (string[start] != string[end]):
            result = "NO"
        else:
            start += 1
            end -= 1
    
    return result
    pass

def calculate(path2file):
    file = open(path2file, "r")

    line = file.readline()
    string = ""

    while line:
        if (len(string) != 0):
            string += ","
        
        value = line.split("    ").replace("\n", "")

        if value[0] == '+':
            string += str(int(value[1]) + int(value[2]))
        elif value[0] == '-':
            string += str(int(value[1]) - int(value[2]))
        elif value[0] == '*':
            string += str(int(value[1]) * int(value[2]))
        elif value[0] == '//':
            string += str(int(value[1]) // int(value[2]))
        elif value[0] == '%':
            string += str(int(value[1]) % int(value[2]))
        elif value[0] == '**':
            string += str(int(value[1]) ** int(value[2]))
        
        line = file.readline()

    return string
    pass

def substring_slice(path2file_1,path2file_2):
    file1 = open(path2file_1, "r")
    file2 = open(path2file_2, "r")

    line1 = file1.readline()
    line2 = file2.readline()
    string = ""

    while line1:
        if (len(string) != 0):
            string += " "

        s = line2[:-1].split(" ")

        string += line1[int(s[0]):int(s[1])+1]

        line1 = file1.readline()
        line2 = file2.readline()

    return string
    pass

import json
import re

def decode_ch(srting_of_elements):
    periodic_table = json.load(open('periodic_table.json'))
    string = ""
    sliced = re.findall('[A-Z][a-z]*', srting_of_elements)

    for s in sliced:
        string += periodic_table[s]

    return string
    pass

class Student:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.fullname = name + " " + surname

    self.grades = [3, 4, 5]

  def greeting(self):
    return "Hello, I am Student"

  def mean_grade(self):
    sum = 0
    for g in self.grades:
      sum += g
    
    return sum/len(self.grades)

  def is_otlichnik(self):
    sr = self.mean_grade()

    if (sr >= 4.5):
      return "YES"
    else:
      return "NO"
    
  def __add__(self, other):
    return self.name + " is friends with " + other.name
  
  def __str__(self):
    return self.fullname
  pass

class MyError(Exception):
  def __init__(self, msg):
    self.msg = msg
  pass