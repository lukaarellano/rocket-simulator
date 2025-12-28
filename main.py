from rocket import Rocket
# 1 F-1 Engine had an ISP of about 263s and a burn time of 30-40 seconds.
# Rocket(mass, fuel mass, isp, burn time)

#mass = 1,100 + 4,000 + 32,000

alpha1 = Rocket(37100, 32000, 263, 35)
alpha1.get_deltav()
alpha1.get_thrust()

alpha1.ignite_engines()