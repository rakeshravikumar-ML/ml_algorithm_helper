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
        1: "Introduction",
        2: "Get Helper Functions",
        3: "Using TensorFlow Datasets to download data",
        4: "Explore Data",
        5: "Plot an image from TensorFlow Datasets",
        6: "Creating preprocessing function for data",
        7: "Batching & preparing datasets for modelling (making datasets run fast)",
        8: "Creating modelling callbacks",
        9: "Setting up mixed precision training",
        10: "Building a feature extraction model",
        11: "Checking layer dtype policies (are we using mixed precision?)",
        12: "Fit the feature extraction model",
        13: "Load and evaluate checkpoint weights",
        14: "Save the whole model to file",
        15: "Preparing our model's layers for fine-tuning",
        16: "A couple more callbacks",
        17: "Download fine-tuned model from Google Storage",
        18: "Fine-tuning the feature extraction model",
        19: "Viewing training results on TensorBoard"
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
    Provides an explanation of the selected model development step.
    """
    explanations = {
        1: "Introduction to the project, explaining objectives, dataset details, and expected outcomes.",
        2: "Helper functions are loaded to speed up data preprocessing, training, and evaluation.",
        3: "TensorFlow Datasets is used to load the dataset, providing easy access to preprocessed datasets.",
        4: "Exploring the dataset includes visualizing images, understanding labels, and dataset distribution.",
        5: "An image from TensorFlow Datasets is plotted to verify data loading correctness.",
        6: "Preprocessing functions are created for resizing, normalizing, and augmenting images.",
        7: "Batching is optimized to speed up data loading and reduce memory usage for training.",
        8: "Model callbacks (like early stopping and checkpointing) are set up to improve training efficiency.",
        9: "Mixed precision training is enabled to speed up model training on compatible GPUs.",
        10: "A feature extraction model is built using a pre-trained CNN as the base model.",
        11: "Dtype policies for layers are checked to ensure mixed precision is being used correctly.",
        12: "The feature extraction model is trained using frozen base layers and newly added layers.",
        13: "Checkpoint weights are loaded to continue training from the best checkpoint.",
        14: "The trained model is saved in a format that can be reloaded and used later.",
        15: "Model layers are prepared for fine-tuning by unfreezing specific layers of the pre-trained model.",
        16: "Additional callbacks (such as learning rate scheduling) are added before fine-tuning.",
        17: "The fine-tuned model is downloaded from Google Storage for evaluation.",
        18: "The model undergoes fine-tuning, allowing deeper layers to adjust weights.",
        19: "Training results are visualized using TensorBoard to monitor performance."
    }

    print("\nStep Explanation:")
    print(explanations.get(step_choice, "Invalid step. Please enter a valid number."))

def show_code_for_step(step_choice):
    """
    Fetches and displays relevant code from the notebook based on single `#` markdown headings.
    """
    file_path = download_notebook()  # Ensure the notebook is available
    if not file_path:
        return

    # ✅ Updated search patterns based on `# Header`
    step_code = {
        1: "# Introduction",
        2: "# Get Helper Functions",
        3: "# Using TensorFlow Datasets to download data",
        4: "# Explore Data",
        5: "# Plot an image from TensorFlow Datasets",
        6: "# Creating preprocessing function for data",
        7: "# Batching & preparing datasets for modelling",
        8: "# Creating modelling callbacks",
        9: "# Setting up mixed precision training",
        10: "# Building a feature extraction model",
        11: "# Checking layer dtype policies",
        12: "# Fit the feature extraction model",
        13: "# Load and evaluate checkpoint weights",
        14: "# Save the whole model to file",
        15: "# Preparing our model's layers for fine-tuning",
        16: "# A couple more callbacks",
        17: "# Download fine-tuned model from Google Storage",
        18: "# Fine-tuning the feature extraction model",
        19: "# Viewing training results on TensorBoard"
    }

    selected_heading = step_code.get(step_choice, None)
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
            if selected_heading.lower() in markdown_text.lower():  # Case-insensitive match
                found_heading = True  # Start collecting code after this markdown cell
        elif cell["cell_type"] == "code" and found_heading:
            code_snippets.append("".join(cell["source"]))  # Collect the next code cell(s)
            break  # Stop after the first code cell following the heading

    if code_snippets:
        print(f"\nCode for Step {step_choice} ({selected_heading}):\n")
        print(code_snippets[0])  # Show the first matching code block
    else:
        print(f"\n❌ No relevant code found for step {step_choice}. Check your notebook's structure.")
