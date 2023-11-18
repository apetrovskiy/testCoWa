def evaporator(content, evap_per_day, threshold):
    nth_day = 0
    absolute_threshold = content * threshold / 100
    while content > absolute_threshold:
        nth_day += 1
        content *= (100 - evap_per_day) / 100
    return nth_day
