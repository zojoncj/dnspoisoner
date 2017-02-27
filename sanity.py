import re

def protect_orst(l):
  ret=[]
  for i in l:
    if re.search("(.*\.)?orst|oregonstate\.edu$",i) == None:
      ret.append(i)
  return ret


