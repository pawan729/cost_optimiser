# 📦 Cost Optimiser

A Python CLI tool that simulates cloud cost estimation and optimization reports using structured project profiles and billing data.

This project takes a **project description**, generates a **profile JSON**, runs a **synthetic billing model**, and outputs a **cost optimization report** — helping teams estimate and optimize infrastructure costs. Ideal for demos, learning, and cost analysis workflows.

---

## 📍 Table of Contents

- [About the Project](#about-the-project)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Repository Structure](#repository-structure)  
- [Usage](#usage)  
- [Example Files](#example-files)  
- [How It Works](#how-it-works)  
- [LLM Model Recommendation](#llm-model-recommendation)  
- [Future Enhancements](#future-enhancements)  
- [License](#license)

---

## 🧠 About the Project

Cost Optimiser is designed to simulate the **cloud cost planning lifecycle**: from receiving a project description to generating a structured project profile, producing mock billing data, and suggesting cost optimization recommendations.

The example in this repo is based on a **food delivery app** with a ₹50,000/month budget and basic monitoring requirements.

---

## 🚀 Features

- Takes a *project description* as input  
- Generates a structured *project profile JSON*  
- Runs a mock *billing simulation*  
- Produces a *cost optimization report*  
- Outputs JSON files for integration and review

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Input/Outputs:** JSON, TXT  
- **CLI:** Terminal-based workflow  
- **LLM Integration:** Generates structured data from descriptions  
(*LLM not hardcoded in the repo — see model recommendation below*)

---

## 📁 Repository Structure

/
├── .gitignore
├── main.py
├── mock_billing.json
├── project_description.txt
├── project_profile.json
├── cost_optimization_report.json
└── README.md


---

## 💻 Usage

1. Clone the repository  
   ```bash
   git clone https://github.com/pawan729/cost_optimiser.git
   cd cost_optimiser

2.Ensure Python is installed (Python 3.8+ recommended)
3.Run the main script
   python main.py
4.Follow the CLI instructions to:
    Input new project descriptions
    Generate profiles
    Run cost simulation
    View or export optimization reports

##Example files 
project_description.txt
project_profile.json	
mock_billing.json	
cost_optimization_report.json
    
**How It Works**
1.Input: A text description of a project’s goals, tech stack, and budget.

2.Profile Generation: Structure the input into JSON for consistent analysis.

3.Mock Billing: Estimate costs for compute, storage, database, monitoring, and networking.

4.Optimization Report: Compare costs to budget and suggest savings.

LLM model used -> AI -> gemini and model -> gemma-3-1b-it

**Future Enhancements**
Integrate real cloud billing APIs (AWS / Azure / GCP)
Add support for multiple projects
Build web interface/dashboard
Export reports in PDF/CSV
Add cost forecasting and trends

**License**
MIT License © 2025
Feel free to use, adapt, and improve!

