"""
Write the unit test for the bbx_nonmax_suppression function.
Try to think about different test cases
"""
# here is the link to access a visual of the bbx before nms: https://www.pixilart.com/art/bbx-visual-002841ea9abfe40

from detection_utils import Detection, bbx_nonmax_suppression

# methods to print test case results
def print_before(detections):
    print("Before NMS:")
    for detection in detections:
        print(detection)

def print_after(final_detections):
    print("After NMS:")
    for final_detection in final_detections:
        print(final_detection)

# test case 1
detections1 = []
detections1.append(Detection(4, 5, 10, 15, 0.9)) #black (color of bbx in visual)
detections1.append(Detection(8, 10, 10, 16, 0.4)) #blue
detections1.append(Detection(6, 7, 10, 9, 0.3)) #red
detections1.append(Detection(10, 2, 11, 10, 0.8)) #pink

print("Test Case 1:")
print_before(detections1)
final_detections = bbx_nonmax_suppression(detections1, 0.5)
print_after(final_detections)

# test case 2
detections2 = []
detections2.append(Detection(4, 33, 13, 13, 0.8)) #dark green
detections2.append(Detection(21, 33, 13, 13, 0.9)) #light green
detections2.append(Detection(38, 33, 13, 13, 0.7)) #yellow

print("Test Case 2:")
print_before(detections2)
final_detections = bbx_nonmax_suppression(detections2, 0.5)
print_after(final_detections)
