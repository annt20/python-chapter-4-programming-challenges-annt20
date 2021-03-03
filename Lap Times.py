number_laps = int(input('How many times have you run around the racetrack?'))
total_lap_time = 0
average_lap_time = 0
fastest_lap = 0
compare_lap = 0
slowest_lap = 0
for i in range(1, number_laps+1):
    lap_time = int(input('Enter the lap time (in seconds) for lap number %d: ' % i))
    total_lap_time += lap_time
    average_lap_time = total_lap_time / number_laps
    if compare_lap == 0:
        fastest_lap = lap_time
        compare_lap = 1
    else:
        if lap_time < fastest_lap:
            fastest_lap = lap_time
        if lap_time > slowest_lap:
            slowest_lap = lap_time
print('Time of the fastest lap: ', fastest_lap)
print('Time of the slowest lap: ', slowest_lap)
print('Average time lap: ', average_lap_time)
