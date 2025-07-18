# app.py
import streamlit as st
import geocoder
from PIL import Image
import os
import uuid
import pandas as pd
from datetime import datetime
from translator import translate, nllb_lang_map

# --- Setup ---
st.set_page_config(page_title="Describe This", layout="centered")
st.title("🖼️ Describe This – Image-to-Caption in Native Language")

# --- Ensure data folders exist ---
os.makedirs("data/images", exist_ok=True)
os.makedirs("data", exist_ok=True)
csv_file = "data/captions.csv"
if not os.path.exists(csv_file):
    pd.DataFrame(columns=[
        "timestamp", "name", "email", "location",
        "title", "description", "category",
        "latitude", "longitude", "caption", "translated_caption"
    ]).to_csv(csv_file, index=False)

# --- Contributor Info ---
st.subheader("👤 Contributor Information (Required)")
name = st.text_input("Full Name")
email = st.text_input("Email")
location = st.text_input("City or Location")
consent = st.checkbox("✅ I consent to the use of my data for open-source AI research.")

if not all([name, email, location, consent]):
    st.warning("Please complete all required fields before uploading.")
else:
    st.subheader("📸 Upload Your Image")
    image_file = st.file_uploader("Upload an image (JPEG/PNG)", type=["jpg", "jpeg", "png"])

    if image_file:
        st.image(Image.open(image_file), caption="Uploaded Image", use_column_width=True)

        # --- Metadata Entry ---
        st.subheader("🏷 Add Image Details")
        title = st.text_input("Title for the image")
        description = st.text_area("Brief description (context, event, background, etc.)")
        category = st.selectbox("Category", [
            "Cultural Event", "Festival", "Street Scene", "Food", "Object", "Nature", "People", "Other"
        ])

        # --- Location ---
        st.write("🌐 Geo Coordinates (auto-filled, editable)")
        try:
            g = geocoder.ip("me")
            lat = st.number_input("Latitude", value=g.latlng[0])
            lon = st.number_input("Longitude", value=g.latlng[1])
        except Exception as e:
            st.warning(f"⚠ Could not fetch location automatically. Error: {e}")
            lat = st.number_input("Latitude (manual entry)", value=0.0)
            lon = st.number_input("Longitude (manual entry)", value=0.0)

        # --- Caption Input or Generation ---
        st.subheader("✍ Captioning")
        user_caption = st.text_area("Enter your caption in your native language (or leave blank to auto-generate):")
        generate = st.button("✨ Generate AI Caption (optional)")

        final_caption = ""
        if generate and not user_caption:
            final_caption = "A group of people celebrating a festival"
            st.success(f"💬 AI-Generated Caption (English): {final_caption}")
        elif user_caption:
            final_caption = user_caption
            st.success(f"📝 You entered: {final_caption}")

        # --- Translation ---
        translated_caption = ""
        if final_caption:
            st.subheader("🌍 Translate Caption")
            source_lang = st.selectbox("Source Language", list(nllb_lang_map.keys()), index=2)  # Default: Telugu
            target_lang = st.selectbox("Target Language", list(nllb_lang_map.keys()), index=0)  # Default: English

            if st.button("Translate"):
                translated_caption = translate(final_caption, source_lang, target_lang)
                st.success(f"📘 Translated Caption ({target_lang}): {translated_caption}")

        # --- Submit Button ---
        if st.button("📥 Submit"):
            unique_img_name = f"{uuid.uuid4()}.png"
            img_path = os.path.join("data/images", unique_img_name)
            with open(img_path, "wb") as f:
                f.write(image_file.getbuffer())

            df = pd.read_csv(csv_file)
            new_row = {
                "timestamp": datetime.now().isoformat(),
                "name": name,
                "email": email,
                "location": location,
                "title": title,
                "description": description,
                "category": category,
                "latitude": lat,
                "longitude": lon,
                "caption": final_caption,
                "translated_caption": translated_caption
            }
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv(csv_file, index=False)

            st.success("✅ Data saved successfully!")

# --- Export Button ---
st.subheader("📦 Export Dataset")
with open(csv_file, "rb") as f:
    st.download_button("📥 Download Captions CSV", f, file_name="captions.csv")
