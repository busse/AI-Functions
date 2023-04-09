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
# ... (existing code for tests 1-6) ...

# Ai function test 7
def test_7(model):
    function_string = "def generate_svg_triangle(style: str) -> str:"
    args = ["'fill: red; stroke: black;'"]
    description_string = """Generates an SVG drawing of a triangle with the provided style information."""

    result_string = ai_functions.ai_function(function_string, args, description_string, model)

    print(f"Output: {result_string}")

    # Assert the result is an SVG with a triangle and the given style information
    print("Testing if result is a valid SVG with a triangle and the given style information...")
    expected_style = args[0].strip("'")
    assert '<?xml version="1.0" encoding="UTF-8"?>' in result_string
    assert '<svg' in result_string and '</svg>' in result_string
    assert '<polygon' in result_string and 'points=' in result_string and '/>' in result_string
    assert f'style="{expected_style}"' in result_string

run_tests("gpt-4")
run_tests("gpt-3.5-turbo")