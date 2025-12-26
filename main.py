import os
import json
import sys
import requests
from dotenv import load_dotenv

load_dotenv()

# =========================
# GEMINI CONFIG
# =========================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY not found in environment variables")

GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    f"gemma-3-1b-it:generateContent?key={GEMINI_API_KEY}"
)

HEADERS = {
    "Content-Type": "application/json"
}

# =========================
# CLI MENU
# =========================
def show_menu():
    print("\n===== COST OPTIMIZER CLI =====")
    print("1. Enter new project description")
    print("2. Run Complete Cost Analysis")
    print("3. View Recommendations")
    # print("4. Export Report")
    print("4. Exit")


# =========================
# PROJECT DESCRIPTION FLOW
# =========================
def enter_project_description():
    print("\n--- Enter Project Description ---")
    project_description = input("> ").strip()

    if not project_description:
        print("❌ Project description cannot be empty.")
        return

    # 1️⃣ Save raw description
    with open("project_description.txt", "w", encoding="utf-8") as f:
        f.write(project_description)

    print("✔ project_description.txt saved")

    # 2️⃣ Strict JSON extraction prompt
    prompt = f"""
Return ONLY valid JSON.
Do not include explanations, markdown, or comments.

Generate JSON in EXACTLY this format:

{{
  "name": "",
  "budget_inr_per_month": 0,
  "description": "",
  "tech_stack": {{
    "frontend": "",
    "backend": "",
    "database": "",
    "proxy": "",
    "hosting": ""
  }},
  "non_functional_requirements": []
}}


Project Description:
{project_description}
"""

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    print("⏳ Calling Gemini API...")

    try:
        response = requests.post(
            GEMINI_URL,
            headers=HEADERS,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("❌ Gemini API request failed:", e)
        return

    # 3️⃣ Extract text output
    try:
        text_output = response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        print("❌ Unexpected Gemini response format")
        return

    # 4️⃣ Extract JSON safely
    try:
        start = text_output.index("{")
        end = text_output.rindex("}") + 1
        project_profile = json.loads(text_output[start:end])
    except (ValueError, json.JSONDecodeError):
        print("❌ Failed to parse JSON from Gemini output")
        print(text_output)
        return

    # 5️⃣ Save structured profile
    with open("project_profile.json", "w", encoding="utf-8") as f:
        json.dump(project_profile, f, indent=4)

    print("✔ project_profile.json generated successfully")
    print(json.dumps(project_profile, indent=4))


# =========================
# PLACEHOLDERS
# =========================
# def run_cost_analysis():
    # print("⚠️ Cost analysis not implemented yet")

# cost analysis
def run_cost_analysis():
    print("\n--- Running Cost Analysis ---")

    # 1️⃣ Load project profile
    try:
        with open("project_profile.json", "r", encoding="utf-8") as f:
            project_profile = json.load(f)
    except FileNotFoundError:
        print("❌ project_profile.json not found. Run option 1 first.")
        return

    # 2️⃣ Build billing generation prompt
    prompt = f"""
You are a cloud cost simulation system.

Generate 12 to 14 realistic synthetic cloud billing records
based on the project profile below.

Rules:
- Output ONLY valid JSON
- Output must be a JSON array (list of objects)
- Cloud-agnostic (do NOT mention AWS, Azure, or GCP explicitly)
- Costs should roughly respect the monthly budget
- Use realistic services: compute, database, storage, bandwidth, load balancer
- Regions should look realistic (ap-south-1, us-east-1, eu-west-1)
- Months should span across multiple months
- All costs must be in INR

Each record MUST strictly follow this format:

{{
  "month": "YYYY-MM",
  "service": "EC2",
  "resource_id": "i-example-01",
  "region": "ap-south-1",
  "usage_type": "Linux/UNIX (on-demand)",
  "usage_quantity": 720,
  "unit": "hours",
  "cost_inr": 900,
  "desc": "Short description"
}}

Project Profile:
{json.dumps(project_profile, indent=2)}
"""

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    print("⏳ Generating synthetic billing data...")

    # 3️⃣ Call Gemini API
    try:
        response = requests.post(
            GEMINI_URL,
            headers=HEADERS,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("❌ Gemini API request failed:", e)
        return

    # 4️⃣ Extract model output
    try:
        text_output = response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        print("❌ Unexpected Gemini response format")
        return

    # 5️⃣ Parse JSON safely
    try:
        start = text_output.index("[")
        end = text_output.rindex("]") + 1
        billing_data = json.loads(text_output[start:end])
    except (ValueError, json.JSONDecodeError):
        print("❌ Failed to parse billing JSON")
        print(text_output)
        return

    # 6️⃣ Save billing output
    with open("mock_billing.json", "w", encoding="utf-8") as f:
        json.dump(billing_data, f, indent=2)

    print("✔ mock_billing.json generated successfully")
    print(f"✔ Total records generated: {len(billing_data)}")



# def view_recommendations():
#     print("⚠️ Recommendations not implemented yet")





def view_recommendations():
    print("\n--- Generating Cost Optimization Report ---")

    # 1️⃣ Load inputs
    try:
        with open("project_profile.json", "r", encoding="utf-8") as f:
            project_profile = json.load(f)

        with open("mock_billing.json", "r", encoding="utf-8") as f:
            billing_data = json.load(f)

    except FileNotFoundError as e:
        print(f"❌ Missing file: {e.filename}")
        return

    # 2️⃣ Compute service-wise costs
    service_costs = {}
    total_cost = 0

    for entry in billing_data:
        service = entry.get("service", "Unknown")
        cost = entry.get("cost_inr", 0)

        service_costs[service] = service_costs.get(service, 0) + cost
        total_cost += cost

    budget = project_profile.get("budget_inr_per_month", 0)
    budget_variance = total_cost - budget
    is_over_budget = budget_variance > 0

    avg_service_cost = total_cost / max(len(service_costs), 1)
    high_cost_services = {
        s: c for s, c in service_costs.items() if c >= avg_service_cost
    }

    # 3️⃣ Build structured recommendation prompt
    prompt = f"""
You are a cloud cost optimization expert.

Generate 6 to 8 cost optimization recommendations as JSON OBJECTS.

Rules:
- Output ONLY valid JSON
- Output must be a JSON array of objects
- Each recommendation MUST follow EXACTLY this schema:

{{
  "title": "",
  "service": "",
  "current_cost": 0,
  "potential_savings": 0,
  "recommendation_type": "open_source | free_tier | right_sizing | optimization | alternative_provider | network_optimization",
  "description": "",
  "implementation_effort": "low | medium | high",
  "risk_level": "low | medium | high",
  "steps": ["", "", ""],
  "cloud_providers": ["AWS", "Azure", "GCP"]
}}

Guidelines:
- Recommendations MUST be multi-cloud
- Include open-source and free-tier suggestions where applicable
- Focus more on high-cost services
- Savings must be realistic (do not exceed current cost)
- No markdown, no explanations, no extra text

Project Profile:
{json.dumps(project_profile, indent=2)}

Billing Summary:
Total Cost: {total_cost}
Service Costs:
{json.dumps(service_costs, indent=2)}
"""

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    print("⏳ Generating recommendations...")

    try:
        response = requests.post(
            GEMINI_URL,
            headers=HEADERS,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("❌ Gemini API error:", e)
        return

    # 4️⃣ Extract Gemini output
    try:
        text_output = response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        print("❌ Unexpected Gemini response format")
        return

    # 5️⃣ Parse recommendation JSON
    try:
        start = text_output.index("[")
        end = text_output.rindex("]") + 1
        recommendations = json.loads(text_output[start:end])
    except (ValueError, json.JSONDecodeError):
        print("❌ Failed to parse recommendation JSON")
        print(text_output)
        return

    # 6️⃣ Compute summary
    total_potential_savings = sum(
        r.get("potential_savings", 0) for r in recommendations
    )

    savings_percentage = (
        (total_potential_savings / total_cost) * 100
        if total_cost > 0 else 0
    )

    high_impact_recommendations = sum(
        1 for r in recommendations
        if r.get("potential_savings", 0) >= avg_service_cost * 0.5
    )

    summary = {
        "total_potential_savings": total_potential_savings,
        "savings_percentage": round(savings_percentage, 2),
        "recommendations_count": len(recommendations),
        "high_impact_recommendations": high_impact_recommendations
    }

    # 7️⃣ Build final report
    report = {
        "project_name": project_profile.get("name", "Unknown Project"),
        "analysis": {
            "total_monthly_cost": total_cost,
            "budget": budget,
            "budget_variance": budget_variance,
            "is_over_budget": is_over_budget,
            "service_costs": service_costs,
            "high_cost_services": high_cost_services
        },
        "recommendations": recommendations,
        "summary": summary
    }

    # 8️⃣ Save output
    with open("cost_optimization_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("✔ cost_optimization_report.json generated successfully")
    print(json.dumps(report, indent=2))



def export_report():
    print("⚠️ Export not implemented yet")


# =========================
# MAIN LOOP
# =========================
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            enter_project_description()
        elif choice == "2":
            run_cost_analysis()
        elif choice == "3":
            view_recommendations()
        # elif choice == "4":
        #     export_report()
        elif choice == "4":
            print("👋 Exiting...")
            sys.exit(0)
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
