"""
Ethan Segvich
September 5, 2025
Python Homework Assignment 1

Circuit theory is a special case of electromagnetic field theory that helps
to analyze systems in a more tractable manner. There are three assumptions
that permit us to use circuit theory:
1. Electrical effects happen instantaneously throughout a system.
2.The net charge on every component in the system is always zero.
3. There is no magnetic coupling between the components in a system.

Applications that interest me:
- Application 1: Wifi and Bluetooth - I like working with networks and
                 building home network systems.
- Application 2: Electric Cars - This interests me because the advances
                 in range and power all rely on circuit design.
- Application 3: Audio Technology - I love music and knowing how the
                 listening systems work is really cool.
"""

import math

print('Wifi and Bluetooth - I like working with networks and',
    'building home network systems.')
print('Electric Cars - This interests me because the advances',
    'in range and power all rely on circuit design.')
print('Audio Technology - I love music and knowing how the',
    'listening systems work is really cool.')


# Question 3
# 3 a)
SPEED_OF_LIGHT = 3 * (10 ** 8) # speed of light in meters per second (c)
FREQUENCY1 = 50 # frequency in Hz (f1)
FREQUENCY2 = 60 # frequency in Hz (f2)

# Wavelength lamda = c / f in meters
wavelength1 = SPEED_OF_LIGHT / FREQUENCY1
wavelength2 = SPEED_OF_LIGHT / FREQUENCY2

print('\nThe wavelength of the first frequency is', f"{wavelength1:.2e}", 'm')
print('The wavelength of the second frequency is', f"{wavelength2:.2e}", 'm')

# 3 b)
# Physical dimension is one tenth of the wavelength
physical_dimension = wavelength1 * (1/10)

print('\nThe physical dimension of the first frequency is',
      f"{physical_dimension:.2e}", 'm, which is 372.82 miles.\n')

# Question 4
# 4 b)
# This computes the voltage v from work w and charge q using v = w / q
# We will be using the electron charge to find the voltage.
bAnswers = [] # list to store computed voltages (V)
cAnswers = [] # List to store computed currents (A)
ELECTRON_CHARGE = -1.6 * (10 ** -19) # electron charge in coulombs
magnitudes = [100, 1000, 10000, 100000, 1000000] # list of work values w in Joules J

for w in magnitudes:
    v = w/ELECTRON_CHARGE # v = w / q in volts
    print(f'The voltage of {w} J is {v:.2e} V.')
    bAnswers.append(v) # Add to list

# 4 c)
print('\n')
# Given charges q (Coulombs)
charge = [1, math.log(100), math.exp(1), 1e-10, 1 / 64]
TIME = 10 ** -9 # TIME is 1 nanosecond (ns) = 1e-9 seconds

# 4 d)
# Compute current i from charge q using i = q / TIME
for q in charge:
    i = q/TIME
    print(f'The current of {q} C is {i:.2e} A.')
    cAnswers.append(i) # add to list

# Print results again in indexed from
print(f'\nIndexed list for 4b voltages:')
for i, v in enumerate(bAnswers):
    print(f'{v:.2e} V')
print(f'\nIndexed list for 4c currents:')
for i, v in enumerate(cAnswers):
    print(f'{v:.2e} A')