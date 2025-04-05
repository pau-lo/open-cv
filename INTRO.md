# Introduction to Computer Vision with OpenCV

## 1. What is an Image?

An **image** is a 2D grid of **pixels** (picture elements). Each pixel holds color/brightness information.  
- **Example**: A 640x480 image has 640 columns and 480 rows of pixels.

```python
import cv2
image = cv2.imread("image.jpg")
print(image.shape)  # Output: (height, width, channels)
```

---

## 2. What is a Pixel?

A **pixel** is the smallest unit in an image. In color images, pixels are represented as a tuple of **(B, G, R)** values, each ranging from 0 to 255.

```python
pixel_value = image[100, 100]  # Get pixel at (100, 100)
print(pixel_value)  # Output: [B, G, R] e.g., [255, 0, 0] for blue
```

---

## 3. RGB Color Channels

- **R (Red)**, **G (Green)**, and **B (Blue)** channels combine to create colors.  
- Each channel is a 2D matrix of intensity values (0–255).

```python
blue_channel = image[:, :, 0]  # Extract the blue channel
```

---

## 4. Grayscale

A grayscale image converts RGB values to a single intensity value (0–255) using a weighted average:  
`Y = 0.299*R + 0.587*G + 0.114*B`.

```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

---

## 5. HSV Color Space

- **Hue** (color), **Saturation** (intensity), and **Value** (brightness).  
- Useful for color-based segmentation.

```python
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
```

---

## 6. Image Histogram

A histogram shows the distribution of pixel intensities.  
- **Applications**: Contrast adjustment, thresholding.

```python
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
```

---

## 7. 2D Convolution

A mathematical operation where a kernel (small matrix) slides over the image to apply effects like blurring or edge detection.

---

## 8. Average Filtering

Blurs an image by replacing each pixel with the average of its neighbors.  
- **Kernel example**: 3x3 matrix with all values = 1/9.

```python
blur = cv2.blur(image, (3, 3))
```

---

## 9. Median Filtering

Reduces noise by replacing pixels with the median of neighboring values. Effective for "salt-and-pepper" noise.

```python
median = cv2.medianBlur(image, 5)
```

---

## 10. Gaussian Filtering

Blurs using a Gaussian kernel (weights pixels by distance from the center).  
- **Sigma** controls the spread.

```python
gaussian = cv2.GaussianBlur(image, (5, 5), 0)
```

---

## 11. Image Thresholding

Converts grayscale to binary using a threshold value.  
- **Types**: Binary, Adaptive, Otsu’s.

```python
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
```

---

## 12. Image Gradient

Measures intensity changes in x/y directions. Used for edge detection.  
- **Sobel operators**: Compute gradients.

```python
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
```

---

## 13. Canny Edge Detection

A multi-step edge detection algorithm:  
1. Noise reduction (Gaussian blur).  
2. Gradient calculation.  
3. Non-maximum suppression.  
4. Hysteresis thresholding.

```python
edges = cv2.Canny(gray, 100, 200)
```

---

## 14. Line Detection (Hough Line Transform)

Detects lines in an image using polar coordinates (ρ, θ).  
- **Probabilistic Hough**: Efficient for detecting line segments.

```python
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=10, maxLineGap=10)
```

---

## 15. Harris Corner Detection

Identifies corners by analyzing intensity variations in multiple directions.  
- **Corners** have high gradients in two directions.

```python
corners = cv2.cornerHarris(gray, 2, 3, 0.04)
image[corners > 0.01 * corners.max()] = [0, 0, 255]  # Mark corners in red
```

---

## 16. SIFT Feature Detection

**Scale-Invariant Feature Transform (SIFT)** detects and describes keypoints invariant to scale/rotation.

```python
sift = cv2.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(gray, None)
```

---

## 17. Optical Flow Object Tracking

Estimates motion vectors between consecutive frames (e.g., Lucas-Kanade method).

```python
old_pts = cv2.goodFeaturesToTrack(old_gray, maxCorners=100, qualityLevel=0.3, minDistance=7)
new_pts, status, err = cv2.calcOpticalFlowPyrLK(old_gray, new_gray, old_pts, None)
```

---

## 18. Camera Calibration

Corrects lens distortion using a chessboard pattern.  
- Computes **camera matrix** and **distortion coefficients**.

```python
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)
```

---

## 19. Pose Estimation

Estimates the 3D pose of an object using 2D-3D point correspondences (Perspective-n-Point).

```python
ret, rvec, tvec = cv2.solvePnP(objp, imgp, mtx, dist)
```

---

## 20. Depth Estimation (Depth Map)\

Computes depth using stereo images.  
- **Disparity map**: Difference in pixel coordinates between left/right images.

```python
stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(left_img, right_img)
```

---
