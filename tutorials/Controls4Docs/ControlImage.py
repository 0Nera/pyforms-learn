#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__      = "Ricardo Ribeiro"
__credits__     = ["Ricardo Ribeiro"]
__license__     = "MIT"
__version__     = "0.0"
__maintainer__  = "Ricardo Ribeiro"
__email__       = "ricardojvr@gmail.com"
__status__      = "Development"


from __init__ import *
import cv2
import os

class SimpleExample(BaseWidget):
	
	
	def __init__(self):
		super(SimpleExample,self).__init__('Simple example')

		#Definition of the forms fields
		self._control 	= ControlImage('Image')
		self._open 	= ControlButton('Open')
		
		self.formset = [' ',(' ', '_control', ' '),'_open']

		self._open.value = self.__open
		
	def __open(self):
		file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '2.ControlsExamples', 'lena.png')
		self._control.value = cv2.imread(file_path)



##################################################################################################################
##################################################################################################################
##################################################################################################################

#Execute the application
if __name__ == "__main__":	 pyforms.start_app( SimpleExample )
	