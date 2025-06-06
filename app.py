import streamlit as st
from video_generator import generate_video

st.title("🎥 Faceless Video Creator")

script = st.text_area("Enter your script or story:")
video_type = st.selectbox("Choose video type:", ["Story", "Quote", "News"])
generate = st.button("Generate Video")

if generate and script:
    with st.spinner("Generating video..."):
        output_path = generate_video(script, video_type)
        st.success("✅ Video generated!")
        st.video(output_path)
        st.markdown(f"[Download Video]({output_path})")
