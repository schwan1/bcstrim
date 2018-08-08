import re
import numpy as np

mSubject = ""
mNumber = ""
mDate = ""
mDueDate = ""
mFrom = ""
mDesc = ""
mRef = [""]
productLine =""
product = ""
account = ""
project = ""
priority = ""
mBody = ""

def after(value, a):
    # Find and validate first part.
    pos_a = value.rfind(a)
    if pos_a == -1: return ""
    # Returns chars after the found string.
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= len(value): return ""
    return value[adjusted_pos_a:]

def between(value, a, b):
    # Find and validate before-part.
    pos_a = value.find(a)
    if pos_a == -1: return ""
    # Find and validate after part.
    pos_b = value.rfind(b)
    if pos_b == -1: return ""
    # Return middle part.
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= pos_b: return ""
    return value[adjusted_pos_a:pos_b]

def before(value, a):
    # Find first part and return slice before it.
    pos_a = value.find(a)
    if pos_a == -1: return ""
    return value[0:pos_a]


def subextract(mask, text):
    # Extract subject line
    sub = re.findall(mask, text)
    for subject in sub:
        subject = subject.replace('\n',' ')
        subject = subject.rstrip()
        subject = after(subject, '// ')
    # Return last found instance in message
    return subject
   
def dateextract(mask, text):
    # Extract message line
    mdate = re.findall(mask, text)
    
    for alldate in mdate:
        alldate = alldate.replace('\n',' ')
        alldate = alldate.rstrip()
        alldate = after(alldate, ':')
        alldate = alldate.lstrip()
    # Return last found instance in message
    return alldate

def descextract(mask, text):
    # Extract message line
    mdesc = re.findall(mask, text)
    for alldesc in mdesc:
        alldesc = alldesc.replace('\n',' ')
        alldesc = alldesc.rstrip()
        alldesc = after(alldesc, ':')
       # alldesc = alldesc.lstrip()
    # Return last found instance in message
    return alldesc


def numextract(mask,text):
    mNumber = ""
    # Extract message line
    mNum = re.findall(mask, text)
    for mNumber in mNum:
        mNumber = mNumber.replace('\n',' ')
        mNumber = mNumber.rstrip()
        mNumber = after(mNumber, 'A')
    # Return last found instance in message
    return mNumber



try:
    with open("BCS Raw 4-1x16EVO.txt",'r') as my_file_handle:
        mtext = my_file_handle.read()
except FileNotFoundError:
    mtext = print ('File Read Error')
    
# Initialize all variables for BCS message content

mSubject = subextract('SUBJECT:.+\n',mtext)
mNumber = numextract('^.MESSAGE NUMBER:',mtext)
mDueDate = dateextract('DUE DATE:.+\n',mtext)
mDate = dateextract('ACTIVITY DATE:.+\n',mtext)
mDesc = descextract('DESCRIPTION:\n.+\n.+\n',mtext)

print (mSubject)
print (mDueDate)
print (mDate)
print (mDesc)
