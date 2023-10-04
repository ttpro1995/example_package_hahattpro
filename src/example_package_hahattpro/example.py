def add_one(number):
    return number + 1

def get_the_cat():
    import pkgutil
    data = pkgutil.get_data('example_package_hahattpro.code_sample', 'do_something.py')
    data_str = data.decode()
    return data_str

