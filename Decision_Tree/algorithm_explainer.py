import urllib.request
import os
import json

# GitHub raw file URL for the notebook
GITHUB_NOTEBOOK_URL = "https://raw.githubusercontent.com/rakeshravikumar-ML/ml_algorithm_helper/main/Decision_Tree/Decision_Tree_Explanation.ipynb"

def download_notebook():
    """
    Downloads the notebook from GitHub if it is not already available in Colab.
    """
    notebook_path = "/content/Decision_Tree_Explanation.ipynb"

    if not os.path.exists(notebook_path):
        print("\nDownloading notebook from GitHub...")
        urllib.request.urlretrieve(GITHUB_NOTEBOOK_URL, notebook_path)
        print("Download complete!")

    return notebook_path

def get_project_steps():
    """
    Returns a dictionary of model development steps.
    """
    return {
        1: "# Step 1: Importing Required Libraries",
        2: "# Step 2: Loading the Dataset",
        3: "# Step 3: Exploratory Data Analysis (EDA) - Overview",
        4: "# Step 4: Checking for Missing Values",
        5: "# Step 5: Handling Categorical Variables",
        6: "# Step 6: Splitting Data into Training & Testing Sets",
        7: "# Step 7: Feature Scaling & Normalization",
        8: "# Step 8: Visualizing Feature Distributions",
        9: "# Step 9: Correlation Analysis & Multicollinearity Check",
        10: "# Step 10: Feature Engineering - Creating New Features",
        11: "# Step 11: Feature Selection - Removing Redundant Features",
        12: "# Step 12: Handling Class Imbalance - SMOTE & Undersampling",
        13: "# Step 13: Training a Basic Random Forest Model",
        14: "# Step 14: Evaluating Model Performance - Confusion Matrix & Classification Report",
        15: "# Step 15: Evaluating Model Performance - Precision-Recall & AUC-ROC",
        16: "# Step 16: Feature Importance Analysis - SHAP & Permutation Importance",
        17: "# Step 17: Hyperparameter Tuning - GridSearchCV",
        18: "# Step 18: Hyperparameter Tuning - RandomizedSearchCV",
        19: "# Step 19: Hyperparameter Tuning - Bayesian Optimization",
        20: "# Step 20: Comparison of Random Forest with Other Models",
        21: "# Step 21: Evaluating Overfitting & Underfitting",
        22: "# Step 22: Cross-Validation - k-Fold & Stratified k-Fold",
        23: "# Step 23: Advanced Model Explainability - SHAP Deep Dive",
        24: "# Step 24: Feature Removal Analysis - Impact on Model Performance",
        25: "# Step 25: Improving Model Generalization - Regularization Techniques",
        26: "# Step 26: Optimizing Random Forest - Reducing Memory & Computation",
        27: "# Step 27: Deploying the Model - Saving & Loading",
        28: "# Step 28: Building a Model API with FastAPI",
        29: "# Step 29: Serving Predictions with Flask & Docker",
        30: "# Step 30: Model Performance Monitoring & Retraining",
        31: "# Step 31: Handling Concept Drift in Production",
        32: "# Step 32: Logging & Version Control for ML Models",
        33: "# Step 33: Creating an End-to-End ML Pipeline",
        34: "# Step 34: Integrating the Model into a Web Application",
        35: "# Step 35: Handling Real-Time Data with Streaming Pipelines",
        36: "# Step 36: Automated Model Retraining & Deployment",
        37: "# Step 37: Exploring Alternative Ensemble Techniques",
        38: "# Step 38: Building a Gradient Boosted Tree Model",
        39: "# Step 39: Comparing Random Forest with XGBoost & LightGBM",
        40: "# Step 40: Building an Explainable AI System",
        41: "# Step 41: Final Thoughts & Next Steps in Model Optimization",
        42: "# Step 42: Additional Advanced Step 1",
        43: "# Step 43: Additional Advanced Step 2",
    }

def show_project_steps():
    """
    Displays the available model development steps.
    """
    steps = get_project_steps()
    print("\nDevelopment Steps:")
    for step, description in steps.items():
        print(f"{step}. {description[3:]}")  # Remove "## " from display

def get_user_step_choice():
    """
    Asks the user for a step number.
    """
    step_choice = int(input("\nWhich step do you need help with? Enter the step number: "))
    return step_choice

from IPython.display import display, HTML

from IPython.display import Markdown, display

def explain_step(step_choice):
    """
    Fetches and displays the explanation from the notebook for the selected step in Markdown format.
    """
    file_path = download_notebook()
    if not file_path:
        return
    
    step_headers = get_project_steps()
    selected_heading = step_headers.get(step_choice, None)

    if not selected_heading:
        print("Invalid step number. Try again.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        notebook_data = json.load(f)

    found_heading = False
    extracted_explanation = []

    for cell in notebook_data["cells"]:
        if cell["cell_type"] == "markdown":
            markdown_text = "".join(cell["source"]).strip()

            if selected_heading in markdown_text:
                found_heading = True
                extracted_explanation.append(markdown_text)  # Include the header cell itself
                continue
            elif found_heading and markdown_text.startswith("## Step"):  # Stop at the next step heading
                break
            elif found_heading:
                extracted_explanation.append(markdown_text)  # Collect all markdown content

    if extracted_explanation:
        markdown_output = f"### {selected_heading[3:]}\n\n" + "\n\n".join(extracted_explanation)
        display(Markdown(markdown_output))  # ✅ Display as Markdown
    else:
        display(Markdown("⚠️ **No detailed explanation found in the notebook.** Check the markdown formatting."))

def show_code_for_step(step_choice):
    """
    Fetches and displays only the relevant code blocks for the selected step.
    """
    file_path = download_notebook()
    if not file_path:
        return

    step_headers = get_project_steps()
    selected_heading = step_headers.get(step_choice, None)

    if not selected_heading:
        print("Invalid step number. Try again.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        notebook_data = json.load(f)

    found_heading = False
    code_snippets = []

    for cell in notebook_data["cells"]:
        if cell["cell_type"] == "markdown":
            markdown_text = "".join(cell["source"]).strip()
            
            if markdown_text.startswith(selected_heading):
                found_heading = True  # Start collecting code
                continue
            elif found_heading and markdown_text.startswith("## Step"):  # Stop at the next step heading
                break
        elif cell["cell_type"] == "code" and found_heading:
            code_snippets.append("\n".join(cell["source"]))  # Collect all code blocks in the section

    print(f"\nCode for Step {step_choice} ({selected_heading[3:]}):\n")
    if code_snippets:
        print("\n\n".join(code_snippets))
    else:
        print(f"No relevant code found for step {step_choice}. Check your notebook's structure.")
