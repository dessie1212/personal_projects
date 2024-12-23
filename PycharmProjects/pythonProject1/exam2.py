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

# Function to take user input
def inputData():
    # Input number of products (boxes)
    n = int(input("Enter the number of products: "))

    # Input boxes and unitsPerBox values
    boxes = []
    unitsPerBox = []

    print("Enter the boxes and units per box values:")
    for i in range(n):
        box_count = int(input(f"Enter the number of boxes for product {i+1}: "))
        boxes.append(box_count)
        unit_per_box = int(input(f"Enter the units per box for product {i+1}: "))
        unitsPerBox.append(unit_per_box)

    # Input truck size
    truckSize = int(input("Enter the truck size (number of boxes the truck can carry): "))

    # Call the function with user inputs and print the result
    result = getMaxUnits(boxes, unitsPerBox, truckSize)
    print(f"Maximum units the truck can carry: {result}")


# Call the function to get input from the user
inputData()
