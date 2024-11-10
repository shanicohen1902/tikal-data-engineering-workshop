import jinja2

# loading the environment
environment = jinja2.Environment()

# loading the template
template = environment.from_string("Hello, {{ name }}!")

# rendering the template and storing the resultant text in variable output
rendered = template.render(name="World")

# printing the output on screen
print(rendered)
