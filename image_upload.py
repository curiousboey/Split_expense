import cv2
from matplotlib import pyplot as plt

# create figure
fig = plt.figure(figsize=(10, 7))

# setting values to rows and column variables
rows = 4
columns = 3

# reading images
Image1 = cv2.imread('Image1.jpg')
Image2 = cv2.imread('Image2.jpg')
Image3 = cv2.imread('Image3.jpg')
Image4 = cv2.imread('Image4.jpg')
Image5 = cv2.imread('Image5.jpg')
Image6 = cv2.imread('Image6.jpg')
Image7 = cv2.imread('Image7.jpg')
Image8 = cv2.imread('Image8.jpg')
Image9 = cv2.imread('Image9.jpg')

plt.text(0.2, 0.8, 'Parabola $Y = x^2$', fontsize = 22)

plt.title("Expenses Calculation",
          fontsize='20',
          backgroundcolor='green',
          color='white')
# Adds a subplot at the 1st position
fig.add_subplot(rows, columns, 4)

# showing image
plt.imshow(Image1)
plt.axis('off')
plt.title("First")

# Adds a subplot at the 2nd position
fig.add_subplot(rows, columns, 5)

# showing image
plt.imshow(Image2)
plt.axis('off')
plt.title("Second")

# Adds a subplot at the 3rd position
fig.add_subplot(rows, columns, 6)

# showing image
plt.imshow(Image3)
plt.axis('off')
plt.title("Third")

# Adds a subplot at the 4th position
fig.add_subplot(rows, columns, 7)

# showing image
plt.imshow(Image4)
plt.axis('off')
plt.title("Fourth")


fig.add_subplot(rows, columns, 8)

# showing image
plt.imshow(Image5)
plt.axis('off')
plt.title("Fifth")


fig.add_subplot(rows, columns, 9)

# showing image
plt.imshow(Image6)
plt.axis('off')
plt.title("Sixth")


fig.add_subplot(rows, columns, 10)

# showing image
plt.imshow(Image7)
plt.axis('off')
plt.title("Seventh")


fig.add_subplot(rows, columns, 11)

# showing image
plt.imshow(Image8)
plt.axis('off')
plt.title("Eighth")


fig.add_subplot(rows, columns, 12)

# showing image
plt.imshow(Image9)
plt.axis('off')
plt.title("Ninth")