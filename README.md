# SpecEval: A Multi-Aspect Benchmark for Specification Generation Across Maturity Levels

## Overview

SpecEval is a benchmarking tool designed to evaluate the capability of large language models (LLMs) in generating formal specifications, including preconditions and postconditions. This project provides resources and tools to assess and enhance the quality of generated specifications.

## Paper

**Title:** SpecEval: A Multi-Aspect Benchmark for Specification Generation Across Maturity Levels  
**Status:** Under Submission

### Abstract

Recent research has shown that large language models (LLMs) are capable of generating formal specifications, including preconditions and postconditions. We propose **SpecEval**, a multi-aspect benchmark to assess the maturity level of existing LLMs for specification generation. It is derived from a diverse set of real-world, open-source projects in Java and Python, including 748 programs sourced from HumanEval, LeetCode, and popular GitHub repositories. We define the maturity level based on the complexity of dependencies of the target code snippet and the complexity of properties being checked, and use specification equivalence checks and testing to calculate the accuracy of generated specifications. Extensive experiments on different prompting strategies and six state-of-the-art models—GPT-4, GPT-3.5, LLaMA-2, LLaMA-3, and CodeLlama—highlight the challenges in generating postconditions for complex logic and external dependencies. Our research finds that generating preconditions and postconditions with high dependency is more challenging than that with self-contained programs, and the language matters for LLMs to generate formal specifications, underscoring the need for further improvements. Our analysis provides insights into the current progress and future directions for enhancing models’ abilities to generate accurate and comprehensive specifications.

### Data
The data for the real world project part is in following link https://drive.google.com/drive/folders/1X2kOhON066jRfslnpGNUJt8Nz6vj0YPA

### Evaluation tool 

This script processes JSONL files to insert preconditions and postconditions into specified Python or Java files. It then executes the modified files and prints the output.

#### Quick Steps
The full step is in the read.md in the Evaluation/Demo/read/md
1. **Prepare JSONL File**: Each line should include a JSON object with `"file_name"`, `"preconditions"`, and `"postconditions"`.

    **Example:**

    ```json
    {
        "file_name": "AddDigits.py",
        "preconditions": [
            "assert isinstance(n, int) and n >= 1"
        ],
        "postconditions": [
            "assert ans > 0"
        ]
    }
    ```

2. **Update Script**: Set the `jsonl_file_path` variable in the Python script to your JSONL file's path.

3. **Prepare Target Files**: Ensure the Python or Java files specified in the JSONL are accessible by the script.

4. **Run the Script**: Execute the Python script to modify, compile (if Java), and run the files.

    ```bash
    python3 eva_pipeline.py
    ```

5. **View Output**: The script prints the number of failed assertions and any other output.
