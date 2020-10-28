def number(bus_stops)
    # Happy Coding
    bus_stops.map { |get_in, get_off| get_in }.sum - bus_stops.map { |get_in, get_off| get_off }.sum
end

number([[10, 0], [3, 5], [5, 8]])
