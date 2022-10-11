#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nu_list = []
    for y in range(0, list_length):
        try:
            sum = my_list_1[y] / my_list_2[y]
        except TypeError:
            print("wrong type")
	    sum = 0
        except ZeroDivisionError:
            print("division by 0")
	    sum = 0
        except IndexError:
            print("out of range")
	    sum = 0
        finally:
            nu_list.append(sum)
    return nu_list
