# JSONL-Based Python/Java File Assertion Inserter

This script processes JSONL files to insert preconditions and postconditions into specified Python or Java files. It then executes the modified files and prints the output.

## Steps to Use

### 1. JSON Format Inside the JSONL File

Each line in the JSONL file should contain a separate JSON object with the following structure:

\`\`\`json
{
    "file_name": "AddDigits.py",
    "preconditions": [
        "assert isinstance(n, int) and n >= 1""
    ],
    "postconditions": [
        "assert ans > 0""
    ]
}
\`\`\`

- **file_name**: The name of the Python file to modify (should include the `.py` extension).
- **preconditions**: A list of assertions to be added immediately after the function signature.
- **postconditions**: A list of assertions to be added just before the return statement in the function.

### 2. Replace the JSONL Path in the Script

Open the Python script and locate the following line:

\`\`\`python
jsonl_file_path = 'path/to/your/jsonl_file.jsonl'
\`\`\`

Replace \`'path/to/your/jsonl_file.jsonl'\` with the actual path to your JSONL file. This is the file containing the JSON objects with preconditions and postconditions.

### 3. Prepare the Files Within the Same Folder

Ensure that the Python files specified in the JSONL file (under \`"file_name"\`) are present in the same directory as the JSONL file or provide the correct relative paths. The script will modify these files according to the instructions in the JSONL file.

### 4. Run the Script

After completing the steps above, run the Python script. The script will:

1. Insert the specified preconditions and postconditions into the appropriate Python files.
2. Execute the modified Python files.
3. Print the number of unique failed assertions and any output from the file execution.

### Example Command

\`\`\`bash
python3 eva_pipeline_py.py
\`\`\`

### Example Output

The script will print the number of failed assertions for each Python file. For example:

\`\`\`text
Output from the executed file 'AddDigits.py':
0
\`\`\`

This output indicates that 0 unique assertion failed during the execution of `example_file.py`.
