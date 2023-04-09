import ast
import json
import time
import ai_functions
import pytest
import openai
import keys

# Initialize the OpenAI API client
openai.api_key = keys.OPENAI_API_KEY

# Run all tests, print the results, and return the number of failed tests
def run_tests(model):
    test_functions = [test_1, test_2, test_3, test_4, test_5, test_6, test_7]
    test_names = [
        "Generate fake people",
        "Generate Random Password",
        "Calculate area of triangle",
        "Calculate the nth prime number",
        "Encrypt text",
        "Find missing numbers",
        "Generate SVG triangle with style information"
    ]
    failed_tests = []

    i = 0
    for test in test_functions:
        print(f"=-=-=- Running test: {test.__name__} - {test_names[i]} with model {model} -=-=-=")
        i += 1
        try:
            test(model)
            print(f"{test.__name__}: PASSED")
        except AssertionError as e:
            print(f"{test.__name__}: FAILED - {e}")
            failed_tests.append(test)
        # Wait so as not to exceed the API rate limit
        time.sleep(1)

    # Print the total number of tests
    print(f"Total tests: {len(test_functions)}")

    # Print the number of failed tests
    print(f"Success Rate: {len(test_functions) - len(failed_tests)}/{len(test_functions)}")

# Ai function test 1
# ... Leave other test functions unchanged ...

# Ai function test 7
def test_7(model):
    function_string = "def generate_svg_triangle_with_style(style_info: str) -> str:"
    args = ["'fill: red; stroke: black; stroke-width:1;'"]
    description_string = """Generates a drawing of a triangle in SVG format with the given style information."""

    result_string = ai_functions.ai_function(function_string, args, description_string, model)

    print(f"Output: {result_string}")

    # Assert the result is a valid SVG triangle with the given style information
    try:
        print("Testing if the output is a string...")
        assert isinstance(result_string, str)
        
        # Hardcoding point values for the triangle
        a_x, a_y, b_x, b_y, c_x, c_y = 0, 0, 100, 0, 50, 50

        print("Testing if the output contains the appropriate SVG format and style information...")
        assert f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><polygon points="{a_x},{a_y} {b_x},{b_y} {c_x},{c_y}" style="{args[0].strip("'")}" /></svg>' in result_string
    except Exception as e:
        print(e)
        assert False

run_tests("gpt-4")
run_tests("gpt-3.5-turbo")