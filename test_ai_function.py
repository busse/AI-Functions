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
        "Generate SVG triangle drawing"
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
# ... (not including previous test functions)

# Ai function test 7
def test_7(model):
    function_string = "def generate_svg_triangle(style_info: str) -> str:"
    args = ["'fill:blue;stroke:black;stroke-width:2;'"]
    description_string = """Generates an SVG drawing of a triangle with the provided style information."""

    result_string = ai_functions.ai_function(function_string, args, description_string, model)

    print(f"Output: {result_string}")

    # Assert the result string contains SVG format according to basic criteria
    print("Testing if result is in SVG format...")
    assert ('<svg' in result_string) and ('</svg>' in result_string)
    assert ('<polygon' in result_string) and ('</polygon>' in result_string)
    assert ('points=' in result_string) and ('style=' in result_string)

run_tests("gpt-4")
run_tests("gpt-3.5-turbo")