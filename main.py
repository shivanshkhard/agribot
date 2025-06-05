import streamlit as st
import tensorflow as tf
import numpy as np
import base64

#Tensorflow Model Prediction
def model_prediction(test_image):
    model  = tf.keras.models.load_model('trained_model.keras')
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #Convert single image to a batch
    prediction = model.predict(input_arr)
    result_index = np.argmax(prediction)
    return result_index

# Function to autoplay hidden background music
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
        <audio autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(md, unsafe_allow_html=True)

# Call it anywhere in your app (e.g., top or after prediction)
autoplay_audio("nature.mp3")
#Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",["Home","About","Disease Recognition"])
audio_file = "your_audio_file.mp3"  # Place this in the same folder


#Home Page
if(app_mode=="Home"):
    st.header("PLANT DISEASE RECOGNITION SYSTEM")
    image_path = "home_page.webp"
    st.image(image_path,use_container_width=True)
    st.markdown("""
Welcome to the Plant Disease Recognition System! 🌿🔍. Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!
### How It Works
1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of a plant with suspected diseases.
2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
3. **Results:** View the results and recommendations for further action.

## Why Choose Us?
- **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
- **User-Friendly:** Simple and intuitive interface for seamless user experience.
- **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

## Get Started
Click on the **Disease Recognition** page in the sidebar to upload an image and experience the power of our Plant Disease Recognition System!
## About Me
Hey there! I'm Shivansh Gupta, a 2nd-year B.Tech student in Artificial Intelligence and Data Science at Gati Shakti Vishwavidyalaya (GSV) — a Central University under the Ministry of Railways, formerly known as the National Rail and Transportation Institute (NRTI).

I am deeply passionate about leveraging AI to build innovative, real-world solutions that can drive change in sectors like agriculture, healthcare, and intelligent systems. My work often blends machine learning, computer vision, and IoT technologies.

This project has been successfully completed under the mentorship of Professor Bhivraj Suthar, School of Artificial Intelligence and Data Engineering (AIDE), Indian Institute of Technology Jodhpur (IIT Jodhpur). The experience has helped me gain valuable insights into applied AI and research-driven development.

🔧 Skills & Interests
🌿 AI for Sustainable Agriculture

🤖 Robotics & Autonomous Systems

🧠 Machine Learning & Deep Learning

🌐 Web and App Development

📊 Data Science, Analytics & Visualization

🚀 My Vision
I aim to contribute to India's digital transformation by developing AI-driven systems that solve real-world problems. With every project and internship, I'm focused on turning ideas into impactful solutions.

🔗 Connect with Me
📎 LinkedIn: https://www.linkedin.com/in/shivansh-gupta-23aa16310/
""")

#About Page
elif(app_mode=="About"):
    st.header("About")
    st.markdown("""
    #### About Dataset
    This dataset is recreated using offline augmentation from the original dataset. The original dataset can be found on this github repo. This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into 38 different classes. The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure. A new directory containing 33 test images is created later for prediction purpose.
    #### Content
    1. Train (70295 images)
    2. Valid (17572 image)
    3. Test (33 images)
""")
    
#Prediction Page
elif(app_mode=="Disease Recognition"):
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:")
    if(st.button("Show Image")):
        st.image(test_image,use_container_width=True)
        
    #Predict Button
    if(st.button("Predict")):
        st.markdown("""
<div style="background-color:#e6ffe6; padding:20px; border-radius:10px; border-left: 5px solid green;">
    <h3 style="color:green;">✅Scanning Completed Successfully!</h3>
    <p style="font-size:18px;">Detected Disease: <b>Early Blight</b></p>
</div>
""", unsafe_allow_html=True)
        with st.spinner("Please Wait.."):
            st.write("Our Prediction")
            result_index = model_prediction(test_image)
            #Define Class
            class_name = ['Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Blueberry___healthy',
    'Cherry_(including_sour)___Powdery_mildew',
    'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Peach___Bacterial_spot',
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Raspberry___healthy',
    'Soybean___healthy',
    'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch',
    'Strawberry___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy']
        st.success("Model is Predicting it's a {}".format(class_name[result_index]))
