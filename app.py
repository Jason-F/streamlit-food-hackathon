import streamlit as st
from streamlit_juxtapose import juxtapose

from PIL import Image
import requests

import pathlib
import pandas as pd
import cv2
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
from IPython.display import Image
from skimage.metrics import structural_similarity
import os
from streamlit_image_comparison import image_comparison
from PIL import Image
#%matplotlib inline

def check_image(image1, image2):
    # To check if images exist
    from os.path import exists
    if exists(image1) and exists(image2):
        print("Files are available. Images should have the same shape")
        img1 = cv2.imread(image1)
        img2 = cv2.imread(image2)
        st.write("Image file 1:", image1, " shape =", img1.shape)
        st.write("Image file 2:", image2, " shape =", img2.shape)
        if img1.shape == img2.shape:
            st.write('`Matched encoding`')
        else:
            st.write('`Unmatched encoding`')
        
    else:
        print("Error!")
        if not exists(image1):
            print(image1, ' is not available')
        if not exists(image2):
            print(image2, ' is not available')
def main():

    page_options = ["Select Data","Structural Similarity Index", "Computer Vision Model", "GPT", "About Us"]

    # -------------------------------------------------------------------
    # ----------------- !! Main code section !! -------------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Select Data":
        # Header contents
        st.write('# Planogram Compliance Model')
        st.image('images/logo1.jpg')
        st.image('images/header1.png')
        st.write('## Upload planogram and realogram data')
        
        planogram_file = st.file_uploader("Choose Planogram",type = 'jpeg')
        realogram_file = st.file_uploader("Upload Realogram",type = 'jpeg')
        if st.button('Submit'):

            image_comparison(
                img1=Image.open(planogram_file),
                img2=Image.open(realogram_file),
                label1="Planogram",
                label2="Realogram",
            )
            plan_filepath = 'images/'+planogram_file.name
            real_filepath = 'images/'+realogram_file.name
            check_image(plan_filepath,real_filepath)
            
        
    if page_selection == "Structural Similarity Index":
        st.title("Structural Similarity Index")
        st.markdown("""Identifying the differences between realogram and planogram""")

    if page_selection == "Computer Vision Model":
        st.title("Computer Vision")
        st.markdown("""Utilizing Azure's Computer Vision model""")


    if page_selection == "GPT":
        st.title("GPT 4o")
        st.markdown("""Utilizing GPT for descriptive anaylsis""")

    if page_selection == "About Us":
        st.info('**The legends who made it happen**')
        st.write('**Jason Farrell** - Senior Data Scientist')
        st.write('**Rod Morgan** - Senior Data Scientist')
        st.write('**Keanu Gertse** - Data Scientist')
        
        st.image('images/logo1.jpg')


if __name__ == '__main__':
    main()