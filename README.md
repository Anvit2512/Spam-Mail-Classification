📧 Spam Email Classification using Machine Learning
<div align="center">
![alt text](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)

![alt text](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)

![alt text](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)

![alt text](https://img.shields.io/badge/License-MIT-green.svg)
</div>
This project implements a Spam Email Classifier using various Supervised Machine Learning algorithms. The application, built with Streamlit, allows users to input any email text and receive a real-time prediction on whether it is Spam (unsolicited junk mail) or Ham (a legitimate email).
✨ Live Demo
Experience the classifier in action without any local setup. Click the link below to access the deployed web application.
🔗 Try the Live App!
🖼️ Screenshots
(Add a screenshot or GIF of the application interface here)
⭐ Features
Real-Time Classification: Instantly predict if an email is Spam or Ham.
Multi-Model Support: Choose from a selection of six different trained machine learning models for prediction.
User-Friendly Interface: A simple and intuitive web interface powered by Streamlit.
TF-IDF Vectorization: Emails are processed and converted into numerical features using the TF-IDF (Term Frequency-Inverse Document Frequency) technique.
Comparative Analysis: Models were trained on different datasets, with notebooks available for reviewing the training process.
🧠 Models Implemented
All models were trained on pre-processed email data vectorized using TF-IDF.
✅ Logistic Regression
✅ Logistic Regression with Cross-Validation
✅ Decision Tree Classifier
✅ Support Vector Machine (SVM)
✅ Random Forest Classifier
✅ Extra Trees Classifier
🚀 How to Run Locally
To run this project on your local machine, follow these steps:
Clone the Repository
Generated bash
git clone https://github.com/Anvit2512/Spam-Mail-Classification.git
cd Spam-Mail-Classification
Use code with caution.
Bash
Install Dependencies
It's recommended to create a virtual environment first.
Generated bash
pip install -r requirements.txt
Use code with caution.
Bash
Run the Streamlit App
Generated bash
streamlit run app.py
Use code with caution.
Bash
The application will open in your default web browser.
📂 Project Structure
Here is an overview of the project's directory structure:
Generated text
Spam-Mail-Classification/
├── app.py              # Main Streamlit application script
├── vectorizer.pkl      # Saved TF-IDF vectorizer
├── model_*.pkl         # Various saved trained ML models
├── requirements.txt    # Project dependencies
├── render.yaml         # Deployment configuration for Render
├── README.md           # Project documentation (this file)
│
├── Spam_Mail_Classification_given_dataset/
│   └── Spam_Mail_Prediction_using_Machine_Learning.ipynb  # Training notebook 1
│
└── spam_mail_classification_method_1_with_deployment/
    └── spam_mail_classification_method_1_with_deployment.ipynb # Training notebook 2
Use code with caution.
Text
Key Files:
app.py: The entry point for the Streamlit web application.
*.pkl: Serialized Python objects, including the trained TF-IDF vectorizer and machine learning models, allowing for fast loading during inference.
requirements.txt: A list of all Python packages required to run the project.
📊 Training & Datasets
The training logic, data preprocessing, and model evaluation are detailed in the Jupyter notebooks located in the project:
Spam_Mail_Classification_given_dataset/: Contains the primary notebook and dataset used for training the final deployed models.
spam_mail_classification_method_1_with_deployment/: Contains an alternative dataset and training workflow, useful for comparative analysis.
🛠️ Tech Stack
Python: Core programming language.
Scikit-learn: For machine learning model implementation, training, and evaluation.
Pandas: For data manipulation and analysis.
NLTK: For natural language processing and text preprocessing.
Joblib: For saving and loading trained models (.pkl files).
Streamlit: For building and deploying the interactive web application.
📜 License
This project is licensed under the MIT License. See the LICENSE file for more details.
👤 Author
Made with ❤️ by Anvit Kumar
<p align="left">
<a href="https://github.com/Anvit2512" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
<a href="https://www.linkedin.com/in/anvit-kumar-52b88b200/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
</p>
⭐ Show Your Support
If you find this project useful or interesting, please consider giving it a ⭐️ star on GitHub