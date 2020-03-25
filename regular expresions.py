# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:29:27 2018

@author: Cherukuri Amul
"""
#
#import re
#email_address = 'sdilipkumar654@gmail.com'
#match = re.search(r'([\w\.-]+)@([\w\.-]+)', email_address)
#if email_address:
#  print(match.group()) # The whole matched text
#  print(match.group(1)) # The username (group 1)
#  print(match.group(2)) # The host (group 2)

##################################################
#import sys
#print ('Enter your name:')
#name=''
#while True:
#   c = sys.stdin.read(1)
#   if c == '\n':
#      break
#   name = name + c
# 
#print ('Your name is:', name)
#######################################################
# regular expression
#used for matching a new password and confiem passwoerd process
#import re 
#pattern = r"Cookie"
# 		 # r is for reading the text or line
#sequence = "Cookie"
#
#if re.match(pattern, sequence):
#  # matching to the exact text
#	print("Match!")
#
#else:
#	 print("Not a match!")


#matching password
#import re 
#pattern = "Cookie"
# 		 # r is for reading the text or line
#sequence =input('enter password:')
#
#if re.match(pattern, sequence):
#  # matching to the exact text
#    f=open('F:/python/file.txt')
#    print(f.read())
#    f.close()
#    
#else:
#    print("password does not match")
#	
#
#

#############################################
 #match function with group method
#import re
#
#line = "Cats are smarter than dogs"
#
#matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
#
#if matchObj:
#   print ("matchObj.group() : ", matchObj.group())
#   print ("matchObj.group(1) : ", matchObj.group(1))
#   print ("matchObj.group(2) : ", matchObj.group(2))
##   print ("matchObj.group(2) : ", matchObj.group(3))
#else:
#   print ("No match!!")

 ############################################  
# search function 
#import re
#
#line = "Cats are smarter than dogs";
#
#searchObj = re.search( r'(.*) are (.*?) .*' , line, re.M|re.I)
#
#if searchObj:
#   print ("searchObj.group() : ", searchObj.group())
#   print ("searchObj.group(1) : ", searchObj.group(1))
#   print ("searchObj.group(2) : ", searchObj.group(2))
#else:
#   print ("Nothing found!!")
#if searchObj.group(1)=='Cats':
#    print("searched")
#else:
#    print("not found")
################################################
# matching Vs searching
#import re
#
#line = "Cats are smarter than dogs";
#
#matchObj = re.match( r'dogs', line, re.M|re.I)
#if matchObj:
#   print ("match --> matchObj.group() : ", matchObj.group())
#else:
#   print ("No match!!")
#
#searchObj = re.search( r'dogs', line, re.M|re.I)
#if searchObj:
#   print ("search --> searchObj.group() : ", searchObj.group())
#else:
#   print ("Nothing found!!")
##############################################
# search & replace
# syntax : re.sub(pattern,repl,string,max=0)
#This method replaces all occurrences of the 
#RE pattern in string with repl, substituting all occurrences 
#unless max provided. This method returns modified string.

#import re
#
#phone = "2004-959-559 This is Phone Number"
#
## Delete Python-style comments
#num = re.sub(r'T.*$', "hai", phone) # '$' matches end of line 
#             # '.' matches any single charector
#             
#print ("Phone Num : ", num)
#
## Remove anything other than digits
#num = re.sub(r'\D', "", phone)    
#print ("Phone Num : ", num)
#









#
#
#import re
#a=r'analytics'
#result=re.match(r'ana',a)
#print(result.start())
#print(result.end())