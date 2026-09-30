# Student Result AI Assistant

A simple AI assistant demonstrating function calling / tool calling.

## What This Project Does

The assistant can answer questions about fictional student results.

When a user asks for a student's result, the AI decides to use the
`get_student_result` tool.

The application executes the Python function and sends the result
back to the AI.

The AI then generates the final response.

## Tool

The project contains one custom tool:

`get_student_result(student_id)`

It retrieves fictional student information using a student ID.

## Example

User:

What is the result of STU-101?

AI:

The AI calls:

`get_student_result("STU-101")`

The function returns the student's information.

The AI then generates a natural-language response.

## Test Cases

### Test 1

What is the result of STU-101?

Expected: Student information is returned.

### Test 2

What is the GPA of STU-103?

Expected: GPA 3.7 is returned.

### Test 3

What can you do?

Expected: The AI answers without using the tool.

### Test 4

What is the result of STU-999?

Expected: The assistant says that no student record was found.

## Technologies

- Python
- Streamlit
- OpenAI API
- Function Calling / Tool Calling