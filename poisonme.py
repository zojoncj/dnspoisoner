#!/usr/bin/env python

import argparse
import sys
import os
import ConfigParser
import sanity
import re

def giveup(msg):
  sys.exit(msg)

def getlist(f):
  try:
    with open(f) as fh:
          lines = fh.read().splitlines()
    return lines
  except IOError:
    giveup("Unable to open file %s" % f)

def getconfig(f):
  if(not os.path.isfile(f)):
    giveup("Config file %s does not exist" % f)
  global config
  c = ConfigParser.ConfigParser(allow_no_value=True)
  try:
    c.read(f)
    config=c
  except ConfigParser.ParsingError, e:
    giveup("Error reading config file %s at %s" %(e.filename,e.errors))

def getwhitelist(l):
  return l

def sanitycheck(l):
  checks=config.options('sanity')
  for check in checks:
    if config.getboolean('sanity',check) == True:
      try:
        f=getattr(sanity,check)
        l=f(l)
      except AttributeError, e:
        giveup(e)
  return l

      


def listmagic(b,w):
  b = set(b)
  w = set(w)
  tmplist=b-w
  l=sanitycheck(tmplist)
  return l


def main(arguments):

  parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument("-c", "--config", help="Configuration File." ,
                        default="./config")
  parser.add_argument("-b", "--blacklist", help="List of domains to be poisoned." ,
                        required=True)

  args = parser.parse_args(arguments)

  getconfig(args.config)


  blacklist=getlist(args.blacklist)
  whitelist=getwhitelist(config.options('whitelist'))
  blocklist = listmagic(blacklist,whitelist)
  print blocklist
  

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
