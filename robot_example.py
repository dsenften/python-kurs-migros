from exercise.Robot import Robot

if __name__ == "__main__":
    x = Robot(3, 4, "north", "Marvin")
    print(x)

    x.move(10)
    x.new_orientation("west")
    x.move(7)
    print(x)

    new_name = "Andrew"
    print(f'{x.get_name()} will be renamed as {new_name}')

    x.rename(new_name)
    print(f'Hi, this is {x.get_name()}')

    x.set_position([0, 0])
    print(x)
