#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import codecs
import warnings
import errno


def extractDoc(filename):

   # Extract text in file that are
   # between /*! and */
   
   macroFile = codecs.open(filename, "r", "latin-1")
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

folder = "./"
listofMacros = findSASfiles(folder)

docFolder = "./docs/"

try:
    os.makedirs(docFolder)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

index = ""
for i in listofMacros:
   heading = '''[Ta meg tilbake.](./)

# {0}

'''.format(i.split(".")[0])
   
   heading += '''

## Innholdsfortegnelse
{: .no_toc}

* auto-gen TOC:
{:toc}

'''

   doc = extractDoc(folder + i)
   
   if doc != "":
      index += "- [{0}]({0})\n".format(i.split(".")[0])
      docFile = codecs.open(docFolder+i.split(".")[0]+".md", "w", "utf-8")
      docFile.write(heading + doc)
      docFile.close()
   else:
      warnings.warn("ADVARSEL: Makroen {0} er ikke dokumentert!".format(i.split(".")[0]))

      
indexHeading = ""
for i in open("./doc/indexHead.md","r").readlines():
   indexHeading += i

indexFile = open(docFolder+"index.md", "w")
indexFile.write(indexHeading+index)
indexFile.close()


