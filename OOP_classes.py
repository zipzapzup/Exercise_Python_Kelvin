import datetime

class User:
  """ Creating user classes. Where User is a database where we can store User's personal data. As this is a test function, we are only storing 3 variables
  Name, Birthday and Hobby
  
  More Properties of this class can be created further."""
  
  def __init__(self, full_name, birthday, hobby):
  self.name = full_name
  self.birthday = birthday #ddmmyyyy
  self.hobby = hobby
  
  # Perform a split in name, creating first name and last name
  name_split = full_name.split(" ")
  self.first_name = name_split[0]
  self.last_name = name_split[1]
  
    def age(self):
    today = datetime.date.today()
    yyyy = int(self.birthday[0:4])  # birthday is a string previously, so need to convert it into int
    mm = int(self.birthday[4:6])
    dd = int(self.birthday[6:8])
    dob = datetime.date(yyyy, mm ,dd) # In here we create a Date of Birth object
    age_in_days = (today - dob).days  # Subtract the 2 Date Object between (Today and DOB)
    age_in_years = age_in_days / 365
    return int(age_in_years)
                          
    
  
  
  
  
# Initiatie 2 users below: Dave John and Knight Frank
user1 = User("Dave John", "01012000","soccer")
user2 = User("Knight Frank", "02022000", "archer")

# Print the age of User1
print("{user1} name is {name} and is {age} years old".format(name=user1.name, age=user1.age))

# Print the age of User2
print("{user2} name is {name} and is {age} years old".format(name=user2.name, age=user2.age))
