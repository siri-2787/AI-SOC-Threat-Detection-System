# AI-Powered SOC Threat Detection & Intelligence System

> 🚨 A Smart AI-Driven Cybersecurity Monitoring & Intelligence Platform  
> Detect • Analyze • Score • Simulate • Visualize Cyber Threats in Real-Time

---

## 🚀 Project Overview

**AI-Powered SOC Threat Detection & Intelligence System** is an advanced AI-based cybersecurity solution designed to simulate real-world **Security Operations Center (SOC)** workflows.

👉 The goal is to replicate how modern enterprises monitor and respond to cyber threats using AI.

This system uses **Machine Learning + Security Intelligence Logic** to:

- 🔍 Detect cyber threats in network traffic  
- 🧠 Classify attack types (DoS, Probe, Anomaly, Normal)  
- 📊 Assign Threat Scores (0–100)  
- 🚨 Generate severity levels (Low, Medium, High)  
- 🔴 Simulate real-time cyber attacks  
- 📈 Visualize network behavior using interactive dashboards  

---

## 🎯 Problem Statement

Traditional cybersecurity systems rely on:

- ❌ Static rule-based detection  
- ❌ Limited adaptability  
- ❌ Poor handling of unknown threats  

👉 This project solves it using:

- ✅ Machine Learning (pattern-based detection)  
- ✅ Anomaly-aware logic  
- ✅ SOC-style intelligent scoring system  

---

## 🔥 Key Features (Unique Highlights)

### ⚡ AI Threat Detection Engine
- Random Forest model detects:
  - Normal Traffic  
  - DoS Attacks  
  - Intrusions / Anomalies  

### 🧠 Threat Scoring System (NEW 🔥)
- Generates a **risk score (0–100)** based on:
  - Error rate  
  - Connection count  
  - Traffic volume  
- Helps prioritize threats like real SOC systems  

### 🖥️ Advanced SOC Dashboard
Built using **Streamlit** with:
- Manual threat analysis  
- Bulk CSV forensic audit  
- Interactive visual analytics  

### 🔴 Live Cyber Attack Simulation (NEW 🔥)
- Simulates real-time incoming traffic  
- Continuously analyzes packets  
- Displays dynamic threat detection  

### 📊 Visual Analytics
- 📈 Traffic Distribution (Attack vs Normal)  
- 📊 Severity Level Analysis  
- 📉 Threat Score visualization  

### 🕵️ Investigation Logs
- SOC-style forensic logs including:
  - Attack type  
  - Severity  
  - Threat score  
  - AI reasoning  

---

## 🏗️ System Architecture
Network Traffic Data
↓
Data Preprocessing (Cleaning + Encoding + Scaling)
↓
Machine Learning Model (Random Forest)
↓
Prediction Engine (Flask API)
↓
Security Intelligence Layer
(Severity + Threat Score + Reasoning)
↓
Streamlit Dashboard
(Visualization + Simulation + Logs)


---

## 🧠 How It Works

### 1️⃣ Data Preprocessing
- Removes missing values  
- Encodes categorical features  
- Scales numerical data  

### 2️⃣ Model Prediction
- Random Forest classifier  
- Predicts:
  - ATTACK  
  - NORMAL  

### 3️⃣ Intelligence Layer (🔥 Key Feature)
- Assigns severity (LOW / MEDIUM / HIGH)  
- Detects attack type  
- Generates explanation  
- Computes threat score  

### 4️⃣ Visualization Layer
- Interactive charts using Plotly  
- Real-time simulation support  

---

## 🛠️ Tech Stack

### 🔹 Backend
- Python  
- Flask (REST API)  

### 🔹 Machine Learning
- Scikit-Learn  
- Pandas  
- NumPy  

### 🔹 Frontend
- Streamlit  
- Plotly  

### 🔹 Additional
- Joblib (model persistence)  
- Logging system  

---

## 📂 Project Structure


AI-SOC-Threat-Detection-System/
├── api/ # Flask API
├── dashboard/ # Streamlit UI
├── src/ # ML logic & preprocessing
├── models/ # Trained models
├── data/ # Dataset
├── logs/ # Detection logs
├── images/ # Screenshots
├── main.py # Training pipeline
├── requirements.txt
└── README.md


---




## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/siri-2787/AI-SOC-Threat-Detection-System.git
cd AI-SOC-Threat-Detection-System
````

---

### 2️⃣ Create Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### 🔹 Step 1: Train Model

```bash
python main.py
```

### 🔹 Step 2: Run API

```bash
cd api
python app.py
```

### 🔹 Step 3: Run Dashboard

```bash
cd dashboard
streamlit run app.py
```

---

## 🧪 Sample Output

* 🟢 NORMAL → Safe traffic
* 🚨 ATTACK → Threat detected
* 🔴 HIGH → Critical risk
* 📊 Threat Score → 0–100

---

## 📊 Results

* Accurate detection of:

  * DoS attacks
  * Network probes
  * Normal traffic
* Real-time simulation capability
* SOC-style threat scoring system

---

## 🎯 Learning Outcomes

* Machine Learning in Cybersecurity
* SOC workflow simulation
* API development using Flask
* Dashboard creation using Streamlit
* Threat intelligence system design

---

## 📈 Future Enhancements

* 🔹 Real-time packet capture (Wireshark integration)
* 🔹 Deep Learning (LSTM / Autoencoders)
* 🔹 Cloud deployment (AWS / GCP)
* 🔹 SIEM integration

---

## 👩‍💻 Author

**P Siri Reddy**
CSE Student


