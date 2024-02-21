import random

import tkinter


ShieldA = 10
HullA = 15
GunA = 2
print(ShieldA)

dice = random.randrange(10)

print (dice)

ModifierA = 3

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Player:
  def __init__(self, name, age):
    self.name = name
    self.age = age


class Ship:
    def __init__(self, category, manufacturer, dimensions, landingpad, crew, passengers, agility, speed, range, fuel, hull, weapons):
        self.category = category
        self.manufacturer = manufacturer
        self.dimensions = dimensions
        self.landingpad = landingpad
        self.crew = crew
        self.passengers = passengers
        self.agility = agility
        self.speed = speed
        self.range = range
        self.fuel = fuel
        self.hull = hull
        self.weapons = weapons


s1 = Ship(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

print(s1.range)

SpaceShipAgilityA = 8
SpaceshipPilotingA = 1

SpaceShipAgilityB = 8
SpaceshipPilotingB = 1

DefenceA = SpaceShipAgilityA + SpaceshipPilotingA
DefenceB = SpaceShipAgilityB + SpaceshipPilotingB

SmallGimballedPulseLaserA = 15*2
SmallGimballedPulseLaserB = 15*2

def my_function():
  print("Hello from a function")

my_function()

def roll_dice():
    dice = random.randrange(10)
    print ('Function invoked dice is ', dice)

roll_dice()

ShieldAf = 35
ShieldBf = 35

ShieldA = 35
ShieldB = 35

HullA = 50
HullB = 50


SensorA = 2

SensorB = 1

WeaponAccuracyScoreA = 5
WeaponAccuracyScoreB = 5

SpaceShipWeaponsA = 2
SpaceShipWeaponsB = 2

DogFightVariableA = DefenceA + SensorA + random.randrange(10)

DogFightVariableB = DefenceB + SensorB + random.randrange(10)

print('DogFightVariableA is ', DogFightVariableA)
print('DogFightVariableB is ', DogFightVariableB)

FiringAtOpponnetShipRoll = WeaponAccuracyScoreA + SpaceShipWeaponsA + random.randrange(10)

def destructioncheck():
    global ShieldA
    global ShieldB

    print("Checking for destruction")

    if ShieldA < 0:
        print('Player Ship was destroyed')

    if ShieldB < 0:
        print ('ShipB was destroyed')

    print("Checking for destruction")

destructioncheck()


def shieldrecharge():
    global ShieldA
    global ShieldAf

    if  ShieldA < ShieldAf:
        ShieldA = ShieldA + 5
    else: ShieldA = ShieldAf
    print ('ShieldA was partialy charged. Its new value is ', ShieldA )



def dogfight():


    global ShieldA
    global ShieldB


    print('Dogfight output function place holder')
    print('DefenceB score is ', DefenceB)

    if DogFightVariableA > DogFightVariableB:
        print('Player won dogfight round and now can attempt to shoot the enemy.')

        if FiringAtOpponnetShipRoll >= DefenceB:
            print('Firing score is ', FiringAtOpponnetShipRoll)
            print('Player firing score of ', FiringAtOpponnetShipRoll, ' is higher or equal to Defence score of the Enemy that is equal to ', DefenceB, ' resulting in successful hit.')
            ShieldB = ShieldB - SmallGimballedPulseLaserA
            print('ShieldB new value is ', ShieldB)

        if FiringAtOpponnetShipRoll < DefenceB:

            print('Player firing score of ', FiringAtOpponnetShipRoll, ' is lower then Defence score of an enemy that is equal to ' , DefenceB, ' resulting in a miss.')

    elif DogFightVariableA < DogFightVariableB:
        print('Enemy won dogfight round and now can attempt to shoot the Player.')
        if FiringAtOpponnetShipRoll >= DefenceA:
            print('Firing score is ', FiringAtOpponnetShipRoll)
            print('Enemy firing score of ', FiringAtOpponnetShipRoll, ' is higher or equal to Defence score of the Players that is equal to ', DefenceA, ' resulting in successful hit.')
            ShieldA = ShieldA - SmallGimballedPulseLaserB
            print('ShieldA new value is ', ShieldA)

        if FiringAtOpponnetShipRoll < DefenceA:
            print('Enemys firing score of ', FiringAtOpponnetShipRoll, ' is lower than Defence score of the Player that is equal to ' , DefenceA, ' resulting in a miss.')

    else:
        print('Dogfight was a draw and this round you both ended up just circling each other.')

dogfight()

destructioncheck()

shieldrecharge()

destructioncheck()

dogfight()

destructioncheck()



'''FIRING AT AN ENEMY SHIP
When it is your turn to fire you must make a D10 roll,
adding your Spaceship Weapons bonus and your
chosen weapon’s accuracy.
If you equal or exceed the target’s Defence score
the weapon hits. On a roll of 10 you will damage a
component on the ship, providing you manage to
penetrate the shields of the target ship.
(see damaging components).
An immobilised or Sniping target has a
Defence score of 0.'''


'''f FiringAtOpponnetShipRoll >= DefenceB:
    print ('Player firing score of ', FiringAtOpponnetShipRoll,
           ' is higher or equal to Defence score of an enemy that is equal to ' , DefenceB, ' resulting in successful hit.' )
else:
    print ('Player firing score of ', FiringAtOpponnetShipRoll,
           ' is lower then Defence score of an enemy that is equal to ' , DefenceB, ' resulting in miss.')
'''




''' To Hit Bonuses
#To calculate the To-Hit bonuses for each weapon on your ship, add the Accuracy score of the weapon to
your pilot’s Spaceship Weapons bonus. Do this for each
weapon on your ship.'''



'''Agility: 8
Speed: 6
Hull: 50
Shields: 35
WEAPONS
Small: Small Gimballed Pulse Laser, +3 Acc, 10 damages
Small: Small Gimballed Pulse Laser, +3 Acc, 10 damages
s+5 damage vs Shields
UTILITY
Mount 1: Empty
Mount 2: Empty
FIXED COMPONENTS
Bulkhead: Lightweight Alloy (no bonuses)
Power Plant: 2E, 6.4MW output, Str 20
Thrusters: 2E, No bonuses, Str 20
Frame Shift Drive: 2E, Range 7LY, Str 15
Life Support: 1E, Emergency Life Support 5 minutes, Str 15
Power Distributor: 1E, No bonus, Str 10
Sensors: 1E, No bonus, Str 5
INTERNAL COMPONENTS
Size 2: 2E Shield Generator (Shield Power 35, Strength 20)
Size 2: 2E Cargo Rack (Strength 20, Capacity 4)
Size 1: Empty
Size 1: 1E Basic Discovery Scanner (Strength 10, 500 LS range
Bonuses: None
Cargo Capacity: 4T
Range: 7LY
Fuel Tank: 2T (20LY)'''



InitiativeA = 2

InitiativeB = 3

'''Take an Equipment Action
Recharge their shields.
Make a Combat Action.'''

ShieldsA = 35

ShieldRecharge = 5

ShildA = ShieldsA + ShieldRecharge



#print('ShieldsA value is ' , ShildsA)

'''Once your Shield has charged up
to half its starting value it reactivates and begins to
provide protection from weapons again.'''

'''Combat Actions
Broadsides
Disengage
Dogfight
Flight assist o
Pass
Ram'''

'''Dogfight: You attempt to pull behind or above an
enemy ship so that you can shoot it but it can’t shoot
you. You can only Dogfight someone in the up-close
zone. Choose an enemy ship that is also up-close. To
resolve a Dogfight roll a D10 and add it to your Defence
score. The enemy ship does the same. If you score
higher than the enemy, you get behind them. If the
enemy scores higher than you, they get behind you. A
draw means you both spend your turns circling each
other without any effect (although you can still fire a
single turret at each other).
Whichever ship gets behind the other opens fire with all
its weapons. The ship in front cannot fire back except
with a single turret.'''

'''Dogfight: You attempt to pull behind or above an
enemy ship so that you can shoot it but it can’t shoot
you. You can only Dogfight someone in the up-close
zone. Choose an enemy ship that is also up-close. To
resolve a Dogfight roll a D10 and add it to your Defence
score. The enemy ship does the same. If you score
higher than the enemy, you get behind them. If the
enemy scores higher than you, they get behind you. A
draw means you both spend your turns circling each
other without any effect (although you can still fire a
single turret at each other).
Whichever ship gets behind the other opens fire with all
its weapons. The ship in front cannot fire back except
with a single turret.'''

Dogfight = random.randrange(10)
