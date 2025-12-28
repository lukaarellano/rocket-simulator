import math
from time import sleep
from random import uniform

## -- CONSTANTS --
G0 = 9.81
k = 0.0001
dt = 0.5
scale_height = 8500.0

class Rocket:
    def __init__(self, mass, fuel, isp, burn_time, shape, radius):
        # - MASS PROPERTIES -
        self.mass = mass
        self.fuel = fuel
        self.initial_mass = self.mass
        self.dry_mass = self.mass - self.fuel
        self.radius = radius
        self.shape = shape
        self.cross_sectional_area = math.pi * self.radius ** 2

        # - ENGINE PROPERTIES -
        self.isp = isp
        self.burn_time = burn_time
        self.deltav = float(math.log(self.mass / self.dry_mass)) * G0 * float(self.isp)
        self.mass_flow_rate = self.fuel / self.burn_time
        self.thrust = self.mass_flow_rate * self.isp * G0

        # - STATE -
        self.y = 0.0
        self.x = 0.0
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self.pitch = math.radians(90.0)

        self.get_drag_coefficient(shape)

    # -- HELPERS --
    def get_drag_coefficient(self, shape):
        if shape == "ogive":
            self.shape = 0.3
        elif shape == "conical":
            self.shape = 0.5
        elif shape == "blunt":
            self.shape = 0.75
        else:
            self.shape = uniform(0.3, 0.75)

    def modify_pitch(self, pitch):
        end_pitch = 0
        start_pitch = 90
        pitch = math.radians(end_pitch) + (math.radians(start_pitch) - math.radians(end_pitch)) * math.e ** -(k * self.y)
        return pitch

    def print_status(self, deltav, velocity, velocity_y, velocity_x, y, x, gravity, pitch):
        print("DeltaV: " + str(round(deltav)) + " m/s.")
        print("Total Velocity: " + str(round(velocity)) + " m/s.")
        print("Vertical Velocity: " + str(round(velocity_y)) + " m/s.")
        print("Horizontal Velocity " + str(round(velocity_x)) + " m/s.")
        print("Height/y-coordinate: " + str(round(y)) + " meters.")
        print("x-coordinate: " + str(round(x)) + " units.")
        print("Gravity: " + str(round(gravity, 3)) + " m/s.")
        print("Pitch: " + str(round(math.degrees(pitch))) + " degrees.")
        print("Apoapsis: " + str(round(self.apoapsis)) + " meters.")
        print("------------------------------------")

    # -- SIMULATION --
    def ignite_engines(self):
        print("Engines ignited!")
        gravity = 9.81

        self.acceleration = 0
        self.velocity = 0
        self.initial_acceleration = self.thrust/self.mass - G0

        self.acceleration_drag = 0
        self.acceleration_drag_x = 0
        self.acceleration_drag_y = 0

        while self.fuel > 1:
            # - PHYSICS -
            self.velocity += self.acceleration * dt
            self.velocity_x = self.velocity * math.cos(self.pitch)
            self.velocity_y += self.thrust/self.mass * math.sin(self.pitch) - gravity - self.acceleration_drag_y * dt

            self.air_pressure = 1.225 * math.e ** (-self.y / scale_height)
            self.drag = 1/2 * self.air_pressure * self.shape * self.cross_sectional_area * self.velocity ** 2

            if self.velocity > 0:
                self.acceleration_drag = self.drag / self.mass
                self.acceleration_drag_x = self.drag / self.mass * self.velocity_x / self.velocity
                self.acceleration_drag_y = self.drag / self.mass * self.velocity_y / self.velocity
            else: pass

            self.acceleration = self.thrust/self.mass - gravity - self.acceleration_drag
            self.acceleration_x = self.thrust/self.mass * math.cos(self.pitch) - self.acceleration_drag_x
            self.acceleration_y = self.thrust/self.mass * math.sin(self.pitch) - self.acceleration_drag_y - gravity

            self.mass -= self.mass_flow_rate * dt
            gravity = G0 * (6371000/(6371000+self.y))**2
            self.fuel -= self.mass_flow_rate * dt
            self.deltav = self.isp * G0 * math.log(self.mass / self.dry_mass)

            self.y += self.velocity_y * dt 
            self.x += self.velocity_x * dt

            self.apoapsis = self.y + (self.velocity**2) / (2 * gravity)
            self.pitch = self.modify_pitch(self.pitch)
            self.print_status(self.deltav, self.velocity, self.velocity_y, self.velocity_x, self.y, self.x, gravity, self.pitch)
            sleep(1)
        print("Fuel depleted.")