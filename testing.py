
#Note: please enter distance_from_sun in millions of kilometers
## CODING CHALLENGE
# 25 MARKS
"""
A] Design a parent class called Planet

It must have:
- General attributes: name, distance_from_sun, planet_type
- A get_distance_to_earth() method that gives you the absolute distance from the Earth.

!!! You can take the distance from the Sun to the Earth as 147 million kilometres !!!

For example, if the planet’s distance_from_sun was 148 million kilometres when you call the get_distance_from_earth()
method, it should give us the distance like this: {'distance to earth’': 1000000} where the implied unit is kilometres.
This means that the planet is 1 million kilometres away from Earth.

   > This question uses an oversimplification of the solar system model, not taking into account orbit position or the
    eccentricity of the orbit, so in reality the result will be an approximate value with a reasonable margin of error.
"""
import math
class Planet:
    def __init__(self, name, distance_from_sun, planet_type):
        self.name = name
        self.distance_from_sun = distance_from_sun 
        self.planet_type = planet_type 

    def get_distance_to_earth(self):
        # distance_to_earth is the distance_from_sun minus 147 million kilometers (distance between earth and the sun)
        # int and abs used to ensure the result is a positive integer, which is returned with the implied unit of km
        self.distance_to_earth = abs(self.distance_from_sun - 147)
        return {'distance to earth': self.distance_to_earth * 1000000}


"""
B] Design a child class called Mercury, which inherits from the Planet class.
This class should have exactly the same attributes as its parent class,
Your child class should also have a static method called happy_new_year(), which
would give us the information on how long a year lasts on the planet (in whatever way you wish!). 
You can take Earth Days as the implied unit.

After, create a Mercury object and print out the value of all its attributes and methods.

!!! HELPFUL INFO ABOUT MERCURY !!!
Distance from Sun: 58 million
Planet Type: Terrestrial
Time taken for the planet to orbit the sun: 88 Earth days
!!!!!!!!!!!!!!!!!!!!

"""

class Mercury(Planet):
    def __init__(self, name, distance_from_sun, planet_type):
        super().__init__(name, distance_from_sun, planet_type)

    # equation to estimate length of a year in Earth days 
    #days = 365 * sqrt(a^3) where a is the distance_from_sun/distance_to_earth
    @staticmethod
    def happy_new_year(dist_from_sun):
        a = dist_from_sun / 147 #distance from earth to the sun
        days = 365 * math.sqrt(a**3)
        return {'A year on this planet lasts': days} 
    
"""
C] Design a child class called Jupiter, which inherits from the Planet class.
This class should have exactly the same attributes as its parent class, as well as the additional attribute 
number_of_moons.
Your child class should also have a static method called happy_new_year(), which would give us the information on how 
long a year lasts on the planet (in whatever way you wish!). You can take Earth Days as the implied unit.

After, create a Jupiter object and print out the value of all its attributes and methods.


!!! HELPFUL INFO ABOUT JUPITER !!!
Distance from Sun: 779 million
Planet Type: Gas Giant
Time taken for the planet to orbit the sun: 4383 Earth days
Number of Moons: 80
!!!!!!!!!!!!!!!!!!!!

"""

class Jupiter(Planet):
    def __init__(self, name, distance_from_sun, planet_type, number_of_moons):
        super().__init__(name, distance_from_sun, planet_type)
        self.number_of_moons = number_of_moons

    # equation to calculate length of a year  in Earth days 
    #days = 365 * sqrt(a^3) where a is the distance_from_sun/distance_to_earth
    @staticmethod
    def happy_new_year(dist_from_sun):
        a = dist_from_sun / 147 #distance from earth to the sun
        days = 365 * math.sqrt(a**3)
        return {'A year on this planet lasts': days} 


#Test cases
p1 = Planet('Mars', 22, 'Terrestrial')
print('from Mars:')
print(p1.get_distance_to_earth())

m = Mercury('Mercury', 58, 'Terrestrial')
print('from Mercury:')
print(m.get_distance_to_earth())
print(m.happy_new_year(58))

j = Jupiter('Jupiter', 779, 'Terrestrial', 80)
print('from Jupiter:')
print(j.get_distance_to_earth())
print(j.happy_new_year(779))