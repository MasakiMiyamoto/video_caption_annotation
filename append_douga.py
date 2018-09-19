# -*- coding: utf-8 -*-
import json
import cv2
#with open('append_annotation.json', 'r') as f:
#data = json.load(f)
data = {}
data["v_OTqq4kn4deM"] = []
append1 = {'sentence':'a','timestamp':[3.43,6.76]}
append2 = {'sentence':'b','timestamp':[22.50,25.83]}
append3 = {'sentence':'c','timestamp':[33.93,37.26]}
append4 = {'sentence':'d','timestamp':[48.67,52.00]}
data["v_OTqq4kn4deM"].append(append1)
data["v_OTqq4kn4deM"].append(append2)
data["v_OTqq4kn4deM"].append(append3)
data["v_OTqq4kn4deM"].append(append4)
data["v_sssssssssss"] = []
append5 = {'sentence':'s','timestamp':[3.43,6.76]}
data["v_sssssssssss"].append(append5)
f2 = open('video_annotation.json', 'w')
json.dump(data, f2, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
