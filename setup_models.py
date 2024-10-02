import os
import subprocess

# Function to pull the models
def pull_models():
    models = ['mistral','llama3.2','gemma2','phi3']
    for model in models:
        print(f"Pulling model: {model}")
        subprocess.run(["ollama", "pull", model])

if __name__ == "__main__":
    pull_models()