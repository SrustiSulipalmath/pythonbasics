class Student:
    def __init__(self,name,major,gpa,is_on_probation):
      #attributes
        self.name = name  #values,parameters
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if float(self.gpa) >= 3.5:
          return True
        else:
          return False
