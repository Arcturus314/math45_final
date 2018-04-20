#Kaveh Pezeshki
#4/13/2018
#Differential Equation Project Rocket Simulator

import math

theta = math.pi/20 #temporary value to optimize
height = 60 #70m tall
fuel_density = 600 #kg m^-3
fuel_ejection_rate = 56100 #kg s^-1
air_density  = 1.225 #kg m^-3
other_vol =  1200 #m^3
other_mass = 25600 #kg

time = 0 #start time of 0
vel = 0  #start velocity of 0
alt = 0 #start altitude of 0

g = 9.81 #gravity constant m s^-2
exhaust_speed = 3000 #speed fuel is ejected at, ms^-1

rocket_radius  = height*math.tan(theta)
rocket_volume  = math.pi*math.pow(rocket_radius,2)*height/3
fuel_volume    = rocket_volume - other_vol
init_fuel_mass = fuel_density * fuel_volume
drag_coeff     = air_density * math.pi * math.pow(rocket_radius, 2) * (1 - math.cos(2*theta))

print("The rocket has a volume of: " + str(rocket_volume))
print("The rocket has a fuel volume of: " + str(fuel_volume))
print("The rocket has a fuel mass of: " + str(init_fuel_mass))
print("The rocket has: " + str(init_fuel_mass) + " kg of fuel")
print("The rocket has a drag coefficient of: " + str(drag_coeff))

timestep = 0.0001 #seconds
final_time = init_fuel_mass / fuel_ejection_rate #seconds
init_mass = other_mass + init_fuel_mass #initial mass of the rocket

print("The rocket will run out of fuel in: " + str(final_time) + " seconds")

times = [0]
vels = [vel]
alts = [alt]

def find_dv(v_in, time):
    new_dv = -g + ( (exhaust_speed*fuel_ejection_rate - math.pow(v_in,2)*drag_coeff)/(init_mass-fuel_ejection_rate*time) )
    return new_dv

def run_simulation():
    global time
    global vel
    global alt
    global times
    global vals
    global alts

    while(time < final_time and vel >= 0):
        time += timestep #incrementing time
        vel = vel + timestep * find_dv(vel, time) #finding new velocity
        alt = alt + timestep * vel #finding new altitude
        #print("time: " + str(time) + " vel: " + str(vel) + " alt: " + str(alt))
        #adding new values to list
        times.append(time)
        vels.append(vel)
        alts.append(alt)

def print_simulation():
    fopen = open("output.csv", "w")
    header = "time (s), velocity (ms^-1), altitude (m)"
    print(header)
    fopen.write(header + "\n")
    for i in range(0,len(times),1000):
        to_print = str(times[i]) + "," + str(vels[i]) + "," + str(alts[i])
        print(to_print)
        fopen.write(to_print + "\n")

def run_multiple() :
    global times
    global vels
    global alts
    global time
    global vel
    global alt
    global theta
    global rocket_volume
    global fuel_volume
    global init_fuel_mass
    global drag_coeff
    global final_time
    global init_mass

    fopen = open("outputmult.csv", "w")
    header = ("theta (rad), max altitude (m), time to max (s)")
    print(header)
    fopen.write(header + "\n")

    start_angle = math.pi / 2
    end_angle   = math.pi / 180 #1 degree
    step_angle  = math.pi / 180

    angle = start_angle-step_angle

    angle_list = []
    alt_list = []

    while angle >= end_angle:
        #setting up initial conditions
        time = 0
        vel  = 0
        alt  = 0
        times = [time]
        vels = [vels]
        alts = [alt]

        rocket_radius  = height*math.tan(theta)
        rocket_volume  = math.pi*math.pow(rocket_radius,2)*height/3
        fuel_volume    = rocket_volume - other_vol
        init_fuel_mass = fuel_density * fuel_volume
        drag_coeff     = air_density * math.pi * math.pow(rocket_radius, 2) * (1 - math.cos(2*theta))


        print("The rocket has a volume of: " + str(rocket_volume))
        print("The rocket has a fuel volume of: " + str(fuel_volume))
        print("The rocket has a fuel mass of: " + str(init_fuel_mass))
        print("The rocket has: " + str(init_fuel_mass) + " kg of fuel")
        print("The rocket has a drag coefficient of: " + str(drag_coeff))

        final_time = init_fuel_mass / fuel_ejection_rate #seconds
        init_mass = other_mass + init_fuel_mass #initial mass of the rocket

        print("The rocket will run out of fuel in: " + str(final_time) + " seconds")


        #running the simulation and adding to lists
        angle_list.append(angle)
        theta = angle
        run_simulation()
        if len(alts) >= 2:
            alt_list.append(alts[-2])
        else:
            alt_list.append(0)

        #printing results and adding to a file
        to_print = str(theta) + "," + str(alt) + "," + str(time)
        print(to_print)
        fopen.write(to_print + "\n")

        #incrementing
        angle -= step_angle

#run_simulation()
#print_simulation()

run_multiple()






