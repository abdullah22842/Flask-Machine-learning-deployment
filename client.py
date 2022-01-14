import base64
import json
import cv2
import requests
import matplotlib.pyplot as plt
#api = 'https:///210.114.1.34:22/Face_shape'
#api = 'https://203.241.246.174:55000/Face_shape'
api='https://211.110.1.73:443/Face_shape'
image_file = 'C:\\Users\\2109902\\Desktop\\results\\1 (59).jpg'
#image_file = 'E:\\projects\\Face shape classification\\spyder\\data\\Crop img_test_1\\train_image\\so_yang\\soYang (12).bmp'
#image_file = 'E:\\projects\\Face shape classification\\spyder\\data\\Crop img_test_1\\train_image\\Ta_Eum\\taEum (19).bmp'
#image_file = 'E:\\projects\\Face shape classification\\spyder\\data\\Crop img_test_1\\Ta_yang\\taYang (9).bmp'

with open(image_file, "rb") as f:
    im_bytes = f.read()
im_b64 = base64.b64encode(im_bytes).decode("utf8")

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

payload = json.dumps({"image": im_b64})
response = requests.post(api, data=payload, headers=headers, verify=False)

image=cv2.imread(image_file)
try:
    data = response.json()
    print(data)
    plt.imshow(image)
except requests.exceptions.RequestException:
    print(response.text)
