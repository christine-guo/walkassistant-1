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
def bbx_nonmax_suppression(detections, overlap_threshold):
    
