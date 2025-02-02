import urllib.request
import os
import json

# GitHub raw file URL for the notebook
GITHUB_NOTEBOOK_URL = "https://raw.githubusercontent.com/rakeshravikumar-ML/ml_algorithm_helper/main/computer_vision/food_vision_project.ipynb"

def download_notebook():
    """
    Downloads the notebook from GitHub if it is not already available in Colab.
    """
    notebook_path = "/content/food_vision_project.ipynb"

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
        1: "## Step 1: Introduction",
        2: "## Step 2: Get Helper Functions",
        3: "## Step 3: Using TensorFlow Datasets to download data",
        4: "## Step 4: Explore Data",
        5: "## Step 5: Plot an image from TensorFlow Datasets",
        6: "## Step 6: Creating preprocessing function for data",
        7: "## Step 7: Batching & preparing datasets for modelling (making datasets run fast)",
        8: "## Step 8: Step 2: Creating modelling callbacks",
        9: "## Step 9: Setting up mixed precision training",
        10: "## Step 10: Building a feature extraction model",
        11: "## Step 11: Checking layer dtype policies (are we using mixed precision?)",
        12: "## Step 12: Fit the feature extraction model",
        13: "## Step 13: Load and evaluate checkpoint weights",
        14: "## Step 14: Save the whole model to file",
        15: "## Step 15: Preparing our model's layers for fine-tuning",
        16: "## Step 16: A couple more callbacks",
        17: "## Step 17: Download fine-tuned model from Google Storage",
        18: "## Step 18: Viewing training results on TensorBoard"
    }

def show_project_steps():
    """
    Displays the available model development steps.
    """
    steps = get_project_steps()
    print("\nModel Development Steps:")
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
