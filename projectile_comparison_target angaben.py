"""
https://courses.lumenlearning.com/boundless-physics/chapter/projectile-motion/
projectile_comparison_gen.py

Compare the projectile motion of a body thrown with various combinations of initial 
velocity and angle of projection.
"""


"""
Aendert das Programm ab um experimentell (dh durch programm-technisches austesten verschiedenster
Winkel und Abschuss-Geschwindigkeits-Kombinationen, folgende Flugbahnen zu finden

1. Abschussgeschwindigkeit und Winkel in Grad um eine Distanz von 100 meter zu erreichen
2. Abschussgeschwindigkeit um eine maximale Hoehe von 100 meter zu erreichen

- gebt fuer den jeweiligen Fall die ermittelten Werte in m/s und GRAD an
- testet grafisch ob das Ergebnis korrekt ist in dem Ihr zwei Flugbahnen eingebt und grafisch darstellen
lasst,die eine muss 100 meter Hoehe erreichen, die zweite 100 meter zueruecklegen

ACHTUNG - wir haben die GRAD in RADIANS umgerechnet fuer die Eingabe in die SIN und COS Funktion
, ihr muesst dementsprechend die Werte die Ihr auslest in Radians wieder in Grad zurueckrechnen
mit Grad = Radians * 360 / 6.28

ACHTUNG - VERWENDET GRAD ZWISCHEN 1 und 46 GRAD
ACHTUNG - VERWENDET M/S ZWISCHEN 1 und 100 M/S
"""



#importing the right modules
import matplotlib.pyplot as plt
import math

# defining the constant g for gravitational force
g = 9.8

targety=100
targetx=100



# help function to plot
def draw_graph(x, y):
    plt.plot(x, y)
    
#help function to return ???    
def frange(start, final, interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval    
    return numbers

# function to draw the tractory
def draw_trajectory(u, theta, t_flight):
    # list of x and y co-ordinates
    x = []
    y = []
    intervals = frange(0, t_flight, 0.001)

    # create the list of travel points
    for t in intervals:
        # x position per cosinus formula
        x.append(u*math.cos(theta)*t)
        # y position per sin formula with gravitational force
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)

    #create the graph
    draw_graph(x, y)




if __name__ == '__main__':

    
    #main program as it was#

    num_trajectories = int(input('How many trajectories? '))
    
    velocities = []
    angles = []
    for i in range(1, num_trajectories+1):
        v = input('Enter the initial velocity for trajectory {0} (m/s): '.format(i))
        theta = input('Enter the angle of projection for trajectory {0} (degrees): '.format(i))
        velocities.append(float(v))
        angles.append(math.radians(float(theta)))

    for i in range(num_trajectories):
        # calculate time of flight, maximum horizontal distance and
        # maximum vertical distance

        # formula for flight time
        t_flight = 2*velocities[i]*math.sin(angles[i])/g

        # max x distance
        S_x = velocities[i]*math.cos(angles[i])*t_flight

        #max y distance
        S_y = velocities[i]*math.sin(angles[i])*(t_flight/2) - (1/2)*g*(t_flight/2)**2

        print('Initial velocity: {0} Angle of Projection: {1}'.format(velocities[i], math.degrees(angles[i])))
        print('T: {0} S_x: {1} S_y: {2}'.format(t_flight,S_x, S_y))
        print()
        draw_trajectory(velocities[i], angles[i], t_flight)
        
    # Add a legend and show the graph
    legends = []
    for i in range(0, num_trajectories):
        legends.append('{0} - {1}'.format(velocities[i], math.degrees(angles[i])))

    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion at different initial velocities and angles')
    plt.legend(legends)
    plt.show()

    

    # new main program to find target  variables for velocity and angle
    
    









    
