import urllib.request
import os
import json

# GitHub raw file URL for the notebook
GITHUB_NOTEBOOK_URL = "https://raw.githubusercontent.com/rakeshravikumar-ML/ml_algorithm_helper/main/Correlation/Correlation.ipynb"

def download_notebook():
    """
    Downloads the notebook from GitHub if it is not already available in Colab.
    """
    notebook_path = "/content/Correlation.ipynb"

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
        1: "Step 1: Import Required Libraries",
        2: "Step 2: Load the Dataset",
        3: "Step 3: Explore Data",
        4: "Step 4: Handling Missing Values",
        5: "Step 5: Visualizing Correlations using Scatterplots",
        6: "Step 6: Computing Pearson Correlation",
        7: "Step 7: Correlation Heatmap",
        8: "Step 8: Additional Correlation Methods (Spearman & Kendall)",
        9: "Step 9: Hypothesis Testing for Correlation",
        10: "Step 10: Checking Multicollinearity with Variance Inflation Factor (VIF)",
        11: "Step 11: Outlier Detection & Its Effect on Correlation",
        12: "Step 12: Computing Correlation Before & After Removing Outliers",
        13: "Step 13: Partial Correlation - Controlling for Other Variables",
        14: "Step 14: Feature Selection Based on Correlation",
        15: "Step 15: Correlation with Categorical Variables",
        16: "Step 16: Cross-Correlation for Time-Series Data",
        17: "Step 17: Rank Transformation for Robust Correlation",
        18: "Step 18: Non-Parametric Bootstrap for Correlation Confidence Intervals"
    }

def show_project_steps():
    """
    Displays the available model development steps.
    """
    steps = get_project_steps()
    print("\nModel Development Steps:")
    for step, description in steps.items():
        print(f"{step}. {description}")

def get_user_step_choice():
    """
    Asks the user for a step number.
    """
    step_choice = int(input("\nWhich step do you need help with? Enter the step number: "))
    return step_choice

def explain_step(step_choice):
    """
    Fetches and displays the explanation from both the predefined text and the notebook.
    """
    file_path = download_notebook()
    if not file_path:
        return
    
    explanations = {
        1: "This step involves importing necessary Python libraries like pandas, NumPy, seaborn, and matplotlib.",
        2: "The dataset is loaded using pandas or TensorFlow Datasets and inspected using .head() and .info() functions.",
        3: "This step explores dataset statistics, distributions, and class imbalances.",
        4: "Missing values are identified and handled using methods like imputation or deletion.",
        5: "Scatterplots are used to visualize relationships between numerical variables.",
        6: "Pearson correlation is computed to measure the linear relationship between variables.",
        7: "A heatmap is plotted to show correlation values between all numerical features.",
        8: "Spearman and Kendall correlation methods are explored for non-linear relationships.",
        9: "Hypothesis testing is performed to check if correlation coefficients are statistically significant.",
        10: "Variance Inflation Factor (VIF) is used to check for multicollinearity between predictors.",
        11: "Outliers are detected using boxplots and their effect on correlation is analyzed.",
        12: "Correlation is computed before and after removing outliers to observe its impact.",
        13: "Partial correlation is computed to measure relationships while controlling for other variables.",
        14: "Highly correlated features are identified and removed to avoid redundancy in models.",
        15: "Correlation between categorical and numerical variables is examined using ANOVA and Chi-square tests.",
        16: "Cross-correlation for time-series data is explored to find lag relationships between variables.",
        17: "Rank transformation is applied to make correlation analysis more robust to outliers.",
        18: "Bootstrap methods are used to compute confidence intervals for correlation coefficients."
    }

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
            markdown_text = "".join(cell["source"])
            if selected_heading in markdown_text:
                found_heading = True  # Start collecting markdown cells
            elif found_heading and markdown_text.startswith("# "):  # Stop at the next section
                break
            elif found_heading:
                extracted_explanation.append(markdown_text)

    print(f"\nStep Explanation: {selected_heading}\n")
    print(explanations.get(step_choice, "No predefined explanation available."))
    
    if extracted_explanation:
        print("\nAdditional Explanation from Notebook:")
        print("\n".join(extracted_explanation))

def show_code_for_step(step_choice):
    """
    Fetches and displays all relevant code blocks for the selected step.
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
            markdown_text = "".join(cell["source"])
            if selected_heading in markdown_text:
                found_heading = True  # Start collecting code
            elif found_heading and markdown_text.startswith("# "):  # Stop at the next section
                break
        elif cell["cell_type"] == "code" and found_heading:
            code_snippets.append("\n".join(cell["source"]))  # Collect all code blocks in the section

    if code_snippets:
        print(f"\nCode for Step {step_choice} ({selected_heading}):\n")
        print("\n\n".join(code_snippets))  # Show all code blocks
    else:
        print(f"\n❌ No relevant code found for step {step_choice}. Check your notebook's structure.")
