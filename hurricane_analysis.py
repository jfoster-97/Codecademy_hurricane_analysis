# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages


    
    

def damages_float(damages):
  updated = []
  for cost in damages:
    if cost[-1] == "M":
      updated.append(float(cost[:-1]) * conversion[cost[-1]])
    elif cost[-1] == "B":
      updated.append(float(cost[:-1]) * conversion["B"])   
    else:
      updated.append(cost)
  return updated

new_damages = damages_float(damages)

# 2 
# Create a Table

# Create and view the hurricanes dictionary
def dict_convert(names, months, years, max_sustained_winds, areas_affected, new_damages, deaths):
  hurricane_info = {}
  for i in range(len(names)):
    hurricane_info[names[i]] = {"Name" : names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": new_damages[i], "Deaths": deaths[i]}
  return hurricane_info

hurricane_dict = dict_convert(names, months, years, max_sustained_winds, areas_affected, new_damages, deaths)
# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key
def year_dict(hurricane_dict):
  year_info = {}
  for name in hurricane_dict:
    year = hurricane_dict[name]["Year"]
    info = hurricane_dict[name]
    if year not in year_info.keys():
      year_info[year] = info
    else:
      temp_list = [year_info[year]]
      temp_list.append(info)
      year_info[year] = temp_list
  return year_info

# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
def affected_areas_dict(areas_affected):
  area_dict = {}
  for all_areas in areas_affected:
    for area in all_areas:
      if area not in area_dict.keys():
        area_dict[area] = 1
      else:
        area_dict[area] += 1

  return area_dict
      
area_dict = affected_areas_dict(areas_affected)
print(area_dict)
# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def most_affected_area(area_dict):
  highest_value = 0
  highest_value_name = ""
  for area in area_dict:
    if area_dict[area] > highest_value:
      highest_value = area_dict[area]
      highest_value_name = area
    elif area_dict[area] == highest_value:
      highest_value_name = highest_value_name + ", " + str(area)
  return highest_value_name, highest_value 

print(most_affected_area(area_dict))

# 6
# Calculating the Deadliest Hurricane

# function using 

#def most_deaths(names, deaths):
#  count = -1 
#  death_value = 0
#  name = ""
#  for death_count in deaths:
#    count += 1
#    if death_count > death_value:
#      death_value = death_count
#      name = names[count]
#    elif death_count == death_value:
#      name = name + ", " + names[count]
#  return name, death_value

def most_deaths(hurricane_dict):
  death_value = 0
  name = ""
  for cane in hurricane_dict:
    if hurricane_dict[cane]["Deaths"] > death_value:
      death_value = hurricane_dict[cane]["Deaths"]
      name = hurricane_dict[cane]["Name"]
#Check for names with same number of deaths so included
    elif hurricane_dict[cane]["Deaths"] == death_value:
      name = name + ", " + hurricane_dict[cane]["Name"]
  return name, death_value


print(most_deaths(hurricane_dict))
# find highest mortality hurricane and the number of deaths

# 7
# Rating Hurricanes by Mortality
def mortality_rating (hurricane_dict):
  mortality_rating_dict = {}
  list0 = []
  list1 = []
  list2 = []
  list3 = []
  list4 = []
  list5 = []
  for hurricane in hurricane_dict:
    death_count = hurricane_dict[hurricane]["Deaths"]
    if death_count == 0:
      list0.append(hurricane_dict[hurricane])
    elif death_count <= 100 and death_count > 0:
      list1.append(hurricane_dict[hurricane])
    elif death_count <= 500 and death_count > 100:
      list2.append(hurricane_dict[hurricane])
    elif death_count <= 1000 and death_count > 500:
      list3.append(hurricane_dict[hurricane])
    elif death_count <= 10000 and death_count > 1000:
      list4.append(hurricane_dict[hurricane])
    else:
      list5.append(hurricane_dict[hurricane])
    mortality_rating_dict[0] = list0
    mortality_rating_dict[1] = list1
    mortality_rating_dict[2] = list2 
    mortality_rating_dict[3] = list3 
    mortality_rating_dict[4] = list4
    mortality_rating_dict[5] = list5
  return mortality_rating_dict

mortality_dict = mortality_rating(hurricane_dict)

# categorize hurricanes in new dictionary with mortality severity as key


# 8 Calculating Hurricane Maximum Damage
def most_damage(hurricane_dict):
  damage_value = 0
  name = ""
  for cane in hurricane_dict:
    try:
      if hurricane_dict[cane]["Damage"] > damage_value:
        damage_value = hurricane_dict[cane]["Damage"]
        name = hurricane_dict[cane]["Name"]
#Check for names with same number of deaths so included
      elif hurricane_dict[cane]["Damage"] == damage_value:
        name = name + ", " + hurricane_dict[cane]["Name"]
    except TypeError:
      continue
  return f"The hurricane {name}, inflicted the most damage, costing ${damage_value}"
# find highest damage inducing hurricane and its total cost
print(most_damage(hurricane_dict))

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def damage_cat (hurricane_dict, damage_scale):
  damage_rating_dict = {}
  list0 = []
  list1 = []
  list2 = []
  list3 = []
  list4 = []
  list5 = []
  for hurricane in hurricane_dict:
    try:
      damage_count = hurricane_dict[hurricane]["Damage"]
      if damage_count == damage_scale[0]:
        list0.append(hurricane_dict[hurricane])
      elif damage_count <= damage_scale[1] and damage_count > damage_scale[0]:
        list1.append(hurricane_dict[hurricane])
      elif damage_count <= damage_scale[2] and damage_count > damage_scale[1]:
        list2.append(hurricane_dict[hurricane])
      elif damage_count <= damage_scale[3] and damage_count > damage_scale[2]:
        list3.append(hurricane_dict[hurricane])
      elif damage_count <= damage_scale[4] and damage_count > damage_scale[3]:
        list4.append(hurricane_dict[hurricane])
      else:
        list5.append(hurricane_dict[hurricane])
    except TypeError:
      continue

    damage_rating_dict[0] = list0
    damage_rating_dict[1] = list1
    damage_rating_dict[2] = list2 
    damage_rating_dict[3] = list3 
    damage_rating_dict[4] = list4
    damage_rating_dict[5] = list5
  return damage_rating_dict
damage_rating_dict = damage_cat (hurricane_dict, damage_scale)
print(damage_rating_dict)

