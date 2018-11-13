#names are case sensitive
#can include but not begin with numbers
#and can use the _ special character
#Assign a value, or values, to variables with the = symbol
a = 10
b, c, d = 2, 5, 10

#some basic types are:
integer = 123456
floating_point = 1.23456
a_string1 = "A string" ; a_string2 = 'Another String'
boolean = False
complex_numbers = 25 + 6j #j is i
a_list = [1,2,'3',4,5,"6"]


#cannot name things any of the python key words listed below:
    #False 	 class 	   finally 	is 	      return
    #None 	 continue  for 	    lambda 	  try
    #True 	 def 	   from 	nonlocal  while
    #and 	 del 	   global 	not 	  with
    #as 	 elif 	   if 	    or 	      yield
    #assert  else 	   import 	pass 	 
    #break 	 except    in 	    raise

#basic arithmetic +,-,*,/,%,**,//
x = 1+(2-3*4/5)%6**7//8 #follows order of operations
#can combine arithmetic and assignment +=,-=,*=,/=,%=,**=,//=
x += 1 # x = x + 1
x %= 2 # x = x % 2

#how to use if, elif, else, and, or, not, in, pass:
#pass does nothing
boolean_false = False
boolean_true = True
example_string = 'example'

if boolean_false:
    pass #not executed, boolean_false is False
elif boolean_false and boolean_true: #else if
    pass #not executed, both are not True
elif boolean_true or boolean_false:
    pass #is executed, one is True
elif not boolean_false:
    pass #not executed, previous elif was True
elif 'x' in example_string:
    pass #not executed, the condition is true, but previous if was true
else:
    pass #not executed, previous if was true

#comparison operators ==, !=, <, <=, >, >=
one = 1
two = 2
if two == one:
    pass #not executed, 2 doesn't equal one
elif one != 1:
    pass #not executed, one does equal one
elif two <= one:
    pass #not executed, two is greator then one
else:
    pass #is executed, all other if statements not true

#how to use while, for, continue, break
list_of_ints = [1,2,3]

for iterator in list_of_ints: #loops through four times
    #first, iterator is assigned 1 list_of_ints[0] then pass
    #second, iterator is assigned 2 then pass
    #thrird, iterator is assigned 3
    if iterator == 3: #on thrid time all values in list_of_ints are set to three
        list_of_ints[0] = 3
        list_of_ints[1] = 3
    pass #finally pass
condition = 0
while condition < 10:
    if condition == 2:   #on third time this is true
        condition = 5    #then condition is assigned 5
        continue         #we skip everything else and start the loop over
    elif condition == 6: #after condition increments from 5 to 6
        break            #the loops ends completely
    else:
        pass
    condition +=1 #we increase condition by one, only if none of the if above are true
    #at the end of ech pass through the loop condition is first 0, 1, 2, 5, 6 then stops

#how to uese def, try, except, return, finally
def some_function(parameter, another_parameter): #def defines a function that has takes some parameters
    if parameter:
        print(another_parameter)
    return 'This is the returned value' #after the function is executed this value is handed back
try:
    some_function(True,'This will be printed') #call to the function defined earlier
except: #you can also specify an exception, blank is just any exception
    print('Excpetion')
else: #if all the except are not executed this is
    print('no execption')
finally: #this is always executed
    print(some_function(False,'This will not be printed')) #the returned value will be printed instead

#TODO how to use class