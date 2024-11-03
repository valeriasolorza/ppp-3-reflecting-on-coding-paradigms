# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  # Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    self.condition = "repaired"
    
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def boost(self):
    self.max_speed *= 2
    
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def flame_jet(self,other):
    other.condition = "trashed"

'''

How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
    1.Encapsulation - attributes are contained in one class, grouping everything together
    2.Inheritance - the "pods" inherit attributes from the Podracer class and can use them without redefning each time
    3.Abstraction - N/A?
    4.Polymorphism - attributes can be changed within each "pod" without changing the class they are inheriting

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    I think his is the simplest way to code this solution as far as we have learned. Maybe other languages have simpler ways?

How in particular did Object Oriented Programming assist in the solving of this problem?
    Each podracer type has a specific class with defined attributes and methods, making it easy to add new podracer types without changing existing code
'''

