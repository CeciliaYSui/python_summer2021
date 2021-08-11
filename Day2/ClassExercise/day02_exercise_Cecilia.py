# An exercise 

from typing import Mapping


class Senator():
  def __init__(self, name):
    self.name = name
    self.bills_voted_on = [] ## list of Bill objects

  def __str__(self): # Print method  
    # self.name
    return "Senator : %s" % (self.name)

    # def __str__(self): #print method will display the school name and sorted student, note the built in
    #     return "%s\n%s" %(self.school_name, self.sort())

  def vote(self, bill, choice):
    #update the bill object--
    # add the senator's name to the the list of yes/no/abstain
    bill.votes[choice].append(self.name)
    #update the senator object--add this bill to the bills this senator has voted on
    self.bills_voted_on.append(bill) 
    #print an informative message announcing the vote 
    # get: name + choice + the bill title
    # return "Senator %s voted %s  ." % (self.name, choice)  
    return "Senator " +  self.name + " voted " + choice + " on " + bill.title +  "." 

class Bill():
  def __init__(self, title):
    self.title = title
    self.votes = {"yes" : [], "no" : [], "abstain" : []}
    self.passed = None

  def __str__(self): # Print method  
    return self.title

  def result(self):
    # update and return the "passed" variable to indicate True/False if the bill passed
    if len(self.votes["yes"]) > len(self.votes["no"]): 
      self.passed = True
    else:
      self.passed = False
    return self.passed


## should be able to do these things
jane = Senator("Jane")
jack = Senator("Jack")
print(jack)
print(jane)
environment = Bill("Environmental Protection")
print(environment)
jane.vote(environment, "yes")
jack.vote(environment, "no")
environment.result()
print(environment.votes)
print(environment.passed) # False 
print(jack.bills_voted_on[0].passed) # False



