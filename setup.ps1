# Check if .venv exists
if (!(Test-Path .venv)) {
    Write-Host "Creating virtual environment..."
    python -m venv .venv
}

# Activate venv and install requirements
Write-Host "Activating virtual environment and installing requirements..."
& .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

Write-Host "Setup complete. To run the app:"
Write-Host "1. Copy .env.example to .env and add your API Key"
Write-Host "2. Run: .\.venv\Scripts\streamlit run chat_app.py"
