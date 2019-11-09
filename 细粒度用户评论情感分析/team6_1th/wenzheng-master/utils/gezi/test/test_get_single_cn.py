#!/usr/bin/env python
#coding=gbk
# ==============================================================================
#          \file   test.py
#        \author   chenghuige  
#          \date   2016-08-25 19:20:59.405334
#   \Description  
# ==============================================================================

  
from __future__ import absolute_import
from __future__ import division
#from __future__ import print_function

import sys,os

#import libstringutil
import nowarning
import libgezi
libstringutil = libgezi 

print libstringutil.extract_gbk_dual('nike����Ьis��')

for item in libstringutil.to_cnvec('nike����Ьis��'):
  print item 

l = libstringutil.extract_gbk_dual('nike����Ь���Ǻ�hah�Բ���')

print l
print type(l)

for item in l.decode('gbk'):
  print item.encode('gbk')

l = libstringutil.to_cnvec(libstringutil.extract_chinese('nike����Ь���Ǻ�hah�Բ���'))

for item in l:
  print item
