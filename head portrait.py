#Author: Stan Yin
#GitHub Name: SomeB1oody
#This project is based on CC 4.0 BY, please mention my name if you use it.
#This project requires opencv.
import cv2 as cv

print("Please enter image location\t")
print("Example: C:\\Wallpaper\\02.png\t")
path = input("Enter HERE: ")
img = cv.imread(path, cv.IMREAD_COLOR)

if img is None:
    raise ValueError("Could not open image\t")

row = img.shape[0] // 2
col = img.shape[1] // 2

circle_radius = 0
if img.shape[1] < img.shape[0]:
    circle_radius = img.shape[1] // 3
else:
    circle_radius = img.shape[0] // 3

max_radius = row // 2

global output_img

def draw_circle():
    global output_img
    output_img = img.copy()
    output_img = cv.circle(output_img, (col, row), circle_radius, (0, 0, 255), thickness=2)
    cv.imshow("Adjust", output_img)

def max_radius_():
    global max_radius
    row_distance = img.shape[0] - row - 1
    col_distance = img.shape[1] - col - 1
    _max_radius = max(max(row_distance, col_distance), max(row, col))
    if _max_radius <= max_radius:
        print("already reach limit")
        max_radius = _max_radius

def radius_track_bar(_radius):
    global circle_radius
    circle_radius = _radius
    draw_circle()

def col_track_bar(_col):
    global col
    col = _col
    draw_circle()

def row_track_bar(_row):
    global row
    row = _row
    draw_circle()

cv.namedWindow("Adjust")
cv.createTrackbar("Col", "Adjust", col, img.shape[1], col_track_bar)
cv.createTrackbar("Row", "Adjust", row, img.shape[0], row_track_bar)
cv.createTrackbar("Radius", "Adjust", circle_radius, max_radius, radius_track_bar)
draw_circle()
cv.waitKey(0)
cv.destroyAllWindows()
