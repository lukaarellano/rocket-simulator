from rocket import Rocket

# 1 F-1 Engine had an ISP of about 263 seconds and a burn time of 30-40 seconds.

# Rocket(mass, fuel mass, isp in seconds, burn time, drag coefficient, cross-sectional area)

# The drag coefficient (first parameter) can be blunt, conical, or ogive. Blunt represents a shorter rocket, and ogive represents a more slender rocket.

# The cross-sectional area (second parameter) is the radius in meters of the front of the rocket.

alpha1 = Rocket(50100, 45000, 285, 18, 'ogive', 0.9144)

alpha1.ignite_engines()