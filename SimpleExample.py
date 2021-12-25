#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__      = "Ricardo Ribeiro"
__credits__     = ["Ricardo Ribeiro"]
__license__     = "MIT"
__version__     = "0.0"
__maintainer__  = "Ricardo Ribeiro"
__email__       = "ricardojvr@gmail.com"
__status__      = "Development"



from pyforms.basewidget import BaseWidget
from pyforms.controls 	import ControlText
from pyforms.controls 	import ControlButton
from pyforms.controls 	import ControlMatplotlib

from pyforms.controls 	import ControlBoundingSlider
from pyforms.controls 	import ControlCheckBox
from pyforms.controls 	import ControlCheckBoxList
from pyforms.controls 	import ControlCombo
from pyforms.controls 	import ControlDir
from pyforms.controls 	import ControlDockWidget
from pyforms.controls 	import ControlEmptyWidget
from pyforms.controls 	import ControlFile
from pyforms.controls 	import ControlFilesTree
from pyforms.controls 	import ControlImage
from pyforms.controls 	import ControlList
from pyforms.controls 	import ControlPlayer
from pyforms.controls 	import ControlProgress
from pyforms.controls 	import ControlSlider
from pyforms.controls 	import ControlVisVis
from pyforms.controls 	import ControlVisVisVolume
from pyforms.controls 	import ControlEventTimeline
from pyforms.controls 	import ControlCodeEditor

import pyforms
import pyforms
import numpy as np

import random

class Example1(BaseWidget):
	
	def __init__(self):
		super(Example1,self).__init__('Simple example 1')

		#Definition of the forms fields
		self._checkbox 		= ControlCheckBox('Choose a directory')
		self._checkboxList 	= ControlCheckBoxList('Choose a file')
		self._player 		= ControlPlayer('Choose a file')
		self._slider		= ControlSlider('Slider')
		
		self._player.show()
		self.formset = [  '_slider', ('_checkboxList', '_player'), ('_checkbox',' ') ]


		self._checkboxList.value = [ ('Item 1', True), ('Item 2', False), ('Item 3', True)]







##################################################################################################################
##################################################################################################################
##################################################################################################################

#Execute the application
if __name__ == "__main__":	 pyforms.start_app( Example1 )