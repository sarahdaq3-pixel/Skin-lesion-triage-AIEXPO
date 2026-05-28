import streamlit as st
import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
import os

st.set_page_config(page_title="Skin Lesion Triage", page_icon="🩺", layout="centered")
st.title("🩺 Skin Lesion Triage Assistant")
st.markdown("**AI-powered screening for primary care clinics**")

@st.cache_resource
def load_model():
    model = models.efficientnet_b0(weights=None)
    num_features = model.classifier[1].in_features
    model.classifier[1] = nn.Linear(num_features, 1)
    if os.path.exists("models/best_model.pt"):
        model.load_state_dict(torch.load("models/best_model.pt", map_location="cpu", weights_only=True))
    model.eval()
    return model

def preprocess_image(image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0)

uploaded_file = st.file_uploader("Upload dermoscopic image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Uploaded Image")
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, use_column_width=True)
    
    with st.spinner("Analyzing..."):
        model = load_model()
        img_tensor = preprocess_image(image)
        with torch.no_grad():
            output = model(img_tensor)
            prob = torch.sigmoid(output).item()
    
    pred = "Suspicious" if prob > 0.5 else "Benign"
    conf = (prob if prob > 0.5 else 1 - prob) * 100
    
    with col2:
        st.subheader("AI Assessment")
        if pred == "Suspicious":
            st.error(f"🚨 Result: SUSPICIOUS")
            st.error(f"Confidence: {conf:.1f}%")
            st.error("Refer to dermatologist")
        else:
            st.success(f"✅ Result: BENIGN")
            st.success(f"Confidence: {conf:.1f}%")
            st.success("Routine monitoring")
    
    st.markdown("---")
    st.progress(prob)
    st.caption(f"Risk Score: {prob*100:.1f}%")
else:
    st.info("👆 Upload an image to begin")