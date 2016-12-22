#-------------------------------------------------------------------------------
# ADJSIM SIMULATION FRAMEWORK - JUPITER MOON SYSTEM
# Designed and developed by Sever Topan
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# IMPORTS
#-------------------------------------------------------------------------------
import random
from environment import *
from constants import *
from PyQt4 import QtGui, QtCore

#-------------------------------------------------------------------------------
# CONSTANTS
#-------------------------------------------------------------------------------

GRAV_CONSTANT = 6.674e-11
TIMESTEP_LENGTH = 10000
DISTANCE_MULTIPLIER = 10000000

#-------------------------------------------------------------------------------
# ABILITIES
#-------------------------------------------------------------------------------

# ABILITY - SETUP
#-------------------------------------------------------------------------------
# !!! predicates will be grouped toget\er for ease of writing
# !!! always sort predicate list before insertion into class
def calculateSetup_predicate_self(target):
   if target.traits.get('type') is not None \
       and target.traits.get('castLog_acc') is not None \
       and target.blockedDuration is 0 \
       and target.abilities['calculateSetup'].blockedDuration is 0:
       return True
   else:
       return False

def calculateSetup_predicate_env(target):
   return True

calculateSetup_predicateList = [TargetPredicate(TargetPredicate.ENVIRONMENT, calculateSetup_predicate_env), \
   TargetPredicate(TargetPredicate.SOURCE, calculateSetup_predicate_self)]


calculateSetup_condition = lambda targetSet: True

def calculateSetup_effect(targetSet, conditionality):
   if conditionality is UNCONDITIONAL:
       return

   targetSet.source.traits['xAcc'].value = 0;
   targetSet.source.traits['yAcc'].value = 0;

   targetSet.source.traits['castLog_acc'].value.clear()

   targetSet.source.abilities['calculateSetup'].blockedDuration = 1
   targetSet.source.abilities['calculateAcc'].blockedDuration = 0
   targetSet.source.abilities['calculateVel'].blockedDuration = 0



# ABILITY - CALCULATE ACCELERATION
#-------------------------------------------------------------------------------
# !!! predicates will be grouped together for ease of writing
# !!! always sort predicate list before insertion into class
def calculateAcc_predicate_target(env, sel, target):
   if target is not env \
       and target is not sel \
       and target.traits.get('type') is not None \
       and target.traits.get('mass') is not None:
       return True
   else:
       return False

def calculateAcc_predicate_self(target):
   if target.traits.get('type') is not None \
       and target.traits.get('castLog_acc') is not None \
       and target.blockedDuration is 0 \
       and target.abilities['calculateAcc'].blockedDuration is 0:
       return True
   else:
       return False

def calculateAcc_predicate_env(target):
   return True

calculateAcc_predicateList = [TargetPredicate(TargetPredicate.ENVIRONMENT, calculateAcc_predicate_env), \
   TargetPredicate(TargetPredicate.SOURCE, calculateAcc_predicate_self), \
   TargetPredicate(0, calculateAcc_predicate_target)]


calculateAcc_condition = lambda targetSet: targetSet.targets[0].traits['type'].value is 'planet' \
   and not targetSet.source.traits['castLog_acc'].value & {targetSet.targets[0]} \
   and targetSet.environment.traits['numPhysicsDependentAgents'].value > len(targetSet.source.traits['castLog_acc'].value)

def calculateAcc_effect(targetSet, conditionality):
   if conditionality is UNCONDITIONAL:
       return

   xDist = (targetSet.targets[0].xCoord - targetSet.source.xCoord) * DISTANCE_MULTIPLIER
   yDist = (targetSet.targets[0].yCoord - targetSet.source.yCoord) * DISTANCE_MULTIPLIER
   absDist = (xDist**2 + yDist**2)**0.5
   absAcc = targetSet.targets[0].traits['mass'].value * GRAV_CONSTANT / (absDist**2)

   targetSet.source.traits['xAcc'].value += absAcc * (xDist / absDist)
   targetSet.source.traits['yAcc'].value += absAcc * (yDist / absDist)

   targetSet.source.traits['castLog_acc'].value.add(targetSet.targets[0])


# ABILITY - CALCULATE VELOCITY
#-------------------------------------------------------------------------------
# !!! predicates will be grouped together for ease of writing
# !!! always sort predicate list before insertion into class
def calculateVel_predicate_self(target):
   if target.traits.get('type') is not None \
       and target.blockedDuration is 0 \
       and target.abilities['calculateVel'].blockedDuration is 0:
       return True
   else:
       return False

def calculateVel_predicate_env(target):
   return True

calculateVel_predicateList = [TargetPredicate(TargetPredicate.ENVIRONMENT, calculateVel_predicate_env), \
   TargetPredicate(TargetPredicate.SOURCE, calculateVel_predicate_self)]

calculateVel_condition = lambda targetSet: \
   targetSet.environment.traits['numPhysicsDependentAgents'].value - 1 == len(targetSet.source.traits['castLog_acc'].value)

def calculateVel_effect(targetSet, conditionality):
   if conditionality is UNCONDITIONAL:
       return

   targetSet.source.traits['xVel'].value += targetSet.source.traits['xAcc'].value * TIMESTEP_LENGTH
   targetSet.source.traits['yVel'].value += targetSet.source.traits['yAcc'].value * TIMESTEP_LENGTH

   targetSet.source.xCoord += targetSet.source.traits['xVel'].value * TIMESTEP_LENGTH / DISTANCE_MULTIPLIER
   targetSet.source.yCoord += targetSet.source.traits['yVel'].value * TIMESTEP_LENGTH / DISTANCE_MULTIPLIER

   targetSet.source.abilities['calculateAcc'].blockedDuration = 2
   targetSet.source.abilities['calculateVel'].blockedDuration = 2

#-------------------------------------------------------------------------------
# AGENT GENERATION FUNCTIONS
#-------------------------------------------------------------------------------

# PLANET CREATION FUNCTION
#-------------------------------------------------------------------------------

def createPlanet(name, mass, size, color, xPos, yPos, xVel, yVel, environment, style = QtCore.Qt.SolidPattern):
   planet = Agent(environment, name, xPos, yPos)
   planet.addTrait('type', 'planet')
   planet.addTrait('xVel', xVel)
   planet.addTrait('yVel', yVel)
   planet.addTrait('xAcc', 0.0)
   planet.addTrait('yAcc', 0.0)
   planet.addTrait('mass', mass)
   planet.addTrait('castLog_acc', set())
   planet.size = size
   planet.color = color
   planet.style = style

   planet.abilities["calculateSetup"] = Ability(environment, "calculateSetup", planet, \
       calculateSetup_predicateList, calculateSetup_condition, calculateSetup_effect)
   planet.abilities["calculateAcc"] = Ability(environment, "calculateAcc", planet, \
       calculateAcc_predicateList, calculateAcc_condition, calculateAcc_effect)
   planet.abilities["calculateVel"] = Ability(environment, "calculateVel", planet, \
       calculateVel_predicateList, calculateVel_condition, calculateVel_effect)
   planet.abilities["calculateAcc"].blockedDuration = 2
   planet.abilities["calculateVel"].blockedDuration = 2

   environment.agentSet.add(planet)

#-------------------------------------------------------------------------------
# AGENT CREATION SCRIPT
#-------------------------------------------------------------------------------

# jupiter system
createPlanet('jupiter', 1.898e27, 10, QtGui.QColor(ORANGE), 0, 0, 0.0 , 0, environment, QtCore.Qt.Dense1Pattern)
createPlanet('io', 8.9e22, 3, QtGui.QColor(GREY), 42, 0, 0.0, 17.38e3, environment)
createPlanet('europa', 4.8e22, 3, QtGui.QColor(BLUE_LIGHT), 67, 0, 0.0, 13.7e3, environment)
createPlanet('ganymede', 1.48e23, 5, QtGui.QColor(RED_DARK), 107, 0, 0.0, 10.88e3, environment)
createPlanet('callisto', 1.08e23, 4, QtGui.QColor(BROWN_LIGHT), 188, 0, 0.0, 8.21e3, environment)

environment.addTrait('numPhysicsDependentAgents', 5)
