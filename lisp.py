#    The homework 2.5 for Professor Zhou's CISC 3150 class at Brooklyn College.


#    Utilities to mimic Lisp and Scheme.

def car(lst):
    return lst[0]
    
def cdr(lst):
    return lst[1:]
   
#    Sums the elements in a list
def sumList(lst):
    if not lst:
        return 0
    else: 
        return car(lst) + sumList(cdr(lst))
    
 
 #    Checks if x is in a list
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

 # RUN: http://ideone.com/wkla46