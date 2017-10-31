#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

def extractDoc(filename):

   # Extract text in file that are
   # between /*! and */
   
   macroFile = open(filename, "r")
   macroFileContent = macroFile.readlines()
   macroFile.close()

   doc = ""
   extract = False
   for i in macroFileContent:
      if extract and "*/" in i:
         extract = False
      if extract:
         doc += i
      if "/*!" in i:
         extract = True
   return(doc)

def findSASfiles(folder):
   SASfiles = []
   for fn in os.listdir(folder):
      readFile = False
      try:
         if fn.endswith(".sas"):
            readFile = True
         else:
            readFile = False
      except:
         readFile = False

      if readFile:
         SASfiles.append(fn)

   return(SASfiles)

#def deleteMD(folder):
#   for fn in os.listdir(folder):
#      if fn.endswith(".md"):
#         os.remove(folder+fn)

folder = "./"
listofMacros = findSASfiles(folder)
print(listofMacros)

docFolder = "./docs/"

#deleteMD(docFolder)

index = ""
for i in listofMacros:
   heading = '''[Ta meg tilbake.](./)

# {0}

'''.format(i.split(".")[0])

   doc = extractDoc(folder + i)
   
   if doc != "":
      index += "- [{0}]({0})\n".format(i.split(".")[0])
      docFile = open(docFolder+i.split(".")[0]+".md", "w")
      docFile.write(heading + doc)
      docFile.close()

      
indexHeading = ""
for i in open(docFolder+"indexHead.md","r").readlines():
   indexHeading += i

indexFile = open(docFolder+"index.md", "w")
indexFile.write(indexHeading+index)
indexFile.close()


