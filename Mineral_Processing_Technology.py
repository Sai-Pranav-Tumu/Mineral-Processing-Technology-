import streamlit as st
import cv2
import numpy as np
from scipy.spatial import distance

# Set the title of the Streamlit app
st.title('Mineral Processing Technology')

# Create a file uploader for the user to upload their image
uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg'])

if uploaded_file is not None:
    # Convert the file to an opencv image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    original_image = cv2.imdecode(file_bytes, 0)

    # Threshold the image
    _, binary_image = cv2.threshold(original_image, 127, 255, cv2.THRESH_BINARY_INV)

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)



    # Create a single image for overlaying all metrics
    image_color = cv2.cvtColor(original_image.copy(), cv2.COLOR_GRAY2BGR)

    # Calculate total surface area (TSA)
    total_area = sum(cv2.contourArea(contour) for contour in contours)
    cv2.putText(image_color, f'TSA: {total_area} pixels', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    # Find the largest contour
    largest_contour = max(contours, key=cv2.contourArea)
    largest_contour_reshaped = largest_contour.reshape(-1, 2)
    distances = distance.cdist(largest_contour_reshaped, largest_contour_reshaped, 'euclidean')
    max_distance = np.unravel_index(np.argmax(distances), distances.shape)
    major_axis_length = int(distances[max_distance])
    cv2.line(image_color, tuple(largest_contour_reshaped[max_distance[0]]), tuple(largest_contour_reshaped[max_distance[1]]), (255, 0, 0), 2)
    cv2.putText(image_color, f"Major Axis Length: {major_axis_length} Pixels", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    # Perimeter
    perimeter = sum(int(cv2.arcLength(contour, True)) for contour in contours)
    cv2.drawContours(image_color, contours, -1, (255, 0, 0), 2)
    cv2.putText(image_color, f'Perimeter: {perimeter} pixels', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    # Calculate the moments of the image for the centroid
    M = cv2.moments(original_image)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.circle(image_color, (cX, cY), 3, (255, 0, 0), -1)
    cv2.putText(image_color, f"Centroid: ({cX}, {cY})", (cX - 50, cY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    st.image(image_color, use_column_width=True)





    # Circle
    # Iterate over each contour to find the minimal enclosing circle for each contour
    image_color = cv2.cvtColor(original_image.copy(), cv2.COLOR_GRAY2BGR)
    for contour in contours:
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)

        # Increase the radius by a small factor (e.g., 5%)
        radius = int(radius * 1.018)

        # Draw the circle on the original image in red color
        cv2.circle(image_color, center, radius, (255, 0, 0), 2)

    st.subheader('SMALLEST CIRCLE')
    st.image(image_color, use_column_width=True)



    # Calculate total surface area (TSA)
    perimeter = 0
    total_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        total_area += area
        perimeter += int(cv2.arcLength(contour, True))

    
    image_color = cv2.cvtColor(original_image.copy(), cv2.COLOR_GRAY2BGR)
    font_scale = min(image_color.shape[0], image_color.shape[1])/1000
    # Write the TSA on the image
    cv2.putText(image_color, f'TSA: {total_area} pixels', (10, int(30 * font_scale)), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 0, 0), 1)
    st.subheader('TOTAL SURFACE AREA (TSA)')
    st.image(image_color, use_column_width=True)
    st.write(f'Total Surface Area: {total_area} pixels')

    

    # Major Axis Length
    # Find the largest contour
    largest_contour = max(contours, key=cv2.contourArea)

    # Reshape the largest contour to a 2D array
    largest_contour_reshaped = largest_contour.reshape(-1, 2)

    # Compute Euclidean distance between all points in the contour and find the maximum
    distances = distance.cdist(largest_contour_reshaped, largest_contour_reshaped, 'euclidean')
    max_distance = np.unravel_index(np.argmax(distances), distances.shape)

    # Get the points corresponding to the maximum distance
    point1 = tuple(largest_contour_reshaped[max_distance[0]])
    point2 = tuple(largest_contour_reshaped[max_distance[1]])

    # Draw a line between these points on the color image with reduced thickness
    image_color = cv2.cvtColor(original_image.copy(), cv2.COLOR_GRAY2BGR)
    cv2.line(image_color, point1, point2, (255, 0, 0), 2) 

    # Calculate font scale based on image size
    font_scale = min(image_color.shape[0], image_color.shape[1])/(25*len(f"Major Axis Length: {int(distances[max_distance])}"))

    # Write the length of the major axis on the image with adjusted font scale and reduced thickness
    cv2.putText(image_color,
                f"Major Axis Length: {int(distances[max_distance])} Pixels",
                (10,
                int(30 * font_scale)),
                cv2.FONT_HERSHEY_SIMPLEX,
                font_scale,
                (255,
                0,
                0),
                1) 

    st.subheader('MAJOR AXIS LENGTH')
    st.image(image_color, use_column_width=True)
    st.write(f'Major Axis Length: {int(distances[max_distance])} pixels')


    # Perimeter
    image_color = cv2.cvtColor(original_image.copy(), cv2.COLOR_GRAY2BGR)
    # Draw contours on a color version of the original image
    cv2.drawContours(image_color, contours, -1, (255, 0, 0), 2)
    # Calculate font scale based on image size
    font_scale = min(image_color.shape[0], image_color.shape[1])/1000

    # Write the perimeter on the image
    cv2.putText(image_color, f'Perimeter: {perimeter} pixels', (10, int(60 * font_scale)), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 0, 0), 1)

    st.subheader('PERIMETER')
    st.image(image_color, use_column_width=True)
    st.write(f'Perimeter: {perimeter} pixels')

    # Centroid
    # Calculate the moments of the image
    M = cv2.moments(original_image)

    # Calculate x,y coordinate of centroid
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    # Draw a red point at the centroid
    image_color = cv2.cvtColor(original_image.copy(), cv2.COLOR_GRAY2BGR)
    cv2.circle(image_color, (cX, cY), 3, (255, 0, 0), -1)

    # Calculate font scale based on image size
    font_scale = min(image_color.shape[0], image_color.shape[1])/(25*len(f"Centroid: ({cX}, {cY})"))

    # Write the coordinates on the image
    cv2.putText(image_color,
                f"Centroid: ({cX}, {cY})",
                (cX - 50,
                cY - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                font_scale,
                (255,
                0,
                0),
                1)

    st.subheader('CENTROID')
    st.image(image_color,use_column_width=True)
    st.write(f'Centroid: ({cX}, {cY})')
