import json
import re
import os
import subprocess

def convert_assertions(java_file_path, preconditions, postconditions):
    with open(java_file_path, 'r') as file:
        lines = file.readlines()

    # Flag to track if we've added the failedAssertions variable
    added_failed_assertions = False
    # List to hold the converted lines
    new_lines = []

    for i, line in enumerate(lines):
        # Add the failedAssertions variable after the class declaration
        if not added_failed_assertions and re.match(r'public\s+class\s+\w+\s*{', line.strip()):
            new_lines.append(line)
            new_lines.append("    private Set<String> failedAssertions = new HashSet<>();\n")
            added_failed_assertions = True
            continue

        # Add preconditions after the function signature
        if re.match(r'public\s+\w+\s+\w+\(.*\)\s*{', line.strip()):
            new_lines.append(line)
            new_lines.extend(convert_assertion_list(preconditions, "Precondition"))
            continue

        # Add postconditions before the return statement
        if line.strip().startswith("return "):
            new_lines.extend(convert_assertion_list(postconditions, "Postcondition"))
            new_lines.append(line)
            continue

        new_lines.append(line)

    # Ensure the size print statement is at the end of the main method
    inside_main = False
    for i, line in enumerate(new_lines):
        if "public static void main" in line:
            inside_main = True
        if inside_main and line.strip() == "}":
            new_lines.insert(i, '        System.out.println("Number of failed assertions: " + solution.failedAssertions.size());\n')
            inside_main = False

    # Write the modified content back to the Java file
    with open(java_file_path, 'w') as file:
        file.writelines(new_lines)

def convert_assertion_list(assertions, prefix):
    """Helper function to convert a list of assertions into try-catch blocks."""
    formatted_assertions = []
    for i, assertion in enumerate(assertions):
        condition = assertion.strip().replace("assert", "").replace(";", "").strip()
        formatted_assertions.append("        try {\n")
        formatted_assertions.append(f"            if (!({condition})) {{\n")
        formatted_assertions.append(f"                throw new AssertionError(\"{prefix} {i + 1} failed\");\n")
        formatted_assertions.append("            }\n")
        formatted_assertions.append("        } catch (Exception e) {\n")
        formatted_assertions.append(f"            failedAssertions.add(\"{prefix} {i + 1} failed: \" + e.getMessage());\n")
        formatted_assertions.append("        }\n")
    return formatted_assertions

def compile_and_run_java(java_file_path):
    # Get the base name and directory of the Java file
    java_dir, java_file = os.path.split(java_file_path)
    java_base = os.path.splitext(java_file)[0]

    # Compile the Java file
    compile_process = subprocess.run(["javac", java_file_path], capture_output=True, text=True)
    if compile_process.returncode != 0:
        print(f"Compilation failed for {java_file_path}:\n{compile_process.stderr}")
        return

    # Run the compiled Java class
    run_process = subprocess.run(["java", "-cp", java_dir if java_dir else ".", java_base], capture_output=True, text=True)
    if run_process.returncode == 0:
        print(f"Execution output of {java_base}:\n{run_process.stdout}")
    else:
        print(f"Execution failed for {java_base}:\n{run_process.stderr}")

def process_jsonl_file(jsonl_file_path):
    with open(jsonl_file_path, 'r') as jsonl_file:
        for line in jsonl_file:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            try:
                json_data = json.loads(line)
                file_name = json_data['file_name']

                # Check if the specified file exists
                if not os.path.exists(file_name):
                    print(f"Error: The file '{file_name}' does not exist.")
                    continue

                preconditions = json_data['preconditions']
                postconditions = json_data['postconditions']

                convert_assertions(file_name, preconditions, postconditions)
                compile_and_run_java(file_name)

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON on line: {line}\nError: {e}")

# Example usage:
jsonl_file_path = '/home/zhengsong/ml_ws/leetcode/test/test_java.jsonl'
process_jsonl_file(jsonl_file_path)
