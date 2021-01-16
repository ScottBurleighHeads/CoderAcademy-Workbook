import random                           # Importing library random that has a list of methods that can used. 

class Car:                              # Declaring a class car.

    def __init__(self, brand):          # The init method declares attributes to 
                                        # be declared when calling the class or making an instance of the class
        
        self.car_name = brand           # Variable belonging to the init object. Declaring the input from the 
                                        # user is equal to the instance variable. 

    def present(self):                          # Declaring a new method present.

        return 'I have a ' + self.car_name      # Returns a string when the method was called saying 
                                                # 'I have a {brand}'

class Model(Car):                         # Declaring a new class that inherits from car.
    def __init__(self, brand, mod):       # Declaring init method that requires two arguments.
        super().__init__(brand)           # Gives you access to methods from the superclass Car
        self.model = mod                  # Declaring parameters mod into the instance variable self.model

    def show(self):
        return self.present() + ', it was made in ' + str(self.model)   # Returns a string with Car instance 
                                                                        # variable self.present and self.model which 
                                                                        # the type has been changed to a string type.

makes = ["Ford", "Holden", "Toyota"]    # Makine a list of models
models = []                             # Declaring an empty list so it can be used in the for loop
for i in range(40):                     # loop where i is an item of ranger 40. Basically i crements from 0 to 39
    models.append(i+1980)               # concatanate a list starting from 1980 to 2020 

def random_int_from_interval(min,max):  # declaring a function that has a minimum and maximum range
    return random.randint(min, max)     # Return a single integer value in the range given in min to max

for model in models:      # Make a loop that is aslong as the list models and save the item list into variable model
                          # to be used elsewhere. 
    
    make = makes[random_int_from_interval(0, len(makes)-1)]     # Pick a random make of car to save in the list makes
    model = models[random_int_from_interval(0, len(makes)-1)]   # Pick a random number between 1980 - 2020
    my_car = Model(make, model) # An instance of the Model class
    print(my_car.show())        # Prints the instance of the class my_car  