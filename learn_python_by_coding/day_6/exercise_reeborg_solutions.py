# Reeborg's world challege - https://reeborg.ca/index_en.html

# First challenge

# def turn_right():
#     for count in range(0, 3):
#         turn_left()
#
# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()


# Second challenge - Hurdle 2

# def turn_right():
#     for count in range(0, 3):
#         turn_left()
#
#
# def jump_if_wall():
#     if wall_in_front():
#         turn_left()
#         move()
#         turn_right()
#         move()
#         turn_right()
#         move()
#         turn_left()
#
#
# while not at_goal():
#     move()
#     jump_if_wall()

# Third Challenge - Hurdle 3
# def turn_right():
#     for count in range(0, 3):
#         turn_left()
#
#
# def jump_if_wall():
#     if wall_in_front():
#         turn_left()
#         move()
#         turn_right()
#         move()
#         turn_right()
#         move()
#         turn_left()
#
#
# while not at_goal():
#     if front_is_clear():
#         move()
#     jump_if_wall()


# Fourth Challenge - Hurdle 4
# def turn_right():
#     for count in range(0, 3):
#         turn_left()
#
#
# def jump_if_wall():
#     if wall_in_front():
#         turn_left()
#         while wall_on_right() and is_facing_north():
#             move()
#         turn_right()
#         move()
#         turn_right()
#         while front_is_clear():
#             move()
#         turn_left()
#
#
# while not at_goal():
#     if front_is_clear():
#         move()
#     jump_if_wall()


# Maze
# def turn_right():
#     for count in range(0, 3):
#         turn_left()
#
#
# while front_is_clear():
#     move()
# turn_left()
#
# while not at_goal():
#     while is_facing_north() and front_is_clear():
#         move()
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
