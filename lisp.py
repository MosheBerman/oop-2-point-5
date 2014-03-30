'''

  Moshe Berman
  Professor Zhou
  CISC 3150
  Spring 2014

  Assignment 2.5

'''

'''    Utilities to mimic Lisp and Scheme. '''

def car(lst):
    return lst[0]
    
def cdr(lst):
    return lst[1:]
  
''' Q1. Write in Python, the following functions on Lisp-style lists. '''

#    Sums the elements in a list
def sumList(lst):
    if not lst:
        return 0
    else: 
        return car(lst) + sumList(cdr(lst))
    
 
 #    tests if x is an element in lst
def member(x, lst):
  if not lst:
      return False
  else: 
    return x == car(lst) or member(x, cdr(lst))

#    Duplicate a list
def duplicate(lst):
    if not lst:
        return []
    else:
        return [car(lst), car(lst)] + duplicate(cdr(lst))   

# Checks if an element is the prefix.
def is_prefix(pre, lst):
  if not pre:
    return True
  elif not car(pre) == car(lst):
    return False
  else:
    return is_prefix(cdr(pre), cdr(lst))

''' Q2. Consider sets represented as Lisp-style lists. Write the following functions. ''' 

# tests if subs is a subset of s
def subset(sub, s):


''' Test the functions... '''

#    Tests 
print "Testing sumList(lst)" 
print sumList([1, 2, 3]) #    6
print sumList([])        #    0

print "Testing member(x, lst)"
print member(7, [1,2,3]) #    False
print member(1, [1,2,3]) #    True

print "Testing duplicate(lst)"
print duplicate([])
print duplicate([8, 10, 30, 52])

print "Testing is_prefix(pre, lst)"
print is_prefix([1,2], [1,2,3,4])
print is_prefix([1,3], [1,2,3,4])

 # RUN: http://ideone.com/wkla46