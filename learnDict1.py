data = {'hour': None, 'temperature': None, 'humidity':
        None, 'wind_speed':
        None, 'wind_direction':
        None, 'direct_flux': None, 'diffuse_flux': None}

# For each key, initialize a list as its value.
for key in data:
  data[key] = list()

for line in infile.readlines():
  lines = line.split()

  # we simply append into the list this key references.
  data['hour'].append(lines[0])
  data['temperature'].append(lines[1])
  data['humidity'].append(lines[2])
  data['wind_speed'].append(lines[3])
  data['wind_direction'].append(lines[4])
  data['direct_flux'].append(lines[5])
  data['diffuse_flux'].append(lines[6])
return data
