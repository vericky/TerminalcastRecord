"""
Copyright Patrick Mullen 2009
"""
__author__="Paddy Mullen"
__date__ ="$May 14/2009"

from setuptools import setup, find_packages

import pdb
#pdb.set_trace()
import os
os.system("cp record_terminalcast/tty_rec/ttyrec /usr/bin")
setup(name='terminalcast_record',
      version='1.0',
      description='record a terminal session',
      author='Paddy Mullen',
      author_email='paddy@chartwidget.com',
      url='http://demo.chartwidget.com',
      entry_points = {
          'console_scripts':[
              'rec_tcast = record_terminalcast.record:my_main']},
      #data_files=["record_terminalcast/tty_rec/ttyrec"],
      packages=['record_terminalcast','record_terminalcast.tty_rec']
     )
