# Codecamp

This repository contains solutions to various coding problems along with corresponding test cases. You can use this repository to practice coding and validate your solutions against the provided test cases using `Python` language.

You can even choose to add the solutions to the problem that you solve

## Getting Started

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/ravi409455/codecamp.git
    ```

2. Navigate to the cloned repository:

    ```bash
    cd codecamp
    ```

3. Add a folder for each problem you solve, the folder name can be the name of the problem.

4. Add your solution and test case files to the repository following the guidelines below.

5. Run the `run.py` script to execute your solutions against the test cases.

## Writing Solutions and Test Cases

### Solutions

- Add a folder with the name of your problem, and go inside it.
- Write your solution in a Python file named `solution.py`.
- The solution should be implemented as a function defined as `def solution`.
- The function should take arguments corresponding to the inputs specified in the test cases.
- Ensure that the function returns the correct output.

Here's an example of how a `solution` function should be written:

```python
def solution(nums):
    """
    Does the given list of numbers, has any duplicates?
    """
    # Initialize a counter to store the occurences for each unique number
    counter = {}
    for item in nums:
        
        # If a number is already there in the counter, that means it is a duplicate
        if counter.get(item):
            return True
        else:
        # Store the number in the counter
            counter[item] = 1

    # No duplicates found
    return False

```

### Test Cases

- Test cases should be defined in a JSON file named `testcases.json` which will also be kept inside the problem's folder.
- Each test case should be a dictionary with keys `input` and `output`.
- The `input` key should contain input values for the solution function as a dictionary.
- The `output` key should contain the expected output for the given input.

Here's an example of how a `testcases.json` file should be structured:

```json
[
    {
        "input": {"arg1": value1, "arg2": value2, ...},
        "output": expected_output1
    },
    {
        "input": {"arg1": value3, "arg2": value4, ...},
        "output": expected_output2
    },
    ...
]
```
## Running Solutions

To run your solutions against the test cases, use the `run.py` script located in the root directory of the repository. Pass the path to the problem directory as an argument when running the script:

```bash
python run.py /path/to/problem_directory
```

## Sample Problem

### Maximum Subarray

**Description:** Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Directory Structure**
```
codecamp
│
└── maximum_subarray/
|    │
|    ├── solution.py
|    │
|    └── testcases.json
│
└── run.py
```

**Writing Solution**

To write a solution for this problem, create a Python file named `solution.py` inside the problem directory. Write your solution function inside this file.

```python
def solution(nums):
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```
**Writing Test Cases**

Test cases are written in JSON format in a file named `testcases.json` inside the problem directory.


```json
[
    {
        "input": {"nums": [-2,1,-3,4,-1,2,1,-5,4]},
        "output": 6
    },
    {
        "input": {"nums": []},
        "output": 1
    },
    {
        "input": {"nums": [5,4,-1,7,8]},
        "output": 23
    }
]
```

**Running Solution**

To run the solution against the test cases, use the run.py script and provide the path to the problem directory as an argument.

```bash
python run.py maximum_subarray
```
This will execute the solution in solution.py against the test cases in testcases.json and print the results.


**Output:**

```bash
Test case 1 passed.
Test case 2 failed.
Test case 3 passed.
```
