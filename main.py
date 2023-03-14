import cv2
import easyocr
import matplotlib.pyplot as plt

# read image
# image_path = 'images/traffic_sign_2.jpg'
image_path = 'images/placa_transito_2.jpg'


img = cv2.imread(image_path)

# instance text detector
languages = ['en', 'pt']
reader = easyocr.Reader(languages, gpu=False)

# detect text on image
text_ = reader.readtext(img)

# draw bbox and text
for t in text_:
    print(t)     

    bbox, text, score = t

    # represents the top left corner of rectangle
    start_point = (int(bbox[0][0]), int(bbox[0][1]))

    # represents the bottom right corner of rectangle
    end_point = (int(bbox[2][0]), int(bbox[2][1]))

    # Black color in BGR
    color = (0, 255, 0)

    # Thickness of -1 will fill the entire shape
    thickness = 5

    cv2.rectangle(img, start_point, end_point, color, thickness)
    cv2.putText(img, text, start_point, cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()    