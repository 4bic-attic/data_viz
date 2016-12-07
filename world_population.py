import json
import pygal
from pygal.maps.world import World
from pygal.style import RotateStyle
from country_codes import get_country_code

#load data onto a list
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

#build a dictionary of population data
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

#group countries into three population levels
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
#see how many countries are in each level
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
wm.title = 'World population in 2010, by Country'
wm.add('0-10M', cc_pops_1)
wm.add('10M-1Bn', cc_pops_2)
wm.add('>1Bn', cc_pops_3)



wm.render_to_file('world_population.svg')
