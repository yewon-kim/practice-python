import pandas as pd

distance_from_sun = [149.6, 1433.5, 227.9, 108.2, 778.6]
planets = ['Earth', 'Saturn', 'Mars', 'Venus', 'Jupiter']

dist_planets = pd.Series(distance_from_sun, index = planets)
print(dist_planets)

c = 18 # speed of light
time_light = dist_planets / c
print(time_light)

close_planets = time_light[time_light < 40].sort_values().index.array
print(close_planets)