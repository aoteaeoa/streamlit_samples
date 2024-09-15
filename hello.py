import streamlit as st
import datetime
from PIL import Image

dt_now = datetime.datetime.now()
st.write(":orange[Today is]", dt_now.year, dt_now.month, dt_now.day)

st.title("_Hello world!_")
st.write("You'll never find a rainbow if you're looking down. -Charles Chaplin-")
st.write("The flower that blooms in adversity is the rarest and most beautiful of all. -Walt Disney-")
st.write("The special secret of making dreams come true can be summarized in four C's. They are Curiosity, Confidence, Courage and Constancy. -Walt Disney-")
st.write("I will prepare and some day my chance will come. -Abraham Lincoln-")
st.write("Whatever you can do, or dream you can, begin it. Boldness has genius, power, and magic in it. -Johann Wolfgang von Goethe-")


# 画像を開く
img = Image.open("ocean.jpg")
# 画像を90度回転させる
rotated_img = img.transpose(Image.ROTATE_270)
# 回転した画像を保存する
rotated_img.save("rotated_ocean.jpg")

# st.image("rotated_ocean.jpg", caption="Blue Lake", width=200)

img = Image.open("garden.jpg")
rotated_img = img.transpose(Image.ROTATE_270)
rotated_img.save("rotated_garden.jpg")
# st.image("rotated_garden.jpg", caption="Japanese garden", width=200)

img = Image.open("pumpkins.jpg")
rotated_img = img.transpose(Image.ROTATE_270)
rotated_img.save("rotated_pumpkins.jpg")

img = Image.open("lotus.jpg")
rotated_img = img.transpose(Image.ROTATE_270)
rotated_img.save("rotated_lotus.jpg")

img = Image.open("yellow flower.jpg")
rotated_img = img.transpose(Image.ROTATE_270)
rotated_img.save("rotated_yellow flower.jpg")

img = Image.open("tulips.jpg")
rotated_img = img.transpose(Image.ROTATE_270)
rotated_img.save("rotated_tulips.jpg")


col1, col2, col3 = st.columns(3) #　画像を並べる
col4, col5, col6 = st.columns(3)

with col1:
    st.write("Blue calm lakeside")
    st.image("rotated_ocean.jpg", width = 200)

with col2:
    st.write("Japanese garden")
    st.image("rotated_garden.jpg", width = 200)

with col3:
    st.write("Autumn pumpkins")
    st.image("rotated_pumpkins.jpg", width = 200)

with col4:
    st.write("White lotus")
    st.image("rotated_lotus.jpg", width = 200)

with col5:
    st.write("Yellow flower")
    st.image("rotated_yellow flower.jpg", width = 200)

with col6:
    st.write("Yellow tulips")
    st.image("rotated_tulips.jpg", width = 200)