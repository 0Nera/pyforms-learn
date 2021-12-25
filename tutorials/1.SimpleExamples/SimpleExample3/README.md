# Simple example 3

This example shows you how to organize the forms side by side using the variable "self.formset".
		
```python
	#Add the name of the forms variables inside tuples organize these forms side by side
	self.formset = [ ('_firstname','_middlename', '_lastname'), 
			'_fullname', (' ' ,'_button', ' '), ' ']
```



**Notes:**
- Forms vertically organized - use list.
- Forms horizontally organized - use a tuple.



![Simple example 3](screenshot.png?raw=true "Screen")