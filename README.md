# Mineral Processing Technology - Streamlit App

This Streamlit application, "Mineral Processing Technology," allows users to upload an image containing mineral particles and provides various measurements and visualizations related to the mineral particles, including the smallest enclosing circle, total surface area, major axis length, perimeter, and centroid.

## Getting Started

To run this Streamlit app locally, follow the steps below:

### Prerequisites

Before running this application, ensure you have the following installed:

- Python: This application is written in Python, so you'll need to have Python installed on your system.
- Python packages: You will need the following Python packages installed. You can install them using pip:

    ```bash
    pip install streamlit opencv-python numpy scipy
    ```

### Running the App

1. Clone this GitHub repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/Mineral-Processing-Technology.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Mineral-Processing-Technology
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run mineral_processing_technology.py
    ```

4. The application should open in your default web browser. You can now use it to upload an image and view the results.

## Usage

1. Upload an image containing mineral particles by clicking the "Choose an image..." button.

2. The application will process the uploaded image and display the following information:

   - **Smallest Enclosing Circle**: This shows the smallest circle that encloses each mineral particle.
   
   - **Total Surface Area (TSA)**: This displays the total surface area of all mineral particles in the image.

   - **Major Axis Length**: This provides the length of the major axis of the largest mineral particle.

   - **Perimeter**: The perimeter of the mineral particles in the image is displayed.

   - **Centroid**: The application calculates and displays the centroid of the mineral particles.

## Acknowledgments

This Streamlit application was created as part of a project on mineral processing technology. It uses Python, OpenCV, and Streamlit to perform image processing and analysis.

## Author
- Sai Pranav Tumu
- GitHub: github.com/Sai-Pranav-Tumu
