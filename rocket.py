# The final version of this will be readable ❤️.

import math
from time import sleep

class Rocket:
    def __init__(self, mass, fuel, isp, burn_time):
        self.mass = mass
        self.fuel = fuel
        self.isp = isp
        self.burn_time = burn_time
        self.initial_mass = self.mass
        self.dry_mass = self.mass - self.fuel
    def get_deltav(self):
        self.deltav = float(math.log(self.mass / self.dry_mass)) * 9.81 * float(self.isp)
        return self.deltav
    def get_thrust(self):
        self.mass_flow_rate = self.fuel / self.burn_time
        self.thrust = self.mass_flow_rate * self.isp * 9.81
        return self.thrust, self.mass_flow_rate
    def ignite_engines(self, shape, radius):
        self.cross_sectional_area = math.pi * radius ** 2
        pitch = 90
        self.y = 0
        self.x = 0
        gravity = 9.81
        self.acceleration = 0
        self.velocity = 0
        self.initial_acceleration = self.thrust/self.mass - 9.81
        self.acceleration_drag = 0
        self.acceleration_drag_x = 0
        self.acceleration_drag_y = 0
        print("Engines ignited!")
        while self.fuel > 1:
            pitch = math.radians(0) + (math.radians(90) - math.radians(0)) * math.e ** -(0.0001 * self.y)
            dt = 0.5  # seconds
            self.velocity += self.acceleration * dt
            self.velocity_x = self.velocity * math.cos(pitch)
            self.velocity_y = self.velocity * math.sin(pitch)
            self.air_pressure = 1.225 * math.e ** (-self.y / 8500)
            self.drag = 1/2 * self.air_pressure * shape * self.cross_sectional_area * self.velocity ** 2
            if self.velocity > 0:
                self.acceleration_drag = self.drag / self.mass
                self.acceleration_drag_x = self.drag / self.mass * self.velocity_x / self.velocity
                self.acceleration_drag_y = self.drag / self.mass * self.velocity_y / self.velocity
            else: pass
            self.acceleration = self.thrust/self.mass - gravity - self.acceleration_drag
            self.acceleration_x = self.thrust/self.mass * math.cos(pitch) - self.acceleration_drag_x
            self.acceleration_y = self.thrust/self.mass * math.sin(pitch) - self.acceleration_drag_y
            self.mass -= self.mass_flow_rate * dt
            gravity = 9.81 * (6371000/(6371000+self.y))**2
            self.fuel -= self.mass_flow_rate * dt
            self.deltav = self.isp * 9.81 * math.log(self.mass / self.dry_mass)
            self.y += self.velocity_y * dt 
            self.x += self.velocity_x * dt
            print("DeltaV: " + str(round(self.deltav)) + " m/s.")
            print("Total Velocity: " + str(round(self.velocity)) + " m/s.")
            print("Vertical Velocity: " + str(round(self.velocity)) + " m/s.")
            print("Horizontal Velocity " + str(round(self.velocity_x)) + " m/s.")
            print("Height/y-coordinate: " + str(round(self.y)) + " meters.")
            print("x-coordinate: " + str(round(self.x)) + " units.")
            print("Gravity: " + str(round(gravity, 3)) + " m/s.")
            print("Pitch: " + str(round(math.degrees(pitch))) + " degrees.")
            print("------------------------------------")
            sleep(1)
        self.apoapsis = self.y + (self.velocity**2) / (2 * gravity)
        print("Apoapsis: " + str(round(self.apoapsis)) + " meters.")
        print("Fuel depleted")