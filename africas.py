import pygal

from pygal.maps.world import World


wm = World()
wm.title = 'North, Central and South Africa'

wm.add('West Africa', ['sn', 'ml','ty', 'td', 'sl', 'mr', 'ng', 'gw', 'gh', 'ne'])
wm.add('North Africa', ['tn', 'td', 'ml', 'ma', 'ly', 'eg', 'dz'])
wm.add('Central Africa', ['bi', 'cd', 'cf', 'cg', 'cm', 'ga's])
wm.add('East Africa', ['ug', 'tz', 'so', 'sd', 'rw', 'ke', 'et'])
wm.add('South Africa', ['za', 'zm', 'zw', 'sz', 'na', 'mz', 'mw', 'ls',
    'ao', 'bw'])

wm.render_to_file('africas.svg')
