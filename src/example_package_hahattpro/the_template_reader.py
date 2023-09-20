import pkgutil

def read_template():
    data = pkgutil.get_data('example_package_hahattpro', 'template/mytemplate.txt')
    data_str = data.decode()
    return data_str
