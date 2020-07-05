"""
Write the following function to apply non-maximum suppression on a number of detection bounding boxes.
Each detection bounding box is one rectange on one image (e.g. around one object) with one detection score
(e.g. 0.9 means very confident being one object, while 0.2 means not that confident). You can define one
class for it or just use one list like [x, y, width, height, score] for one rectangle.
Non-maximum suppression of these bbx is similar as the non-maximum suppression in edge detection: if two
bbx overlapping and the overlap rate (e.g. overlap_area / union area) is larger than overlap_threshold,
the bbx with heigher detection score will suppress the bbx with lower detection score (e.g. the bbx with
lower detection score will be deleted).
At the end, return the remaining detection bbx
"""

class Detection:
    # constructor
    def __init__(self, x, y, width, height, score):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.score = score
    # accessors
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def get_score(self):
        return self.score
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ") | Width: " + str(self.width) + " | Height: " + str(self.height) + " | Score: " + str(self.score)


def bbx_nonmax_suppression(detections, overlap_threshold):
    # sort the list of detections by its score from highest to lowest
    detections = sorted(detections, key=lambda detection: detection.score, reverse = True)
    # create a new list to save the remaining detection bbx after nms
    final_detections = []
    final_detections.append(detections[0])
    del detections[0]
    for index, detection in enumerate(detections):
        for final_detection in final_detections:
            # find overlap_rate and compare to overlap_threshold
            if overlap_rate(detection, final_detection) > overlap_threshold:
                del detections[index]
                break
        else:
            final_detections.append(detection)
            del detections[index]
    return final_detections




# function to calculate the overlap rate (overlap_area / union_area) between two detection boxes
def overlap_rate(b1, b2):
    # get coordinates
    # tl = top left; br = bottom right
    x1_tl = b1.get_x()
    x2_tl = b2.get_x()
    x1_br = b1.get_x() + b1.get_width()
    x2_br = b2.get_x() + b2.get_width()
    y1_tl = b1.get_y()
    y2_tl = b2.get_y()
    y1_br = b1.get_y() + b1.get_height()
    y2_br = b2.get_y() + b2.get_height()
    # calculate overlap_area
    x_overlap = max(0, min(x1_br, x2_br)-max(x1_tl, x2_tl))
    y_overlap = max(0, min(y1_br, y2_br)-max(y1_tl, y2_tl))
    overlap_area = x_overlap * y_overlap
    # calculate union_area
    area_1 = b1.get_width() * b1.get_height()
    area_2 = b2.get_width() * b2.get_height()
    union_area = area_1 + area_2 - overlap_area
    # calculate overlap_rate
    return overlap_area / float(union_area)
