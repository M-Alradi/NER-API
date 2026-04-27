set -e  # Exit on error

echo "Creating virtual environment..."
python3 -m venv .venv

echo "Activating virtual environment..."
source .venv/Scripts/activate                  # Windows
# source .venv/bin/activate                    # macOS/Linux

echo "Installing requirements..."
pip install -r requirements.txt

echo "Installing additional packages..."
pip install python-multipart

echo "Downloading spaCy model (en_core_web_sm)..."
python -m spacy download en_core_web_sm

echo "Setup complete!"