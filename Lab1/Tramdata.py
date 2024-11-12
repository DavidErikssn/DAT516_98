import json

jsonobject = 'tramstops.json'
lines = 'tramlines.txt'

def build_tram_stops(jsonobject):
    with open(jsonobject) as file:
        data = json.load(file)
        
        for key, value in data.items():
            tramstops = {key: {'lat': value['position'][0], 'lon': value['position'][1]}}
            return tramstops
            
def build_tram_lines(lines):
    with open(lines) as file:

        print(linjer)
        stops = []
        for line in file:

            lin = (line.split())
            
            stop = ' '.join(lin[:-1])
            #print(stop)
            

        
        #for i in stops:
           # if i != '':

        #print(stops)
                
        #print(stops)

        #index = 1
        #for i in range(9):
        #    dic = {index: [line for line in file]}
        #    index += 1
        #    print(dic)
#
        #stops = []
        #for line in file:
        #    lin = (line.split())
        #    
        #    stop = (' '.join(lin[:-1]))
            
    #print(stops)

build_tram_lines(lines)
