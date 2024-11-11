---
title: Interview Question Generator Using Gemini & LangChain
emoji: 😒
colorFrom: blue
colorTo: red
sdk: streamlit
app_file: app.py
pinned: false
---

## GeminiMinds
This project is a dynamic Interview Question Generator that leverages Google's Gemini model and LangChain to generate intelligent and diverse interview questions. Designed to streamline the process of question generation, this tool is especially useful for recruiters, educators, and interview preparers.

### Project Overview
The Interview Question Generator is designed to produce tailored interview questions based on specific topics or keywords. Utilizing Gemini for natural language understanding and LangChain to structure coherent queries, this generator outputs a diverse range of questions suited to technical, behavioral, and situational interview scenarios.

This project is deployed on Hugging Face Spaces with continuous integration set up using GitHub Actions for seamless deployment.

### Features
* **Natural Language Understanding**: Uses Gemini for processing context and generating relevant questions.
* **Customizable Topics**: Generates questions based on any input topic or keyword.
* **Types of Questions**: Supports various question types such as technical, behavioral, and situational.
* **Real-time Deployment**: Deployed on Hugging Face Spaces for easy access.
* **Automated Deployment**: Configured with GitHub Actions for CI/CD.

### Directory Structure
* **assets/**: Contains images, icons, or other media used in the project.
* **data/**: Holds data files or examples used in testing.
* **research/**: Notes or research-related documentation.
* **app.py**: Main application file, handling the question generation logic.
* **requirements.txt**: Lists the dependencies required for the project.
* **.github/workflows/**: Contains GitHub Actions workflow for automated deployment.
* **README.md**: Project documentation.

### Installation
1. Clone the repository:
```
   git clone https://github.com/iUnnati31/Interview-Question-Generator.git
```
2. Navigate to the project directory:
```
cd Interview-Question-Generator
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```

### Usage
1. Run the app locally:
```
python app.py
```
2. Access the deployed version on Hugging Face Spaces at [Hugging Face Link](https://huggingface.co/spaces/unnatiag/GeminiMinds).

### Deployment
This project is set up with GitHub Actions for continuous integration and deployment on Hugging Face Spaces. Any push to the main branch triggers the deployment workflow defined in `.github/workflows/main.yaml`.

### License
This project is licensed under the MIT License.

### Acknowledgments
* LangChain for seamless NLP workflow integration.
* Hugging Face Spaces for hosting and deployment.
* Google Gemini for the natural language generation capabilities.

### Contributor
Unnati Agarwal
