import json

jsonobject = 'tramstops.json'
lines = 'tramlines.txt'

def build_tram_stops(jsonobject):
    with open(jsonobject) as file:
        data = json.load(file)
        tstops = {}
        for key, value in data.items():
            tstops[key] = {'lat': value['position'][0], 'lon': value['position'][1]}
            #tramstops = key, {'lat': value['position'][0], 'lon': value['position'][1]}
        return tstops
        
#print(build_tram_stops(jsonobject))
            
def build_tram_lines(lines):
    with open(lines) as file:

        tram_lines = {}
        current_line = None
        stops = []

        for line in file:
            line = line.strip()

            if line.endswith(':'):

                if current_line is not None:
                    tram_lines[current_line] = stops  
                current_line = line.strip(':')  
                stops = []  

            elif line:  
                stop_name = ' '.join(line.split()[:-1])  
                stops.append(stop_name)  

        if current_line is not None:
            tram_lines[current_line] = stops

        return tram_lines


#print(build_tram_lines(lines))
