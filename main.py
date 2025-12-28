from rocket import Rocket
# 1 F-1 Engine had an ISP of about 263s and a burn time of 30-40 seconds.
# 1 Merlin-1D Engine had an ISP of about 285 and a burn time of 18 seconds (if you divide the burn time of all 9 engines in the Falcon 9 by 9).
# Rocket(mass, fuel mass, isp, burn time)

#mass = 1,100 + 4,000 + 40,000

alpha1 = Rocket(50100, 45000, 285, 18)
alpha1.get_deltav()
alpha1.get_thrust()

alpha1.ignite_engines()