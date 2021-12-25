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



class SimpleExample5(BaseWidget):
	
	def __init__(self):
		super(SimpleExample5,self).__init__('Simple example 5')

		#Definition of the forms fields
		self._firstname 	= ControlText('First name', 'Default value')
		self._middlename 	= ControlText('Middle name')
		self._lastname 		= ControlText('Lastname name')
		self._fullname 		= ControlText('Full name')
		self._button 		= ControlButton('Press this button')

		self.formset = [ {
						  	'Tab1':['_firstname','||','_middlename','||','_lastname'], 
						  	'Tab2': ['_fullname']
						  },
						  '=',(' ','_button', ' ') ]

		
		#Define the window main menu using the property main menu
		self.mainmenu = [
			{ 'File': [
					{'Open': self.__dummyEvent},
					'-',
					{'Save': self.__dummyEvent},
					{'Save as': self.__dummyEvent}
				]
			},
			{ 'Edit': [
					{'Copy': self.__dummyEvent},
					{'Past': self.__dummyEvent}
				]
			}
		]

	def __dummyEvent(self):
		print "Menu option selected"


##################################################################################################################
##################################################################################################################
##################################################################################################################

#Execute the application
if __name__ == "__main__":	 pyforms.start_app( SimpleExample5 )
	