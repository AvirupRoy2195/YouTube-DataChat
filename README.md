# YouTube Analytics Chat App

This application allows you to chat with the YouTube Analytics dataset using natural language.

## Setup

1.  **Run the setup script:**
    ```powershell
    .\setup.ps1
    ```
    This will create a virtual environment (`.venv`) and install the required dependencies.

2.  **Configure Environment Variables:**
    - Copy `.env.example` to `.env`.
    - Open `.env` and add your OpenAI API Key:
      ```
      OPENAI_API_KEY=your_api_key_here
      ```

## Running the App

Run the application using the Streamlit executable within the virtual environment:

```powershell
.\.venv\Scripts\streamlit run chat_app.py
```
