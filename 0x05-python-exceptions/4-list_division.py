#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    nu_list = []
    for y in range(0, list_length):
        try:
            sum = my_list_1[y] / my_list_2[y]
        except TypeError:
            sum = 0
            print("wrong type")
        except ZeroDivisionError as err:
            sum = 0
            print(err)
        except IndexError:
            sum = 0
            print("out of range")
        finally:
            nu_list.append(sum)
        return nu_list
