#!/usr/bin/env python

import argparse
import sys
import os
import ConfigParser

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
  config = ConfigParser.ConfigParser(allow_no_value=True)
  try:
    config.read(f)
  except ConfigParser.ParsingError, e:
    giveup("Error reading config file %s at %s" %(e.filename,e.errors))
  return config

def getwhitelist(list):
  return list
 
def getnames(b,w):
  b = set(b)
  w = set(w)
  return b - w


def main(arguments):

  parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument("-c", "--config", help="Configuration File." ,
                        default="./config")
  parser.add_argument("-b", "--blacklist", help="List of domains to be poisoned." ,
                        required=True)


  args = parser.parse_args(arguments)

  config=getconfig(args.config)
  blacklist=getlist(args.blacklist)
  whitelist=getwhitelist(config.options('whitelist'))
  getnames(blacklist,whitelist)
  

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
