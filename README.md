# Campus-Sustainability-Twin-AI
Campus Sustainability Twin AI is an intelligent platform developed using Python, Flask, and IBM Granite that automates complaint analysis, categorizes sustainability issues, detects priorities, provides AI-powered chatbot assistance, and helps institutions optimize campus resource management.
# 🌱 Campus Sustainability Twin AI
### AI-Powered Intelligent Complaint Analysis and Resource Management System

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![IBM Granite](https://img.shields.io/badge/IBM-Granite-purple)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Overview

Campus Sustainability Twin AI is an intelligent web-based platform designed to improve the management of sustainability-related issues within educational institutions. The system leverages Artificial Intelligence to automatically analyze complaints submitted by students, faculty, and staff, classify them into relevant categories, determine their priority level, and provide instant assistance through an AI-powered chatbot.

Traditional complaint management systems often require manual review, which can delay responses and reduce operational efficiency. This project addresses those challenges by integrating AI-driven complaint classification, intelligent prioritization, analytics dashboards, and conversational assistance into a single platform.

Developed as part of the **IBM AI for Sustainability Internship**, this project demonstrates how AI can support smarter campus administration and contribute to sustainable resource management.

---

# 🎯 Problem Statement

Educational institutions receive numerous complaints every day regarding issues such as:

- 💧 Water leakage
- 💡 Electricity failures
- 🗑 Waste management
- 🚍 Transportation
- 🏢 Infrastructure maintenance
- 🌱 Sustainability concerns

Manual handling of these complaints often results in:

- Slow response time
- Improper prioritization
- Human errors
- Poor resource allocation
- Lack of centralized monitoring

The objective of this project is to automate complaint analysis using Artificial Intelligence, enabling faster decision-making and improved campus sustainability.

---

# 💡 Proposed Solution

Campus Sustainability Twin AI introduces an intelligent complaint management ecosystem where AI performs the initial analysis of each complaint.

The system:

- Accepts complaint submissions through a web interface
- Uses IBM Granite AI to understand complaint text
- Automatically categorizes complaints
- Predicts priority levels
- Stores complaint information securely
- Generates dashboard analytics
- Assists users through an AI chatbot
- Supports better resource allocation for campus authorities

---

# ✨ Key Features

## 🤖 AI Complaint Classification

Automatically analyzes complaint descriptions using IBM Granite and classifies them into predefined sustainability categories.

---

## 🚨 Intelligent Priority Detection

Identifies complaint urgency based on keywords, context, and issue severity.

Priority Levels:

- 🔴 High
- 🟠 Medium
- 🟢 Low

---

## 💬 AI Chatbot

Provides intelligent responses to user queries regarding campus sustainability issues and complaint management.

---

## 📊 Interactive Dashboard

Visualizes complaint statistics including:

- Total complaints
- Category-wise distribution
- Priority analysis
- Complaint trends
- Resource insights

---

## 🗄 Database Management

Stores complaint records efficiently using SQLite.

---

## 📈 Sustainability Analytics

Helps administrators identify recurring issues and make informed decisions for campus improvement.

---

# 🏗 System Architecture

```
User
   │
   ▼
Flask Web Application
   │
   ├───────────────┐
   │               │
Complaint Module   AI Chatbot
   │               │
IBM Granite API    │
   │               │
Priority Detection │
   │               │
SQLite Database
   │
Dashboard Analytics
   │
Campus Administrator
```

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend Development |
| Flask | Web Framework |
| HTML5 | User Interface |
| CSS3 | Styling |
| JavaScript | Frontend Interactivity |
| SQLite | Database |
| IBM Granite | AI Complaint Analysis |
| ChromaDB | AI Knowledge Retrieval |
| Pandas | Data Processing |

---

# 📂 Project Structure

```
Campus-Sustainability-Twin-AI
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── modules
│   ├── chatbot.py
│   ├── granite_classifier.py
│   ├── priority_detector.py
│   ├── dashboard_data.py
│   └── database.py
│
├── templates
│
├── static
│
├── data
│   └── Campus_Sustainability_Twin_AI_500_Row_Dataset.csv
│
└── documentation
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/campus-sustainability-twin-ai.git
```

## Navigate into Project

```bash
cd campus-sustainability-twin-ai
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file from `.env.example` and add your IBM Granite API credentials.

---

## Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 📊 Dataset

The project uses a custom sustainability complaint dataset containing approximately **500 complaint records** related to campus infrastructure and environmental issues.

Sample categories include:

- Water Supply
- Electricity
- Waste Management
- Transportation
- Infrastructure
- Maintenance
- Sanitation

---

# 🔄 Workflow

1. User submits a complaint.
2. Complaint text is sent to IBM Granite.
3. AI classifies the complaint.
4. Priority detector assigns urgency.
5. Complaint is stored in SQLite.
6. Dashboard updates automatically.
7. Administrator reviews analytics.
8. AI chatbot assists users with information.

---

# 🚀 Future Enhancements

- Email notifications
- SMS alerts
- Mobile application
- Real-time complaint tracking
- GIS-based issue mapping
- Predictive maintenance using Machine Learning
- Multi-language support
- Cloud deployment
- Role-based authentication
- Advanced analytics dashboard

---

# 🎓 Learning Outcomes

This project helped me gain practical experience in:

- Artificial Intelligence integration
- IBM Granite Foundation Models
- Flask web development
- Database management
- Prompt engineering
- Dashboard development
- Full-stack application development
- Sustainable
