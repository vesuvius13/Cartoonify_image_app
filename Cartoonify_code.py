import cv2
import numpy as np
import streamlit as st

st.title("Cartoonify App")

st.write(
    """This app creates a filtered version of the image you provide, start by uploading an image 👇
    """
)

uploaded_file = st.file_uploader("Upload Files", type=["jpeg", "jpg", "png", "jiff"])

if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)



def color_quantization(img, k):
  data = np.float32(img).reshape((-1, 3))

  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)
  ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
  center = np.uint8(center)
  result = center[label.flatten()]
  result = result.reshape(img.shape)
  return result

try:

    total_color = 12

    results = color_quantization(opencv_image, total_color)
    col1, col2 = st.beta_columns(2)

    col1.image(opencv_image, use_column_width=True, channels="BGR", caption="Original")

    col2.image(results, use_column_width=True, channels = "BGR",caption="Filtered")

except:
    pass

  







