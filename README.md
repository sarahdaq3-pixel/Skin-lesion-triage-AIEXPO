# 🩺 SkinGuard AI

**Building a Healthier Jordan**

AI-powered skin lesion triage assistant for primary care clinics in resource-limited settings.

[![Watch the Demo](https://img.shields.io/badge/Watch-Demo-red?style=for-the-badge&logo=youtube)](https://youtu.be/DCFckyiwhow?is=-JokTHGGdpHVJQMU)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Overview

SkinGuard AI is a web-based screening tool that helps general practitioners in Jordan triage skin lesions by classifying them as **Benign** (routine monitoring) or **Suspicious** (refer to dermatologist). Built with deep learning and designed for accessibility in resource-limited healthcare settings.

### Key Features
- ✅ Real-time binary classification of dermoscopic images
- ✅ Confidence scoring with clinical recommendations
- ✅ Browser-based interface (no installation required)
- ✅ 77.9% validation accuracy on HAM10000 dataset
- ✅ Open-source and transparent

---

## 🎥 Demo Video

Watch our full project demonstration:

**[SkinGuard AI - AI Expo Jordan 2026 Demo](https://youtu.be/DCFckyiwhow?is=-JokTHGGdpHVJQMU)**

The video includes:
- Problem statement and healthcare context
- Technical implementation walkthrough
- Live demo with test cases
- Impact and future work

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- PyTorch
- Streamlit

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/sarahdaq3/Skin-Lesion-Triage-AI.gitcd Skin-Lesion-Triage-AI
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Training the Model

To retrain the model from scratch:

1. Download the HAM10000 dataset from [ISIC Archive](https://www.isic-archive.com/)
2. Place images in `dataset/images/` folder
3. Run the training notebook:
```bash
jupyter notebook main_notebook.ipynb
```
4. Execute all cells to train and save the model

---

## 🧠 Technical Details

### Model Architecture
- **Backbone**: EfficientNet-B0 (pre-trained on ImageNet)
- **Classification Head**: Binary classification layer (1 output)
- **Input Size**: 224×224 pixels
- **Activation**: Sigmoid for probability output
- **Threshold**: 0.5 for binary decision

### Training Configuration
- **Dataset**: HAM10000 (10,015 dermoscopic images)
- **Split**: 80% train / 20% test
- **Optimizer**: AdamW (lr=3e-4)
- **Loss**: Binary Cross-Entropy
- **Batch Size**: 32
- **Early Stopping**: Patience=3 epochs
- **Best Validation Accuracy**: 77.92%
- **Best Validation Loss**: 0.6114

### Preprocessing
- Resize to 224×224- Normalize using ImageNet mean/std:
  - Mean: [0.485, 0.456, 0.406]
  - Std: [0.229, 0.224, 0.225]

---

## 📂 Project Structure
Skin-Lesion-Triage-AI/
├── main_notebook.ipynb          # Complete training pipeline
├── app.py                       # Streamlit web application
├── best_model.pt                # Trained model weights (~16 MB)
├── requirements.txt             # Python dependencies
├── training_curves.png          # Loss/accuracy visualization
├── README.md                    # This file
└── dataset/
    ├── images/                  # Dermoscopic images
    └── test.csv                 # Test set metadata
```
---

## 📊 Dataset

**Source**: [HAM10000](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T)  
**License**: CC-BY-NC 4.0  
**Citation**: Tschandl, P., Rosendahl, C. & Kittler, H. The HAM10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions. Sci Data 5, 180161 (2018).

### Class Distribution
- **Benign**: Nevus, Benign Keratosis, Dermatofibroma (~79%)
- **Suspicious**: Melanoma, Basal Cell Carcinoma, Actinic Keratosis, Vascular Lesions (~21%)

---

## 🔬 Results

### Performance Metrics
- **Validation Accuracy**: 77.92%
- **Test Accuracy**: ~77%
- **Model Size**: ~16 MB
- **Inference Time**: <1 second per image

### Sample Predictions

| Image | True Label | Prediction | Confidence |
|-------|-----------|------------|------------|
| Benign lesion | Benign | ✅ Benign | 65.7% |
| Suspicious lesion | Suspicious | 🚨 Suspicious | 81.4% |

---

## ⚠️ Disclaimer

**This tool is for educational and screening purposes only.**

SkinGuard AI is designed as a **decision-support tool** to assist healthcare professionals in triaging skin lesions. It is **NOT** a replacement for:
- Professional medical diagnosis
- Dermatologist consultation
- Clinical judgment

Always confirm AI predictions with a qualified healthcare provider. Low-confidence predictions (<60%) should always be reviewed by a specialist.

---

## 🛣️ Future Work

1. **Domain Adaptation**: Collect and train on Jordanian dermoscopic images for better local performance
2. **Explainability**: Integrate Grad-CAM heatmaps to show which lesion regions influenced predictions
3. **Mobile App**: Develop offline-capable mobile version for rural clinics
4. **Multi-class Classification**: Expand beyond binary to specific lesion types
5. **Clinical Validation**: Partner with Jordanian healthcare providers for real-world testing

---

## 👥 Team

**Team Name**: SkinGuard AI  
**Competition**: AI Expo Jordan 2026  
**Category**: Healthcare / AI for Social Good

**Team Members**:
- **Sarah Khalad Daqrouq** - Lead Developer & Project Lead

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.

This project is open-source to encourage transparency, collaboration, and adoption in global health AI initiatives.

---

## 🙏 Acknowledgments

- **Dataset**: International Skin Imaging Collaboration (ISIC)
- **Framework**: PyTorch, Streamlit
- **Support**: AI Expo Jordan 2026, IEEE CIS University of Jordan

---

## 📞 Contact

For questions, collaboration, or deployment inquiries:
- **Email**: sarahdaq3@gmail.com
- **GitHub**: [sarahdaq3](https://github.com/sarahdaq3)

---

**Built with ❤️ for a healthier Jordan**
