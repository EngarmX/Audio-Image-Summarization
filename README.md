# AI-Powered Audio & Image Summarization System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org)
[![Framework](https://img.shields.io/badge/Framework-Flask-black.svg)](https://flask.palletsprojects.com/)
[![Model](https://img.shields.io/badge/LLM-Gemma--1B--LoRA-orange.svg)](https://huggingface.co/google/gemma-1b)
[![Database](https://img.shields.io/badge/Database-MongoDB-green.svg)](https://www.mongodb.com/)

An enterprise-grade, multi-modal AI pipeline designed to ingest, synchronize, and summarize unstructured audio and visual data. This system integrates Optical Character Recognition (OCR), Speech-to-Text (STT), and a fine-tuned Large Language Model (LLM) into a unified, high-performance web application capable of processing complex, long-form multi-modal inputs.

---

## 🚀 Core Features

* **Multi-Modal Ingestion:** Seamlessly processes text-heavy images and long-form audio files within a unified execution pipeline.
* **Fine-Tuned Summarization:** Powered by a customized **Gemma-1B** model, fine-tuned via Low-Rank Adaptation (LoRA) and 4-bit quantization for lightweight, high-quality dialogue and content summarization.
* **Long-Form Audio Processing:** Outperforms major off-the-shelf tools in specialized multi-modal synchronization tasks, handling complex audio files up to 27 minutes in length.
* **Secure Production Backend:** Robust Flask-based architecture featuring MongoDB authentication, secure session management, and comprehensive error-handling frameworks.

---

## 🛠️ Tech Stack & Architecture

### AI & Machine Learning
* **LLM Base:** Google Gemma-1B
* **Optimization:** LoRA (Low-Rank Adaptation), 4-bit Quantization (BitsAndBytes)
* **Multi-Modal Frameworks:** OCR Engines & Speech-to-Text APIs

### Backend & Database
* **Server Framework:** Python, Flask
* **Database:** MongoDB (User Authentication & Session State Management)
* **Design Principles:** Object-Oriented Programming (OOP), Robust Error Handling

---

## 📐 System Workflow

The architecture bridges data extraction and language generation to deliver rapid, accurate summaries:

1. **Data Ingestion:** User uploads an audio file (MP3/WAV) or image document through the web UI.
2. **Feature Extraction:**
   * **Audio Path:** Processed via an optimized Speech-to-Text engine to extract a raw text transcript.
   * **Image Path:** Processed via high-precision OCR to capture embedded textual data.
3. **Synchronization & Assembly:** Extracted text data is normalized, structured, and passed into a specialized prompt context window.
4. **LLM Inference:** The Quantized Gemma-1B (LoRA) model generates a concise, context-aware abstractive summary.
5. **Secure Delivery:** The backend validates user permissions via MongoDB, logs the session, and serves the payload securely to the frontend.

---

## 📦 Installation & Setup

### Prerequisites
* Python 3.10 or higher
* MongoDB instance (Local or Atlas)
* CUDA-compatible GPU (Highly recommended for LLM/LoRA inference)

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/audio-image-summarizer.git](https://github.com/yourusername/audio-image-summarizer.git)
cd audio-image-summarizer
