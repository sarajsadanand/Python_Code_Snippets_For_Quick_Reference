###################################################################################
'''# importing the module
import pandas as pd

# creating a sample dataframe
data = pd.DataFrame({'Brand': ['Maruti', 'Hyundai', 'Tata',
                               'Mahindra', 'Maruti', 'Hyundai',
                               'Renault', 'Tata', 'Maruti'],
                     'Year': [2012, 2014, 2011, 2015, 2012,
                              2016, 2014, 2018, 2019],
                     'Kms Driven': [50000, 30000, 60000,
                                    25000, 10000, 46000,
                                    31000, 15000, 12000],
                     'City': ['Gurgaon', 'Delhi', 'Mumbai',
                              'Delhi', 'Mumbai', 'Delhi',
                              'Mumbai', 'Chennai', 'Ghaziabad'],
                     'Mileage': [28, 27, 25, 26, 28,
                                 29, 24, 21, 24]})

# displaying the DataFrame
display(data)
'''

###################################################################################
'''
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('Run...')


player1 = PlayerCharacter("Saraj", 22)
print(player1.name)
'''
###################################################################################
'''def super_func(*args, **kwargs):
    print(args)   # args as a tuple
    print(kwargs)  # this returns keyword arguments as a dict
    total = 0
    for i in kwargs.values():
        total += i
    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num1=10, num2=20))
'''


###################################################################################
'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def oldest_student(*args):
    return max(args)


s1 = Student('Saraj', 22)
s2 = Student('San', 33)
s3 = Student('Sai', 34)

print(f"The oldest student is {oldest_student(s1.age, s2.age, s3.age)} year old.")
'''
###################################################################################

