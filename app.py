import streamlit as st
import cv2
import numpy as np
from text_extraction import extract_text  # Import the function from text_extraction.py

st.title("License Plate Detection and Recognition")
st.write("Upload an image to detect license plates and extract text from them.")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    st.image(image[:, :, ::-1], caption="Uploaded Image", use_column_width=True)

    annotated_image, detected_text = extract_text(image)

    if detected_text:
        st.write(f"Detected Text: {detected_text}")
    else:
        st.write("No license plate detected.")

    st.image(annotated_image[:, :, ::-1], caption="Processed Image with Annotations", use_column_width=True)
