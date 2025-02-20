
def my_print(var):
    print(var, "has a type", type(var))

def my_var():
    var_int = 42
    var_str = "42"
    var_str_2 = "quarante-deux"
    var_float = 42.0
    var_bool = True
    var_list = [42]
    var_dict = {42: 42}
    var_tuple = (42,)
    var_set = set()

    my_print(var_int)
    my_print(var_str)
    my_print(var_str_2)
    my_print(var_float)
    my_print(var_bool)
    my_print(var_list)
    my_print(var_dict)
    my_print(var_tuple)
    my_print(var_set)


if __name__ == '__main__':
    my_var()