# 🏠 Home Harmony AI System

An AI-powered platform that transforms the home design experience by combining machine learning, recommendation systems, and computer vision.

---

## 🚀 Features

### 🔹 Designer Matchmaking
- Built using Random Forest (91.3% accuracy)
- Matches users with designers based on:
  - Style
  - Budget
  - Location

### 🔹 Furniture Recommendation System
- Collaborative filtering (user-based & item-based)
- Uses cosine similarity to suggest products

### 🔹 Image & Text-Based Search
- CLIP (ViT-B/32) for embeddings
- FAISS for fast similarity search
- Supports:
  - Image upload → find similar furniture
  - Text search → “modern chair” → results

---

## 🧠 My Role

I independently designed and developed the entire AI system including:
- Model selection and training
- Data preprocessing (encoding, normalization)
- Recommendation algorithms
- Image similarity pipeline (CLIP + FAISS)
- Backend API integration (FastAPI)

---

## 🛠 Tech Stack

- Python
- FastAPI
- Scikit-learn
- Pandas / NumPy
- CLIP (OpenAI)
- FAISS

---

## 📡 API Endpoints

### Image Search
POST /search/image  
Upload image → returns similar furniture

### Text Search
POST /search/text  
Input query → returns recommendations

### Matchmaking
POST /match  
Input: style, budget → returns designers

---

## 🎓 Education

Bachelor’s Degree in Computers and Information Technology  
Alexandria University & Egyptian E-Learning University  
Graduation: 2025  
Graduation Project: Excellent

---

## ⚡ Future Improvements
- Real dataset integration
- UI frontend connection
- Deployment on cloud (AWS / GCP)
- User feedback learning loop

- ## 🔍 Example Output

Input:
{
  "style": "modern",
  "budget": "medium"
}

Output:
{
  "matched_designers": [
    {"name": "Designer A"},
    {"name": "Designer B"}
  ]
}
