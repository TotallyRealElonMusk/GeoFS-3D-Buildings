import json

def export():
    default = [{
		"location": [],
		"url": "",
		"options": {
			"shadows": 1
		},
		"htr": [],
		"rotateModelOnly": True,
		"scale": 1,
		"type": 100
	}	
]
    with open('D:\G3D\JSON\CustomBuildings.json', 'r') as f:
        data = json.load(f)
        
    with open('buildings.json', 'r') as f:
        buildings = json.load(f)
        
    for i in range(len(data)):
        
        name = data[i]["name"]
        name=retype(name)
        print(name)
        if name in buildings['buildings']:
            print('already exists')
        else:
            with open(name, 'w') as f:
                json.dump(default, f)
            with open(name, 'r') as f: 
                data2 = json.load(f)
                
            data2[0]["location"]=data[i]["position"]
            data2[0]["url"]=data[i]["url"]
            data2[0]["htr"]=data[i]["rotation"]
            data2[0]["scale"]=data[i]["scale"][0]
            
            with open(name, 'w') as f:
                json.dump(data2, f, indent=2)
                
            completeurl="https://raw.githubusercontent.com/TotallyRealElonMusk/GeoFS-3D-Buildings/3.0/JSON-Files/"+name
            data[i]["url"] = completeurl
                    
            with open('D:\G3D\JSON\CustomBuildings.json', 'w') as f:
                json.dump(data, f, indent=2)

            buildings['buildings'].append(name)
            with open('buildings.json', 'w') as f:
                json.dump(buildings, f, indent=2)
        
    print("done")
    

def retype(x):
    x=x.replace(" ", "_")
    x+=".json"
    return x


def delete():
    with open('D:\G3D\JSON\CustomBuildings.json', 'r') as f:
        data = json.load(f)
    for element in data:
        element.pop('rotation', None)
        element.pop('scale', None)
    with open('D:\G3D\JSON\CustomBuildings.json', 'w') as f:
        json.dump(data, f, indent=2)
