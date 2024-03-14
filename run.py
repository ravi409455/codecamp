import os
import json
import importlib.util
import sys


def run_solution(problem_dir):
    # Load test cases
    test_cases_path = os.path.join(problem_dir, "testcases.json")
    with open(test_cases_path, "r") as file:
        test_cases = json.load(file)

    # Import solution function
    spec = importlib.util.spec_from_file_location(
        "solution", os.path.join(problem_dir, "solution.py")
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    solution_function = getattr(solution_module, "solution")
    compare_output = getattr(solution_module, "compare_output", None)

    # Run test cases
    for idx, test_case in enumerate(test_cases, start=1):
        inputs = test_case.get("input", {})
        expected_output = test_case.get("output")

        result = solution_function(**inputs)

        testcase_result = False
        if compare_output:
            testcase_result = compare_output(result, expected_output)
        else:
            testcase_result = result == expected_output

        if testcase_result:
            print(f"Test case {idx} passed.")
        else:
            print(f"Test case {idx} failed.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run.py <problem_directory>")
        sys.exit(1)

    problem_dir = sys.argv[1]
    run_solution(problem_dir)
