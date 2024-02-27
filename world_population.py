import json

from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
from country_codes import get_country_code
from pygal_maps_world.maps import World

# Load data into a list.
filename = 'population_data.json'

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = "World Population in 2010"
cc_pops1, cc_pops2, cc_pops3 = dict(), dict(), dict()

# Loading the json file
with open(filename) as f:
    pop_data = json.load(f)

#print the 2010 population for each country 
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            if population <= 10000000:
                cc_pops1[code] = population
            elif 10000000 < population <= 1000000000:
                cc_pops2[code] = population
            elif population > 1000000000:
                cc_pops3[code] = population
        else:
            print("ERROR - " + country_name)

wm.add('0-10m', cc_pops1)
wm.add('10m-1bn', cc_pops2)
wm.add('>1bn', cc_pops3)

wm.render_to_file('world_population.svg')