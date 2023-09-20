from jinja2 import Environment, PackageLoader, select_autoescape


def render_mytemplate(your_name, my_name):
    env = Environment(
        loader=PackageLoader("example_package_hahattpro", "template"),
        autoescape=select_autoescape()
    )

    return env.get_template("mytemplate.txt").render(
        YOUR_NAME=your_name,
        MY_NAME=my_name
    )