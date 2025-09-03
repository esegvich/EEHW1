import math
"""
Ethan Segvich
EE 2125A - Circuits I
Professor Pandey

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

print('Wifi and Bluetooth - I like working with networks and',
    'building home network systems.')
print('Electric Cars - This interests me because the advances',
    'in range and power all rely on circuit design.')
print('Audio Technology - I love music and knowing how the',
    'listening systems work is really cool.')


# Question 3
# 3 a)
SPEED_OF_LIGHT = 3 * (10 ** 8)
FREQUENCY1 = 50
FREQUENCY2 = 60

wavelength1 = SPEED_OF_LIGHT / FREQUENCY1
wavelength2 = SPEED_OF_LIGHT / FREQUENCY2

print('\nThe wavelength of the first frequency is', f"{wavelength1:.2e}", 'm')
print('The wavelength of the second frequency is', f"{wavelength2:.2e}", 'm')

# 3 b)

physical_dimension = wavelength1 * (1/10)

print('\nThe physical dimension of the first frequency is',
      f"{physical_dimension:.2e}", 'm, which is 372.82 miles.\n')

# Question 4
# 4 a)
bAnswers = []
cAnswers = []
ELECTRON_CHARGE = 1.6 * (10 ** -19)
magnitudes = [100, 1000, 10000, 100000, 1000000]

for w in magnitudes:
    v = w/ELECTRON_CHARGE
    print(f'The voltage of {w} J is {v:.2e} V.')
    bAnswers.append(v)

# 4 b)
print('\n')
charge = [1, math.log(100), math.exp(1), 1e-10, 1 / 64]
TIME = 10 ** -9

for q in charge:
    i = q/TIME
    print(f'The voltage of {q} C is {i:.2e} A.')
    cAnswers.append(i)

print('\n')
print(bAnswers)
print(cAnswers)
