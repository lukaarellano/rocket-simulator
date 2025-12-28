import math
from time import sleep

class Rocket:
    def __init__(self, mass, fuel, isp, burn_time):
        self.mass = mass
        self.fuel = fuel
        self.isp = isp
        self.burn_time = burn_time
    def get_deltav(self):
        self.deltav = float(math.log(self.mass/(self.mass-self.fuel))) * 9.81 * float(self.isp)
        return self.deltav
    def get_thrust(self):
        self.mass_flow_rate = self.fuel / self.burn_time
        self.thrust = self.mass_flow_rate * self.isp * 9.81
        return self.thrust, self.mass_flow_rate
    def ignite_engines(self):
        self.acceleration = 0
        self.velocity = 0
        self.height = 0
        self.initial_acceleration = self.thrust/self.mass - 9.81
        print("Engines ignited!")
        while self.fuel > 1:
            self.mass = self.mass - self.mass_flow_rate
            self.fuel = self.fuel - self.mass_flow_rate
            self.deltav = float(math.log(self.mass/(self.mass-self.fuel))) * 9.81 * float(self.isp)
            self.acceleration = self.thrust/self.mass - 9.81
            self.average_acceleration = (self.initial_acceleration + self.acceleration) / 2
            self.velocity += self.average_acceleration
            self.average_velocity = (self.deltav / 2)
            self.height += self.velocity
            print("DeltaV: " + str(round(self.deltav)) + " m/s.")
            print("Velocity: " + str(round(self.velocity)) + " m/s.")
            print("Height: " + str(round(self.height)) + " meters.")
            print("------------------------------------")
            sleep(1)
        self.apoapsis = self.height + ((self.velocity * self.velocity) / (9.81 * 2))
        print("Apoapsis: " + str(round(self.apoapsis)) + " meters.")
        print("Fuel depleted")