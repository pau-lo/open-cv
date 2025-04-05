import cv2 as cv
import os

# Define a function to load image from file
def load_image(file_path):
    """
    Loads image from the given file path.

    Args:
        file_path (str): Path to the image file.

    Returns:
        numpy.ndarray: The loaded image.
    """
    return cv.imread(file_path)

# Load the image from a file with a hidden path
# file_path = "./images/baby-color-kitten.jpg"
# image = load_image(file_path)

# Alternatively, you could hardcode the path into the file instead of passing it as an argument.
image_path = os.path.join(os.path.dirname(__file__), 'images', 'baby-color-kitten.jpg')
image = load_image(image_path)

# Convert to grayscale
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Show the grayscale image
cv.imshow("Grayscale Image", gray_image)
cv.waitKey(0)
cv.destroyAllWindows()

# Alternatively, you could hardcode the path into the file instead of passing it as an argument.
image_path = os.path.join(os.path.dirname(__file__), 'images', 'baby-color-kitten.jpg')
image = load_image(image_path)
