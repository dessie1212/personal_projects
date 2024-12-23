
def getMaxUnits(boxes, unitsPerBox, truckSize):
    # Check if truck size is positive
    if truckSize < 1:
        raise ValueError("Truck size must be a positive number.")

    if len(boxes) < 1:
        raise ValueError("The number of boxes must be greater than or equal to 1.")

    # Check if boxes and unitsPerBox arrays have the same length
    if len(boxes) != len(unitsPerBox):
        raise ValueError("The length of boxes and unitsPerBox must be the same.")


    # Check if any entry in boxes or unitsPerBox is negative
    if any(box < 1 for box in boxes) or any(unit < 1 for unit in unitsPerBox):
        raise ValueError("Boxes and unitsPerBox must not contain negative values.")

    # Pair each product's box count and units per box
    box_unit_pairs = [(boxes[i], unitsPerBox[i]) for i in range(len(boxes))]

    # Sort pairs in descending order of units per box
    box_unit_pairs.sort(key=lambda x: x[1], reverse=True)

    total_units = 0
    # Load boxes into the truck from highest to lowest units per box
    for box_count, unit_per_box in box_unit_pairs:
        # Take as many boxes as possible, limited by the truck's capacity
        boxes_to_take = min(truckSize, box_count)

        # Add the units from the boxes taken
        total_units += boxes_to_take * unit_per_box

        # Decrease truck size by the number of boxes taken
        truckSize -= boxes_to_take

        # Stop if the truck is full
        if truckSize == 0:
            break

    return total_units


b = []
u = []
t = 6
X = getMaxUnits(b,u,t)
print(X)

# Rules
# 1 <= boxes <= 10^5
# 1 <= unitsPerBox <= 10^5
# boxes == unitsPerBox
# 1 <= truckSize <= 10^8
# LONG_INTEGER_ARRAY boxes
# LONG_INTEGER_ARRAY unitsPerBox
#  LONG_INTEGER truckSize
# Must return LONG_INTEGER



