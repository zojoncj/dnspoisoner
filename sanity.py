import re
def protect_default(l):
  ret=[]
  for i in l:
    if re.search("(.*\.)?orst\.edu$",i) == None:
      ret.append(i)
  return ret

def protect_orst(l):
  print sys._getframe().f_code.co_name
  ret=[]
  for i in l:
    if re.search("(.*\.)?orst\.edu$",i) == None:
      ret.append(i)
  return ret

def protect_oregonstate(l):
  ret=[]
  for i in l:
    if re.search("(.*\.)?oregonstate\.edu$",i) == None:
      ret.append(i)
  return ret
