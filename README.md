# Ask Your CSV - Streamlit App

This repository contains a Streamlit web application that allows users to upload a CSV file and make predictions using pre-trained machine learning models. The application provides insights into the model's performance through confusion matrices.

## Getting Started

To run the Streamlit app, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repository
   ```

3. Install the required dependencies. It is recommended to use a virtual environment:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run your_app.py
   ```

   Replace `your_app.py` with the actual name of your Python script containing the Streamlit app code.

## Usage

1. Access the Streamlit app through your web browser.

2. Upload a CSV file by using the provided file uploader.

3. Once the file is uploaded, the application displays the contents of the CSV file in a tabular format.

4. Choose a prediction model by selecting the appropriate option ('2013' or '2023').

5. If a model is available for the selected year, it will be loaded. Otherwise, an error message will be displayed.

6. The application then generates and displays a confusion matrix based on the selected model's predictions.

## Models

The repository includes two pre-trained models:

- **2013 Model:** This model is loaded from the file "rfc_model.pkl".
- **2023 Model:** This model is loaded from the file "rfc_model_23.pkl".

Note: Ensure that the models are available in the same directory as the Streamlit app script.

## Model Features

### For '2013' Model

- Features: 'V1', 'V2', 'V3', ..., 'Amount', 'Hour'
- Target: 'Class'

### For '2023' Model

- Features: 'V1', 'V2', 'V3', ..., 'Amount'
- Target: 'Class'

## Confusion Matrix

The confusion matrix provides the following metrics:

- True Positives
- True Negatives
- False Positives
- False Negatives

These metrics offer insights into the model's performance on the uploaded CSV file.

## Note

If the selected model is not available or there is an error loading the model, the application will prompt you to try again.

Feel free to customize the application and models based on your specific use case.

**Happy predicting!**
