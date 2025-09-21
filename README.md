# AI Agent for Tracking Daily Water and Meal Intake

This project is a multi-agent system designed to help you track your daily water and meal intake. It consists of two agents:

*   **Water Intake Agent**: Provides feedback on your daily water consumption.
*   **Meal Tracker Agent**: Offers insights into your meals and calorie intake.

The application is built with Python, Streamlit, and LangChain.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a Conda environment and activate it:**
    ```bash
    conda create --name water-tracker python=3.9
    conda activate water-tracker
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file** in the root directory and add your Groq API key:
    ```
    GROQ_API_KEY=your-api-key
    ```

## How to Run the App

1.  **Open your terminal** and navigate to the project's root directory.

2.  **Run the Streamlit application:**
    ```bash
    streamlit run dashboard.py
    ```

3.  **Open your web browser** and go to the URL provided by Streamlit (usually `http://localhost:8501`).
