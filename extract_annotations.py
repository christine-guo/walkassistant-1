import json
import urllib
import cv2

class Annotation(object):
    def __init__(self, name, x, y, height, width):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def get_name(self):
        return self.name
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height

class Door(Annotation):
    def __init__(self, name, x, y, height, width, type):
        super(Door, self).__init__(name, x, y, height, width)
        self.type = type
    def get_type(self):
        return self.type

def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__

# read json file into a dictionary
json_file = 'annotations.json'
readfile = open(json_file)
json_data = json.load(readfile)

outfile = open('extracted_data.txt', 'w')

results = []
for image in json_data:
    # skip images with no annotations
    if len(image.get("Label")) == 0:
        continue
    else:
        image_data = {}
        image_data["ID"] = image.get("ID")
        image_data["Original Image"] = image.get("Labeled Data")
        objects = image["Label"]["objects"]
        annotations = []
        # loop through every annotation per image
        for item in objects:
            name = item["title"]
            x = int(item["bbox"]["left"])
            y = int(item["bbox"]["top"])
            height = int(item["bbox"]["height"])
            width = int(item["bbox"]["width"])
            # if the bbx is a door, get the type
            if name == "Door":
                type = item["classifications"][0]["answer"]["title"]
                annotations.append(Door(name, x, y, height, width, type))
            else:
                annotations.append(Annotation(name, x, y, height, width))
        image_data["Annotations"] = annotations
        outfile.write(json.dumps(image_data, default=dumper, indent=2))
        results.append(image_data)


all_image_names = []
# download each image from link and save file name to list
for image in results:
    link = image.get("Original Image")
    link_split = link.split(".jpg")
    image_name = link_split[0].split('/')[-1] + ".jpg"
    urllib.urlretrieve(link, image_name)
    all_image_names.append(image_name)


# draw bbx onto image
for index, image_data in enumerate(results):
    image_file = all_image_names[index]
    image = cv2.imread(image_file)
    for annotation in image.get("Annotation"):
        x = annotation.get_x()
        y = annotation.get_y()
        start_point = (x, y)
        height = annotation.get_height()
        width = annotation.get_width()
        end_point = (x + width, y + height)
        image = cv2.rectangle(image, start_point, end_point, (0, 0, 0), 2)
        cv2.imwrite(image_file, image)


# get statistics
num_annotations = 0
num_door = 0
num_knob = 0
num_stairs = 0
num_ramp = 0
num_double = 0
num_single = 0
num_revolving = 0
num_automatic = 0
for image in results:
    annotations = image.get("Annotations")
    for annotation in annotations:
        num_annotations += 1
        if annotation.get_name() == "Door":
            num_door += 1
            if annotation.get_type() == "Single":
                num_single += 1
            elif annotation.get_type() == "Double":
                num_double += 1
            elif annotation.get_type() == "Revolving":
                num_revolving += 1
            else:
                num_automatic += 1
        elif annotation.get_name() == "Knob":
            num_knob += 1
        elif annotation.get_name() == "Stairs":
            num_stairs += 1
        else:
            num_ramp += 1

print("Number of Annotations = " + str(num_annotations))
print("Number of Doors = " + str(num_door))
print("\t Single = " + str(num_single))
print("\t Double = " + str(num_double))
print("\t Automatic = " + str(num_automatic))
print("\t Revolving = " + str(num_revolving))
print("Number of Knobs = " + str(num_knob))
print("Number of Stairs = " + str(num_stairs))
print("Number of Ramps = " + str(num_ramp))
