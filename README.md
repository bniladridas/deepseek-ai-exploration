# DeepSeek AI Exploration Project

## Model Overview: DeepSeek-R1

### Key Characteristics
- **Architecture**: Mixture of Experts (MoE)
- **Base Model**: DeepSeek-V3-Base
- **Activated Parameters**: 37 billion
- **Total Parameters**: 671 billion
- **Context Length**: 128K tokens
- **Version**: V1.0

### Model Capabilities
- State-of-the-art reasoning model
- Excels in math, code, and language tasks
- Trained using large-scale reinforcement learning (RL)
- Enhanced through supervised fine-tuning (SFT)

### Recommended Configuration
- Temperature: 0.5-0.7 (recommended: 0.6)
- Avoid system prompts
- For math problems: Include step-by-step reasoning
- Conduct multiple tests and average results

### Supported Environments
- **Runtime Engines**: vLLM and SGLang
- **Hardware**: NVIDIA Ampere, Blackwell, Jetson, Hopper, Lovelace, Pascal, Turing, Volta
- **Preferred OS**: Linux

### Licensing
- Community-driven model by DeepSeek AI
- MIT License
- Ready for research and commercial use

### Additional Resources
- [DeepSeek Website](https://www.deepseek.com/)
- [GitHub Repository](https://github.com/deepseek-ai/DeepSeek-R1)
- [Research Paper](https://arxiv.org/abs/2501.12948)

## Project Overview
This project explores the capabilities of the DeepSeek-R1 model using NVIDIA AI Enterprise's integration with multiple language runtimes.

## Prerequisites
- Python 3.8+
- Node.js 14+ (optional)
- Bash (with cURL)
- NVIDIA API Key

## Setup Instructions
1. Clone the repository
2. Create a Python virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Set up API Key:
   ```
   export NVIDIA_API_KEY='your_api_key_here'
   ```

## API Key Management

### Secure Configuration
We use a `.env` file to manage sensitive configuration details securely:

1. Copy the `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file and replace placeholders with your actual API keys:
   ```bash
   nano .env
   ```

### Best Practices
- Never commit `.env` file to version control
- Use environment variables for sensitive information
- Rotate API keys periodically
- Limit API key permissions

### Required Environment Variables
- `NVIDIA_API_KEY`: Your NVIDIA DeepSeek AI API key
- `DEEPSEEK_MODEL_NAME`: Model identifier
- `DEEPSEEK_DEFAULT_TEMPERATURE`: Model creativity setting
- `DEEPSEEK_DEFAULT_TOP_P`: Nucleus sampling parameter
- `DEEPSEEK_MAX_TOKENS`: Maximum response length

### Python Dependency for .env Support
Install python-dotenv to load environment variables:
```bash
pip install python-dotenv
```

### Example Usage in Python
```python
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Access API key
api_key = os.getenv('NVIDIA_API_KEY')
```

### Security Warning
Protect your API keys. Do not share them or expose them in public repositories.

## Running Examples

### Python Example
```bash
python deepseek_python_example.py
```

### Node.js Example
```bash
# Install Node.js dependencies
npm init -y
npm install openai

# Run the script
node deepseek_node_example.js
```

### Bash cURL Example
```bash
# Make the script executable
chmod +x deepseek_curl_example.sh

# Run the script
./deepseek_curl_example.sh
```

## Running the Notebook
```
jupyter notebook DeepSeek_Exploration.ipynb
```

## Key Components
- Python script for DeepSeek AI interaction
- Node.js script for DeepSeek AI interaction
- Bash cURL script for direct API interaction
- Jupyter Notebook for interactive exploration
- Flexible API key configuration

## Notes
- The scripts are designed to work with or without an API key
- Demonstrates model interaction in multiple languages and methods
- Supports streaming responses
- Provides multiple approaches to AI model interaction

## Acknowledgments
Thanks to the NVIDIA NIM AI Software Production Team and DeepSeek AI for providing this powerful reasoning model.
