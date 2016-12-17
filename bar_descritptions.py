import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['tensorflow', 'httpie', 'awesome-python']

plot_dicts = [
    {'value' : 40348, 'label' :'Description of tensorflow'},
    {'value' : 22287, 'label' :'Description of httpie'},
    {'value' : 27148, 'label' :'Description of awesome-python'}
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
