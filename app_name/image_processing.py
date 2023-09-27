def process_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to RGB (if it's in BGR format)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Define the regions of interest (ROIs) where the colors are located
    # You'll need to adjust these coordinates based on your specific case
    roi_coordinates = [(start_x, start_y, end_x, end_y) for (start_x, start_y, end_x, end_y) in [
        (100, 200, 200, 300),  # Example ROI 1
        (300, 200, 400, 300),  # Example ROI 2
        # Add more ROIs as needed
    ]]

    colors = {}

    for index, (start_x, start_y, end_x, end_y) in enumerate(roi_coordinates):
        # Crop the ROI
        roi = image_rgb[start_y:end_y, start_x:end_x]

        # Calculate the mean color in the ROI
        mean_color = np.mean(roi, axis=(0, 1))

        # Store the color in the result dictionary
        colors[f'Color_{index+1}'] = mean_color.astype(int).tolist()

    return colors
