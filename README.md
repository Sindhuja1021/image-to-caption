
# 📸 Image-to-Caption in Native Language 🗣️

An AI-powered open-source web app that helps users generate and contribute captions for images in their **native Indian languages**. The app combines **open-source image captioning** and **multilingual translation** to enable the creation of valuable multimodal corpora for underrepresented languages.

---

## 🚀 Features

- ✅ Upload your own image or choose from a sample set
- 📝 Write a caption in your native language (Telugu, Hindi, etc.)
- 🤖 Get AI-generated English captions using BLIP model
- 🌐 Translate captions into Indian languages using NLLB (No Language Left Behind)
- 💾 Save the caption-image pair as a contribution to an open corpus
- 🔁 Human-in-the-loop correction enabled
- 📦 Lightweight and can run on Hugging Face Spaces or local machines

---

## 🧠 Tech Stack

| Component       | Tools/Models Used                                  |
|-----------------|-----------------------------------------------------|
| Frontend        | [Streamlit](https://streamlit.io)                  |
| Image Captioning | [BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base) |
| Translation     | [NLLB-200](https://huggingface.co/facebook/nllb-200-distilled-600M) |
| Deployment      | [Hugging Face Spaces](https://huggingface.co/spaces) |
| Data Storage    | CSV / JSON based, extensible to database           |

---

## 🧪 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/your-username/describe-this.git
cd describe-this

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
````

---

## 📁 File Structure

```
describe-this/
├── app.py                   # Main Streamlit app
├── components/              # UI & logic modules
│   ├── upload.py
│   ├── caption_box.py
│   └── translation.py
├── ai/                      # AI model wrappers
│   ├── caption_generator.py
│   └── translator.py
├── assets/                  # Logo, icons
├── data/                    # Saved caption records
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📚 Dataset Goal

Each submission contributes:

* An image
* A caption in English (from AI)
* A caption in a selected Indian language (manual or translated)
* Language label (e.g., `ta` for Tamil, `te` for Telugu, `hi` for Hindi)

This creates a **multilingual, multimodal corpus** valuable for low-resource NLP tasks.

---

## 🤝 Team Contributions

| Name       | Role                               |
| ---------- | ---------------------------------- |
| Sriteja    | Frontend UI with Streamlit         |
| Vrishin    | Image captioning model integration |
| Sindhuja   | Translation model integration      |
| Nithin     | Data saving & export pipeline      |
| Bhavani    | Documentation & testing            |

---

## 🌐 Deployment

This app is deployed on **Hugging Face Spaces**:
🔗 [https://huggingface.co/spaces/your-team/describe-this](https://huggingface.co/spaces/your-team/describe-this)

---

## 🛡 License

This project is licensed under the **MIT License**. Feel free to use, extend, and contribute.

---

## 🧠 Inspired By

* The need for inclusive AI in Indian languages
* AI4Bharat’s IndicNLP & corpus work
* Hugging Face’s open-source vision

---

## 💡 Future Improvements

* Voice input via Whisper
* Caption quality scoring using BERTScore
* Gamified contributions & leaderboards
* Integration with Wikimedia Commons

---

🌱 Help us grow India's open-source multilingual corpus.
Contribute your caption and language today!

---
