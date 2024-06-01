import requests
import cv2
import pytesseract

URL = 'https://www.abhilekh-patal.in/jspui/password-login?captcha=captcha'
response = requests.get(URL)

if response.status_code == 200:
    # Get the content of the response (image data)
    image_data = response.content

    # Save the image to a file
    with open('image.jpg', 'wb') as file:
        file.write(image_data)
        print('Image downloaded successfully.')
else:
    print('Failed to download the image. Status code:', response.status_code)


image1 = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
_, thresh1 = cv2.threshold(image1, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
opening = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
# cv2.imwrite('result_image.jpg', image1)
# cv2.imshow('Image', opening)
# cv2.waitKey(0)  # Wait for a key press
# cv2.destroyAllWindows()

text1 = pytesseract.image_to_string(opening, lang="eng")
print(text1)