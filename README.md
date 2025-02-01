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

## Jupyter Notebook JSON Structure

### Understanding Notebook Metadata

Jupyter notebooks are stored as JSON files with a specific structure:

```json
{
    "cells": [
        {
            "cell_type": "markdown|code",
            "metadata": {},
            "source": ["Cell content as an array of strings"]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.8.5"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}
```

### Key Components
- **cells**: Array of notebook cells (markdown or code)
- **metadata**: Information about kernel and language
- **nbformat**: Notebook format version
- **nbformat_minor**: Minor version of the notebook format

### Troubleshooting Tips
- Ensure valid JSON structure
- Check for proper cell formatting
- Verify metadata is correctly defined
- Use tools like `nbconvert` to validate notebooks

## Performance Evaluation

### DeepSeek Performance Notebook
The `DeepSeek_Performance_Evaluation.ipynb` provides a comprehensive assessment of the DeepSeek-R1 model's capabilities:

#### Evaluation Metrics
- **Reasoning Performance**
  - Tests across different difficulty levels
  - Measures response time and token count
  - Includes easy, medium, and hard reasoning tasks

- **Coding Performance**
  - Evaluates code generation in multiple languages
  - Assesses response time and code complexity
  - Languages tested: Python, JavaScript, Rust

#### Visualization
- Bar charts comparing response times
- Performance metrics across different task types
- Insights into model's strengths and limitations

### How to Run
```bash
jupyter notebook DeepSeek_Performance_Evaluation.ipynb
```

### Customization
- Easily extend test cases
- Add more programming languages
- Modify difficulty levels

### Key Insights
- Quantitative analysis of AI model performance
- Benchmark DeepSeek-R1's reasoning and coding abilities
- Provides a structured approach to model evaluation

## Full Performance Evaluation Notebook Content

### Note
For the most up-to-date and interactive version, please refer to the `DeepSeek_Performance_Evaluation.ipynb` file in the repository.

```python
# DeepSeek-R1 Performance Evaluation Notebook

# Project Overview
# This notebook provides a comprehensive performance evaluation 
# of the DeepSeek-R1 AI model across various domains and test scenarios.

# Import required libraries
from openai import OpenAI
from dotenv import load_dotenv
import os
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv('NVIDIA_API_KEY')
)

# Test Case 1: Reasoning Performance
def test_reasoning_performance(prompts):
    results = []
    for difficulty, prompt in prompts.items():
        start_time = time.time()
        response = client.chat.completions.create(
            model="deepseek-ai/deepseek-r1",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        end_time = time.time()
        
        results.append({
            'difficulty': difficulty,
            'prompt': prompt,
            'response': response.choices[0].message.content,
            'response_time': end_time - start_time,
            'token_count': len(response.choices[0].message.content.split())
        })
    
    return pd.DataFrame(results)

# Reasoning test prompts
reasoning_prompts = {
    'easy': "What is 15 * 7?",
    'medium': "If a train travels 120 miles in 2 hours, what is its speed?",
    'hard': "Solve this logic puzzle: A farmer has chickens and cows. The total number of heads is 50 and the total number of legs is 140. How many chickens and cows does the farmer have?"
}

# Run reasoning performance tests
reasoning_results = test_reasoning_performance(reasoning_prompts)
print(reasoning_results)

# Test Case 2: Coding Performance
def test_coding_performance(coding_tasks):
    results = []
    for language, task in coding_tasks.items():
        start_time = time.time()
        response = client.chat.completions.create(
            model="deepseek-ai/deepseek-r1",
            messages=[{"role": "user", "content": task}],
            max_tokens=500
        )
        end_time = time.time()
        
        results.append({
            'language': language,
            'task': task,
            'solution': response.choices[0].message.content,
            'response_time': end_time - start_time,
            'code_length': len(response.choices[0].message.content.split('\n'))
        })
    
    return pd.DataFrame(results)

# Coding tasks for different languages
coding_tasks = {
    'Python': "Write a function to calculate the Fibonacci sequence up to n terms",
    'JavaScript': "Create a function that checks if a string is a palindrome",
    'Rust': "Implement a basic bubble sort algorithm"
}

# Run coding performance tests
coding_results = test_coding_performance(coding_tasks)
print(coding_results)

# Visualization of Performance Metrics
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
reasoning_results.plot(x='difficulty', y='response_time', kind='bar')
plt.title('Reasoning Task Response Time')
plt.xlabel('Difficulty Level')
plt.ylabel('Response Time (seconds)')

plt.subplot(1, 2, 2)
coding_results.plot(x='language', y='response_time', kind='bar')
plt.title('Coding Task Response Time')
plt.xlabel('Programming Language')
plt.ylabel('Response Time (seconds)')

plt.tight_layout()
plt.show()

# Performance Summary
# This notebook provides a comprehensive evaluation of the 
# DeepSeek-R1 model's performance across reasoning and coding tasks.
```

### Notebook Execution Notes
- Requires NVIDIA API Key
- Depends on environment variables
- Uses OpenAI client for model interaction
- Generates performance metrics and visualizations

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
