from jinja2 import Environment, PackageLoader, select_autoescape


env = Environment(
    loader=PackageLoader('pinout','templates'),
    autoescape=select_autoescape(['html', 'xml']),
)

# Base SVG elements
svg = env.get_template('svg.svg')
svg_group = env.get_template('group.svg')
svg_image = env.get_template('image.svg')

# Component SVG templates (made from multiple svg elements)
svg_pin_label = env.get_template('pin_label.svg')
