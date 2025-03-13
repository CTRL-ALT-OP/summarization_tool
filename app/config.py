import os

# Set the repository path (Update this based on your local setup)
REPO_PATH = os.path.expanduser("C:\\Users\\reube\\nebulatk")

# Set the API URL for sending summaries
API_URL = "https://example.com/api/summarize"

# Storage paths
SUMMARY_PATH = "storage/summaries"
DOCUMENTATION_PATH = "storage/documentation"

# Ensure directories exist
os.makedirs(SUMMARY_PATH, exist_ok=True)
os.makedirs(DOCUMENTATION_PATH, exist_ok=True)
