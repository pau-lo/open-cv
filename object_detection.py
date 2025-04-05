import cv2 as cv

# Load the image
image = cv.imread(
    "./open-cv/sample-images/baby-color-kitten.jpg"
)  # Replace with your image file

# Convert to grayscale
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Show the grayscale image
cv.imshow("Grayscale Image", gray_image)
cv.waitKey(0)
cv.destroyAllWindows()
