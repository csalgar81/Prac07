"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
"""
from Prac07.car import Car


def main():
    """bus = Car()
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)

    limo = Car(100, 'limon')
    limo.add_fuel(20)
    print("fuel of limo = ", limo.fuel)
    limo.drive(115)
    print("odo of limo = ",limo.odometer)
    print(str(limo))
    print(limo)
    str(limo)
    """

    camion_object = Car('hhh','34')

    print(camion_object)


#    print("Car {}, {}".format(bus.fuel, bus.odometer))
#    print("Car {self.fuel}, {self.odometer}".format(self=bus))

main()