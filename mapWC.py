#!/usr/bin/env python

import sys
import string

for line in sys.stdin:
  words=line.split()
  print '%s\t%s' % (words[1],1)
  
