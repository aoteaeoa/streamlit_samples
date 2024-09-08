import streamlit as st

from PIL import Image

st.title("Hello world!")
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


col1, col2, col3 = st.columns(3) #　画像を並べる

with col1:
    st.header("Blue calm lakeside")
    st.image("rotated_ocean.jpg", width = 200)

with col2:
    st.header("Japanese garden")
    st.image("rotated_garden.jpg", width = 200)

with col3:
    st.header("Autumn pumpkins")
    st.image("rotated_pumpkins.jpg", width = 200)
