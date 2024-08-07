import json
import os
import subprocess

def insert_pre_post_conditions_from_json(json_data):
    file_name = json_data['file_name']

    # Check if the specified file exists
    if not os.path.exists(file_name):
        print(f"Error: The file '{file_name}' does not exist.")
        return

    preconditions = json_data['preconditions']
    postconditions = json_data['postconditions']

    # Read the content of the Python file
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Insert 'failed_assertions = set()' at the first line
    lines.insert(0, "failed_assertions = set()\n\n")

    # Helper function to format assertions with try-except blocks
    def format_assertions_with_try_except(assertions, prefix):
        formatted_assertions = []
        for i, assertion in enumerate(assertions):
            formatted_assertions.append(f"    try:\n")
            formatted_assertions.append(f"        {assertion}\n")
            formatted_assertions.append(f"    except Exception as e:\n")
            formatted_assertions.append(f"        failed_assertions.add(\"{prefix} {i + 1} failed: \" + str(e))\n")
        return formatted_assertions

    # Find the insertion points
    for i, line in enumerate(lines):
        if line.strip().startswith("def "):
            func_signature_index = i
            break

    # Format and insert preconditions after the function signature
    precondition_lines = format_assertions_with_try_except(preconditions, "Precondition")
    lines.insert(func_signature_index + 1, "".join(precondition_lines))

    # Find the last return statement to insert postconditions before it
    return_indices = [i for i, line in enumerate(lines) if line.strip().startswith("return ")]
    if return_indices:
        return_index = return_indices[-1]
        postcondition_lines = format_assertions_with_try_except(postconditions, "Postcondition")
        lines[return_index:return_index] = postcondition_lines
    else:
        # If no return statement is found, insert postconditions at the end of the function
        lines.extend(format_assertions_with_try_except(postconditions, "Postcondition"))

    # Insert 'print(len(failed_assertions))' at the end of the file
    lines.append("\nprint(len(failed_assertions))\n")

    # Write the modified content back to the Python file
    with open(file_name, 'w') as file:
        file.writelines(lines)

    # Execute the modified file and capture the output
    result = subprocess.run(["python3", file_name], capture_output=True, text=True)

    # Print the captured output
    print(f"Output from the executed file '{file_name}':")
    print(result.stdout)

    # Print any errors encountered during execution
    if result.stderr:
        print(f"Errors during execution of '{file_name}':")
        print(result.stderr)

def process_jsonl_file(jsonl_file_path):
    with open(jsonl_file_path, 'r') as jsonl_file:
        for line in jsonl_file:
            try:
                json_data = json.loads(line.strip())
                insert_pre_post_conditions_from_json(json_data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON on line: {line.strip()}\nError: {e}")

# Example usage: change the jsonl path to the test.jsonl
jsonl_file_path = ''
process_jsonl_file(jsonl_file_path)

