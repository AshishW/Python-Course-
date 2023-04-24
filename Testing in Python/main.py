def add_5_to_input(num):
    try:
        return int(num) + 5
    except ValueError as err:
        return err