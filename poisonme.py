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
  print f
  config = ConfigParser.ConfigParser()
  config.read(f)

def main(arguments):

  parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument("-b", "--blacklist", help="List of domains to be poisoned." ,
                        required=True)
  parser.add_argument("-c", "--config", help="Configuration File." ,
                        default="./config")
  parser.add_argument("-w", "--whitelist", help="List of domains to not allow to be poisoned.", 
                        default="./whitelist")


  args = parser.parse_args(arguments)

  blacklist=getlist(args.blacklist)

  config=getconfig(args.config)

  whitelist=getlist(args.whitelist)
  


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
