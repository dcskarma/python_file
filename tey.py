# !/usr/bin/env python

hacker = "me"

def local_var():
  hacker = "you"


print ("The local var is %s") % (hacker)

local_var()

print ("the golbal var is %s") % (hacker)
