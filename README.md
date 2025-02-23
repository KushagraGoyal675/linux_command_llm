# Linux Command LLM

## Overview
Linux Command LLM is a fine-tuned language model designed to interpret natural language commands and generate corresponding Linux shell commands. This model is based on `open_llama_3b_v2` and has been fine-tuned to assist users in efficiently executing system operations through natural language input.

## Features
- **Natural Language to Shell Command Translation**: Converts human-readable instructions into precise Linux commands.
- **Fine-Tuned for Linux Tasks**: Covers command-line utilities, file management, networking, package management, and system monitoring.
- **Optimized for WSL ARM**: Ensuring seamless execution on ARM-based Windows Subsystem for Linux (WSL).
- **Integration with LLM Kernel**: Can be embedded into an OS with an LLM-integrated kernel for intuitive system interactions.

## Model Information
- **Base Model**: `open_llama_3b_v2`
- **Fine-Tuned Model**: [Hugging Face Repository](https://huggingface.co/kushagragoyal/fine_tuned_model)
- **Parameter Size**: 3B

## Setup & Installation

### Prerequisites
- Python 3.8+
- PyTorch
- Hugging Face Transformers Library
- WSL ARM Environment (for deployment on WSL ARM)

### Installation Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/linux_command_llm.git
   cd linux_command_llm
   ```
2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Download the Fine-Tuned Model**
   ```python
   from transformers import AutoModelForCausalLM, AutoTokenizer
   
   model_name = "kushagragoyal/fine_tuned_model"
   tokenizer = AutoTokenizer.from_pretrained(model_name)
   model = AutoModelForCausalLM.from_pretrained(model_name)
   ```

## Usage

### Running the Model
```python
from transformers import pipeline

pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
command = pipe("List all files in the current directory")
print("Generated Command:", command[0]['generated_text'])
```

### Example Queries
| Input (Natural Language) | Output (Shell Command) |
|--------------------------|------------------------|
| "List all files in a directory" | `ls -l` |
| "Show the current working directory" | `pwd` |
| "Check disk usage" | `df -h` |
| "Find a file named 'log.txt'" | `find / -name 'log.txt'` |

## Roadmap
- **Phase 1**: Basic Linux command support (✓ Completed)
- **Phase 2**: Context-aware command generation
- **Phase 3**: Support for multi-command workflows
- **Phase 4**: Full OS integration with LLM kernel

## Contribution
Contributions are welcome! If you’d like to improve the model, fine-tune additional commands, or integrate new features, feel free to submit a pull request.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

