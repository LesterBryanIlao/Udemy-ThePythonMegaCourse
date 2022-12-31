import cv2
import glob

images = glob.glob("*.jpg")
print(images)

def resizeImage(image_name):
    img = cv2.imread(image_name, 0)
    resized_image = cv2.resize(img, (100, 100))
    cv2.imshow(image_name, resized_image)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite(image_name.split(".")[0]+"_resized.jpg", resized_image)
    

for image in images:
    resizeImage(image)
