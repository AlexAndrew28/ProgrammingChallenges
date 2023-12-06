"""
Intersection over Union calculator 

Given two bounding boxes calculate the IoU between them

"""


def calculate_area(box: [float, float, float, float]) -> float:
    """ Calculate the area of a box given its coordinates

    Args:
        box (float, float, float, float]): The coordinates of the box in the form: [x1, y1, x2, y2]

    Returns:
        float: The area of the box
    """
    return (box[2]-box[0]) * (box[3]-box[1])


def calculate_iou(box_a: [float, float, float, float], box_b: [float, float, float, float]) -> float:
    """ Calculate the IoU (intersection over union) of two bounding boxes. IoU is a measure of how much two boxes overlap

    Args:
        box_a (float, float, float, float]): The first boxes coordinates in the form: [x1, y1, x2, y2]
        box_b (float, float, float, float]): The second boxes coordinates in the form: [x1, y1, x2, y2]

    Returns:
        float: The intersection over union of the boxes
    """
    
    # get the coordinates of box formed by the overlap between the two boxes
    intersection_x1 = max(box_a[0], box_b[0])
    intersection_x2 = min(box_a[2], box_b[2])
    
    intersection_y1 = max(box_a[1], box_b[1])
    intersection_y2 = min(box_a[3], box_b[3])

    # check if there is any overlap 
    if intersection_x2 >= intersection_x1 and intersection_y2 >= intersection_y1:
        intersection_area = calculate_area([intersection_x1, intersection_y1, intersection_x2, intersection_y2])
        union_area = calculate_area(box_a) + calculate_area(box_b) - intersection_area
        
        return intersection_area/union_area
    else:
        return 0



box_a = [50, 100, 200, 300]
box_b = [80, 120, 220, 310]

print(calculate_iou(box_a, box_b))
