# 📦 Cost Optimiser

Cost Optimiser is a **Python-based CLI application** that simulates cloud cost estimation and optimization using **structured project profiles, synthetic billing data, and AI-generated recommendations**.

The tool accepts a project description, converts it into a structured profile, generates mock billing data, and produces a detailed **cost optimization report**. It is ideal for **academic projects, learning cloud cost planning, and demonstrating LLM-driven automation**.

---

## 📍 Table of Contents

- About the Project  
- Key Features  
- Tech Stack  
- Repository Structure  
- Installation & Usage  
- Example Files  
- How It Works  
- LLM Model Usage  
- Future Enhancements  
- License  

---

## 🧠 About the Project

Cost Optimiser simulates the **end-to-end cloud cost planning lifecycle**:

1. Accepting a natural language project description  
2. Converting it into a structured JSON project profile  
3. Generating synthetic billing data  
4. Analyzing costs against a defined budget  
5. Producing optimization recommendations  

The reference use case included in this repository is a **food delivery application** designed for **~10,000 monthly users** with a **₹50,000/month budget**, focusing on scalability, cost efficiency, and uptime monitoring.

---

## 🚀 Key Features

- Menu-driven Command Line Interface  
- Converts plain text descriptions into structured JSON  
- Generates synthetic cloud billing data  
- Produces a cost optimization report  
- Budget variance calculation  
- Clean and reusable JSON outputs  
- Suitable for demos, coursework, and AI-driven tooling projects  

---

## 🛠️ Tech Stack

- Programming Language: Python  
- Interface: CLI (Command Line Interface)  
- Data Formats: JSON, TXT  
- AI Platform: Gemini  
- LLM Model: gemma-3-1b-it  
- Architecture Style: Modular, file-based workflow  

---

## 📁 Repository Structure

```
cost_optimiser/
│
├── .gitignore
├── main.py
├── project_description.txt
├── project_profile.json
├── mock_billing.json
├── cost_optimization_report.json
└── README.md
```

---

## 💻 Installation & Usage

1. Clone the repository  
```bash
git clone https://github.com/pawan729/cost_optimiser.git
cd cost_optimiser
```

2. Ensure Python is installed (Python 3.8 or higher recommended)  
```bash
python --version
```

3. Run the application  
```bash
python main.py
```

4. Follow the CLI menu to:
- Enter a new project description  
- Generate a project profile  
- Run complete cost analysis  
- View optimization recommendations  
- Export reports  

---

## 📄 Example Files

- project_description.txt – Raw project description input  
- project_profile.json – Structured project profile  
- mock_billing.json – Synthetic cloud billing data  
- cost_optimization_report.json – Final cost analysis and recommendations  

---

## 🔍 How It Works

1. Input  
A text description containing project goals, tech stack, and budget.

2. Profile Generation  
The description is transformed into a structured JSON profile for consistent analysis.

3. Synthetic Billing  
Estimated costs are generated for compute, storage, database, monitoring, and networking.

4. Optimization Report  
Total cost is compared with the budget and optimization suggestions are generated.

---

## 🤖 LLM Model Usage

This project uses **Google Gemini AI** for structured data generation.

- Model Used: gemma-3-1b-it  
- Purpose:
  - Project profiling  
  - JSON generation  
  - Synthetic billing creation  
  - Cost optimization recommendations  

The model is instruction-tuned and well-suited for reliable structured outputs.

---

## 📈 Future Enhancements

- Integration with real cloud billing APIs (AWS / Azure / GCP)  
- Multi-project support  
- Cost forecasting and trend analysis  
- Export reports in PDF and CSV formats  
- Web-based dashboard interface  

---

## 📜 License

MIT License © 2025  

You are free to use, modify, and distribute this project for academic, personal, or commercial purposes with attribution.

---

## 👤 Author

Pawan Kumar Yadav  
GitHub: https://github.com/pawan729
