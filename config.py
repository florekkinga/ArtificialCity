cell_size = 9  # in px
screen_size = width, height = 100 * cell_size, 100 * cell_size
lane_width = 4 * cell_size  # in meters

tps = 100
car_speed_limit = 50
car_spawn_prob = 0.1
car_slow_prob = 0.45
car_v_change = 1
car_slow_duration = 2

"""dictionary: 
{lane_from_number: [lane_into, at_length, untill_length, appear_at_travelled]}
untill length is necesarry because it is not very probable that a car will
get self.travelled value that is exactly equal to the `at_length`
appear_at_travelled is distance on which the car should appear on `lane_into`
"""
turns = {1: None,
         2: [7, 25, 35, 58],
         3: [6, 21, 30, 62],
         4: [11, 21, 30, 58],
         5: None,
         6: [1, 38, 50, 0],
         7: None,
         8: None,
         9: None,
         10: None,
         11: [5, 38, 45, 0]}

v_first_lane_x = (width - lane_width * 6 - 26 * cell_size) / 2
h_first_lane_x = (height - lane_width * 4) / 2

car_lanes = [
    # horizontal lanes -> y
    (1, h_first_lane_x + 0.25 * lane_width),
    (2, h_first_lane_x + 3.25 * lane_width),
    (3, h_first_lane_x + 4.25 * lane_width),
    (4, h_first_lane_x + 0.25 * lane_width),
    (5, h_first_lane_x + 3.25 * lane_width),

    # vertical lanes -> x
    (6, v_first_lane_x + 0.25 * lane_width),
    (7, v_first_lane_x + 1.25 * lane_width),
    (8, v_first_lane_x + 2.25 * lane_width),
    (9, v_first_lane_x + 26 * cell_size + 3.25 * lane_width),
    (10, v_first_lane_x + 26 * cell_size + 4.25 * lane_width),
    (11, v_first_lane_x + 26 * cell_size + 5.25 * lane_width),
]

tram_lanes = [
    (1, h_first_lane_x + 1.25 * lane_width),
    (2, h_first_lane_x + 2.25 * lane_width)
]

zebra_lanes = [
    # x, y

    # vertical
    (1, (v_first_lane_x - lane_width, h_first_lane_x)),
    (2, (v_first_lane_x - 0.75 * lane_width, h_first_lane_x + lane_width * 5)),
    (3, (v_first_lane_x + 26 * cell_size + 6.5 * lane_width, h_first_lane_x)),
    (4, (v_first_lane_x + 26 * cell_size + 6.75 * lane_width, h_first_lane_x + lane_width * 4)),

    # horizontal
    (5, (v_first_lane_x + 3 * lane_width, h_first_lane_x - lane_width)),
    (6, (v_first_lane_x, h_first_lane_x - 0.75 * lane_width)),

    (7, (v_first_lane_x + 6 * lane_width + 26 * cell_size, h_first_lane_x - lane_width)),
    (8, (v_first_lane_x + 3 * lane_width + 26 * cell_size, h_first_lane_x - 0.75 * lane_width)),

    (9, (v_first_lane_x + 3 * lane_width, h_first_lane_x + 5.5 * lane_width)),
    (10, (v_first_lane_x, h_first_lane_x + 5.75 * lane_width)),

    (11, (v_first_lane_x + 6 * lane_width + 26 * cell_size, h_first_lane_x + 4.5 * lane_width)),
    (12, (v_first_lane_x + 3 * lane_width + 26 * cell_size, h_first_lane_x + 4.75 * lane_width)),

]

c_lanes_coordinates = dict(car_lanes)
z_lanes_coordinates = dict(zebra_lanes)
t_lanes_coordinates = dict(tram_lanes)
