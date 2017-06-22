#!/usr/bin/env python3
# Author: Rae M.
# 6/22/2017

# Classes in file:
    # SolarSystem- holds the 9 planet child classes and the orbital period calculation logic/fact info
    # Planet- parent to the nine named planet child classes
        # Mercury
        # Venus
        # Earth
        # Mars
        # Jupiter
        # Saturn
        # Uranus
        # Neptune
        # Pluto
    # def Main() has the argument parser for command line arguments
    # solargui.py has the GUI component of the application, which skips def Main() in this file


class Planet(object):
    """
    Base class Planet that is parent to the 9 child planets:
    Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto

    """
    #Defines name, distance, and orbital period, to be overridden in each child's class
    def __init__(self, name, distance=149600000, orbitalPeriod=1.0):
        self.name = name
        self.distanceToSun = distance
        self.orbitalPeriod = orbitalPeriod

    #establish 'getters'
    def getDistanceToSun(self):
        return (self.distanceToSun)

    def getName(self):
        return (self.name)

    def getOrbitalPeriod(self):
        return (self.orbitalPeriod)

    #planet's basic info, returned on -verbose but updated for each planet's individual facts
    def info(self):
        return ("The planet " + self.getName() + " is " \
                + str(self.getDistanceToSun()) + "km to its sun and takes " \
                + str(self.getOrbitalPeriod()) + " Earth years to orbit its sun.")

    #set up setters
    def setDistanceToSun(self, distance):
        self.distanceToSun = distance

    def setName(self, name):
        self.name = name

    def setOrbitalPeriod(self, orbitalPeriod):
        self.orbitalPeriod = orbitalPeriod

class Mercury(Planet):
    def __init__(self):
        #sets up Mercury's unique properties. Polymorphism and inheritence in action
        Planet.__init__(self, "Mercury", 70000000, 4.14)
        self.radius = 0.3829
        self.spacecraft = ["Mariner 10", "MESSENGER"]

    def getRadius(self):
        #Returns Mercury's radius relative to Earth's
        return(self.radius)

    def getSpacecraft(self):
        #Returns a list of spacecraft what have visited Mercury
        return(self.spacecraft)

    def info(self):
        return ("The planet " + self.getName() + " is " \
                + str(self.getDistanceToSun()) + "km to its sun and takes " + "\n"
                + str(self.getOrbitalPeriod()) + " Earth years to orbit its sun."+ "\n"
                + "Its radius is " + str(self.getRadius()) + " Earths." + "\n"
                + str(self.getSpacecraft()) + " are spacecraft that have visited this planet"+ "\n" )

class Venus(Planet):
    def __init__(self):
        Planet.__init__(self, "Venus", 108200000, 1.62)
        self.radius = 0.9499
        self.temp = 462

    def getRadius(self):
        #Returns Venus's radius relative to Earth's
        return(self.radius)

    def getTemp(self):
        #Returns Venus's avg surface temperature in celsius
        return(self.temp)

    def info(self):
        return ("The planet " + self.getName() + " is " + "\n"
                + str(self.getDistanceToSun()) + "km to its sun and takes "+ "\n"
                + str(self.getOrbitalPeriod()) + " Earth years to orbit its sun."+ "\n"
                + "Its radius is " + str(self.getRadius()) + " Earths."+ "\n"
                + "Its average surface temperature is " + str(self.getTemp())+ "\n"  )

class Earth(Planet):
    #  This is the initialization method for Earth.  This will run every time
    #  an Earth is created.  Notice there are no input parameters.
    def __init__(self):
        Planet.__init__(self, "Earth", 150000000, 1.0)
        self.oceanList = ["Pacific", "Atlantic", "Indian", "Southern", "Artic"]
        self.continentList = ["North America", "South America", "Antarctica",\
                              "Africa", "Europe", "Asia", "Australia"]

    def getContinents(self):
        #Returns the list of continents.

        return (self.continentList)

    def getOceans(self):
        #Returns the list of oceans.
        return (self.oceanList)

    def info(self):
        return ("The planet " + self.getName() + " is " + "\n"
                + str(self.getDistanceToSun()) + "km to its sun and takes " + "\n"
                + str(self.getOrbitalPeriod()) + " Earth years to orbit its sun."+ "\n"
                + "Its oceans names are " + str(self.getOceans()) + "\n"  "and its continents are "
                + str(self.getContinents()) + "\n" )

class Mars(Planet):

    def __init__(self):
        Planet.__init__(self, "Mars", 227900000, 0.53)
        self.radius = 0.532
        self.moons = ["Phobos", "Deimos"]

    def getRadius(self):
        #Returns Mars's radius relative to Earth's
        return(self.radius)

    def getMoons(self):
        #returns a list of Mars's two moons
        return(self.moons)

    def info(self):
        return ("The planet " + self.getName() + " is " + "\n"
                + str(self.getDistanceToSun()) + "km to its sun and takes " + "\n"
                + str(self.getOrbitalPeriod()) + " Earth years to orbit its sun." + "\n"
                + "Its radius is " + str(self.getRadius()) + " Earths."+ "\n"
                + "Its Moons are " + str(self.getMoons()) + "\n" )

class Jupiter(Planet):

    def __init__(self):
        Planet.__init__(self, "Jupiter", 778400000, 0.084)
        self.radius = 10.983
        self.galMoons = ["Io", "Europa", "Ganymede", "Callisto"]

    def getRadius(self):
        #Returns Jupiter's average radius relative to Earth's
        return(self.radius)

    def getGalMoons(self):
        #Returns a list of Jupiter's Galilean moons
        return(self.galMoons)

    def info(self):
        return ("The planet " + self.getName() + " is " + "\n"
                + str(self.getDistanceToSun()) + "km to its sun and takes " + "\n"
                + str(self.getOrbitalPeriod()) + " Earth years to orbit its sun." + "\n"
                + "Its radius is " + str(self.getRadius()) + " Earths." + "\n"
                + "Its Galilean moons are " + str(self.getGalMoons()) + "\n" )

class Saturn(Planet):

    def __init__(self):
        Planet.__init__(self, "Saturn", 1429000000, .0331)
        self.radius = 9.001
        self.bigMoons = ["Mimas", "Enceladus", "Tethys", "Dione", "Titan", \
                         "Rhea", "Lapetus", "Hyperion", "Phoebe", "Janus", \
                         "Epimetheus", "Prometheus", "Pandora"]


    def getRadius(self):
        #Returns Saturn's average radius relative to Earth's
        return(self.radius)

    def getBigMoons(self):
        #Returns a list of Saturn's moons that have a diameter of 50km or larger
        return(self.bigMoons)

    def info(self):
        return ("The planet " + self.getName() + " is " + "\n"
                + str(self.getDistanceToSun()) + "km to its sun and takes " + "\n"
                + str(self.getOrbitalPeriod()) + " Earth years to orbit its sun."+ "\n" \
                + "Its radius is " + str(self.getRadius()) + " Earths." + "\n"
                + "Its biggest moons are " + str(self.getBigMoons()) + "\n" )

class Uranus(Planet):
    def __init__(self):
        Planet.__init__(self, "Uranus", 2871000000, 0.0117)
        self.radius = 3.968
        self.moons = ["Miranda", "Ariel", "Umbriel", "Titania", "Oberon"]

    def getRadius(self):
        #Returns Uranus's radius relative to Earth's
        return(self.radius)

    def getMoons(self):
        #Returns a list of Uranus's major moons
        return(self.moons)

    def info(self):
        return ("The planet " + self.getName() + " is " + "\n"
                + str(self.getDistanceToSun()) + "km to its sun and takes " + "\n"
                + str(self.getOrbitalPeriod()) + " Earth years to orbit its sun." + "\n"
                + "Its radius is " + str(self.getRadius()) + " Earths." + "\n"
                + "Its major moons are " + str(self.getMoons()) + "\n" )

class Neptune(Planet):
    def __init__(self):
        Planet.__init__(self, "Neptune", 4498000000, 0.00606)
        self.radius = 3.856
        self.moons = ["Naiad", "Thalassa", "Despina", "Galatea", "Larissa", "S/2004 N 1", "Proteus",\
                      "Triton", "Nereid", "Halimede", "Sao", "Laomedeia", "Psamathe", "Neso"]

    def getRadius(self):
        #Returns Neptune's radius relative to Earth's
        return(self.radius)

    def getMoons(self):
        #Returns a list of Neptune's major moons
        return(self.moons)

    def info(self):
        return ("The planet " + self.getName() + " is " + "\n"
                + str(self.getDistanceToSun()) + "km to its sun and takes " + "\n"
                + str(self.getOrbitalPeriod()) + " Earth years to orbit its sun." + "\n"
                + "Its radius is " + str(self.getRadius()) + " Earths." + "\n"
                + "Its moons are " + str(self.getMoons()) + "\n"  )

class Pluto(Planet):

    def __init__(self):
        Planet.__init__(self, "Pluto", 5906292480, 0.00405)
        self.radius = 0.1868
        self.moons = ["Charon", "Styx", "Nix", "Kerberos", "Hydra"]

    def getRadius(self):
        #Returns Pluto's average radius relative to Earth's
        return(self.radius)
    def getMoons(self):
        #Returns a list of Pluto's moons
        return(self.moons)

    def info(self):
        return ("The planet " + self.getName() + " is " + "\n"
                + str(self.getDistanceToSun()) + "km to its sun and takes " + "\n"
                + str(self.getOrbitalPeriod()) + " Earth years to orbit its sun." + "\n"
                + "Its radius is " + str(self.getRadius()) + " Earths." + "\n"
                + "Its moons are " + str(self.getMoons()) + "\n" )


class SolarSystem(object):
    def __init__(self):
        self.mercury = Mercury()
        self.venus = Venus()
        self.earth = Earth()
        self.mars = Mars()
        self.jupiter = Jupiter()
        self.saturn = Saturn()
        self.uranus = Uranus()
        self.neptune = Neptune()
        self.pluto = Pluto()

        self.planetList = [self.mercury, self.venus, self.earth, self.mars, self.jupiter, self.saturn, self.uranus, self.neptune, self.pluto]

    #collects and prints all 9 planet's info methods and prints them
    def allInfo(self):
        for planet in self.planetList:
            print(planet.info())
    def getNumOrbits(self, orbitdays):
        """
            Calculates the number of orbits using the number of elapsed earth days as an input

        """
        allorbits = ""
        for planet in self.planetList:
            orbit = (orbitdays * planet.getOrbitalPeriod())/365
            orbit = format(orbit, '.3f')
            orbitstring = str(orbit)
            orbitoutput = planet.getName() + " has orbited the sun " + orbitstring + " times."
            allorbits += orbitoutput + "\n"
        return allorbits
def main():

    from argparse import ArgumentParser
    parser = ArgumentParser()

    #command line version of the application.
    #use -v for more information on each planet
    parser.add_argument("orbitdays", type=int, help="display how many orbits the planet has made around the sun")
    parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")

    args = parser.parse_args()

    solarsystem = SolarSystem()

    if args.verbose:
        print(solarsystem.allInfo())
        print(solarsystem.getNumOrbits(args.orbitdays))
    else:
        print(solarsystem.getNumOrbits(args.orbitdays))

if (__name__ == "__main__"):
    main()
