import streamlit as st
import joblib
import os # Keep os for checking if files exist

# ... (keep the rest of your app.py the same) ...

# ----------------- REPLACE THIS FUNCTION -----------------
# @st.cache_resource
# def load_artifacts():
#     """
#     Loads the saved vectorizer and all trained models from disk
#     using their specific filenames.
#     """
#     # First, check if all required files exist
#     required_files = [
#         'tfidf_vectorizer.pkl',
#         'logistic_regression_model.pkl',
#         'logistic_regression_cv_model.pkl',
#         'decision_tree_model.pkl',
#         'svm_model.pkl',
#         'random_forest_model.pkl',
#         'extra_trees_model.pkl'
#     ]
    
#     for f in required_files:
#         if not os.path.exists(f):
#             # If any file is missing, raise an error to be caught below
#             raise FileNotFoundError(f"Missing required file: '{f}'. Please ensure all models and the vectorizer are saved from your notebook and are in the same folder as app.py.")

#     # Load the vectorizer
#     vectorizer = joblib.load('tfidf_vectorizer.pkl')
    
#     # Define the models and their user-friendly names
#     models_to_load = {
#         "Logistic Regression": 'logistic_regression_model.pkl',
#         "Logistic Regression (CV)": 'logistic_regression_cv_model.pkl',
#         "Decision Tree": 'decision_tree_model.pkl',
#         "Support Vector Machine": 'svm_model.pkl',
#         "Random Forest": 'random_forest_model.pkl',
#         "Extra Trees": 'extra_trees_model.pkl'
#     }
    
#     # Load each model
#     loaded_models = {}
#     for name, filename in models_to_load.items():
#         loaded_models[name] = joblib.load(filename)
        
#     return vectorizer, loaded_models
# # ----------------- END OF REPLACEMENT -----------------
@st.cache_resource
def load_artifacts():
    """
    Loads the saved vectorizer and all trained models from disk
    using their specific filenames. Works both locally and on Render.
    """
    base_path = os.path.dirname(os.path.abspath(__file__))

    # List of required filenames
    required_files = [
        'tfidf_vectorizer.pkl',
        'logistic_regression_model.pkl',
        'logistic_regression_cv_model.pkl',
        'decision_tree_model.pkl',
        'svm_model.pkl',
        'random_forest_model.pkl',
        'extra_trees_model.pkl'
    ]

    # Check existence of all required files
    for filename in required_files:
        file_path = os.path.join(base_path, filename)
        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"Missing required file: '{filename}'. Please ensure all models and the vectorizer are saved "
                f"and are located in the same directory as app.py."
            )

    # Load vectorizer
    vectorizer = joblib.load(os.path.join(base_path, 'tfidf_vectorizer.pkl'))

    # Define models to load
    model_files = {
        "Logistic Regression": 'logistic_regression_model.pkl',
        "Logistic Regression (CV)": 'logistic_regression_cv_model.pkl',
        "Decision Tree": 'decision_tree_model.pkl',
        "Support Vector Machine": 'svm_model.pkl',
        "Random Forest": 'random_forest_model.pkl',
        "Extra Trees": 'extra_trees_model.pkl'
    }

    # Load models
    loaded_models = {
        name: joblib.load(os.path.join(base_path, fname))
        for name, fname in model_files.items()
    }

    return vectorizer, loaded_models


# --- The rest of your app.py stays exactly the same ---
st.title("📧 Spam Mail Prediction using Machine Learning")
st.markdown("""
This application classifies an email as either **Spam** or **Ham** (not spam) using various pre-trained machine learning models.
Paste the content of an email below and select a model to see the classification.
""")

try:
    vectorizer, models = load_artifacts()
    
    st.sidebar.title("Classifier Options")
    model_choice = st.sidebar.selectbox(
        "Choose a classification model:",
        list(models.keys())
    )

    st.header("Classify Your Email")
    email_input = st.text_area(
        "Paste the full email content here:",
        height=250,
        placeholder="Subject: Special Offer! You've won a prize..."
    )

    if st.button("Classify Email", type="primary"):
        if email_input.strip() == "":
            st.warning("Please paste some email text to classify.")
        else:
            selected_model = models[model_choice]
            input_features = vectorizer.transform([email_input])
            prediction = selected_model.predict(input_features)[0]

            st.subheader(f"Prediction using {model_choice} Model:")
            if prediction == 1:
                st.error("🚨 This email is classified as **SPAM**.", icon="🚨")
            else:
                st.success("✅ This email is classified as **HAM** (Not Spam).", icon="✅")

except FileNotFoundError as e:
    st.error(str(e)) # Display the specific error message from the function