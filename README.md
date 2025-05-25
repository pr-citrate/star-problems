# Star Problems Repository

This repository is a collection of programming challenges focused on printing various patterns of stars (`*`). It's
designed for practicing basic programming skills.

---

## Repository Structure

The repository is organized as follows:

```
.
├── problems/         # Contains problem descriptions in markdown (multiple languages)
│   ├── <problem_name>.<lang>.md
│   └── ...
├── answers/          # Contains reference solutions and their tests
│   ├── <problem_name>.py
│   ├── <problem_name>_test.py
│   └── ...
├── solves/           # Directory for your own solutions
│   ├── <problem_name>.py
│   └── ...
├── conftest.py       # Pytest configuration for testing/judging
├── pytest.ini        # Pytest settings
└── README.md         # This file
```

* **`problems/`**: Holds the descriptions of each programming challenge. We aim to provide descriptions in multiple
  languages (e.g., `.en.md` for English, `.ko.md` for Korean).
* **`answers/`**: Contains the official or reference Python solutions (`.py`) for each problem and their corresponding
  `pytest` test files (`_test.py`).
* **`solves/`**: This directory is empty by default but is the recommended place for *you* to save your solutions.
* **`conftest.py`**: A special `pytest` file that provides shared fixtures (helper functions) for testing. These
  fixtures help run your scripts and compare their output against the expected results.
* **`pytest.ini`**: Configuration file for `pytest`, defining markers and default options.

---

## How to Solve Problems

1. **Choose a Problem**: Browse the `problems/` directory. Pick a problem you want to solve and read its markdown
   description (e.g., `single_star.en.md`).
2. **Write Your Solution**: Create a Python file (e.g., in a `solves/` directory you create) and write the code to solve
   the problem.
3. **Test Your Solution**:
    * Ensure you have `pytest` installed (`uv sync`).
    * Find the test file in `answers/` that corresponds to your problem.
    * **Important**: Edit the test file. Look for the line `answer_path = "solves/<problem_name>.py"` and make sure it
      points to *your* solution file.
    * Open your terminal or command prompt, navigate to the root directory of this repository, and run the command:
      `pytest answers/<problem_name>_test.py -m judge`
    * The tests will run, comparing your script's output to the expected output. If all tests pass, congratulations! If
      not, review the error messages and debug your code.

---

## How to Contribute

### How to Add New Problems

If you want to contribute by adding new star-printing challenges:

1. **Problem Description**:
    * Create a new markdown file in `problems/`.
    * Clearly define the problem, input specifications (if any), output specifications, and provide examples.
    * If possible, add translations.
2. **Reference Solution**:
    * Write a correct Python solution and save it in `answers/`.
3. **Test File**:
    * Create a `pytest` test file in `answers/`.
    * Import `pytest`.
    * Define the `expected_path` to point to your reference solution.
    * Create a `test_judge` function using the `@pytest.mark.judge` decorator. This test should use the `compare_script`
      fixture (from `conftest.py`) to compare a potential user's solution (assumed path: `solves/<problem_name>.py`)
      with your reference solution.
    * Add other test functions using the `compare_output` fixture to check specific inputs and outputs. You may use
      `run_script` fixtures to judge. See existing `_test.py` files for examples.

### How to make other changes

We welcome contributions beyond adding new problems! Whether it's fixing a typo, improving documentation, enhancing the
testing framework, or fixing bugs in existing solutions, your help is appreciated.

Here's how you can contribute:

1. **Report Issues**: If you find a bug or have a suggestion, please open an issue on the GitHub repository. Provide as
   much detail as possible.
2. **Submit Pull Requests**: For direct contributions:
    * **Fork** the repository to your own GitHub account.
    * **Clone** your fork to your local machine.
    * Create a **new branch** for your changes (e.g., `git checkout -b feature/improve-docs` or
      `git checkout -b fix/test-runner-bug`).
    * **Make your changes** and commit them with clear, descriptive messages.
    * **Push** your changes to your fork on GitHub.
    * Open a **Pull Request** (PR) from your branch to the main repository's `main` branch.
    * Describe your changes in the PR and explain why they are beneficial.

We'll review your contribution and merge it if it aligns with the project's goals.

---

## Running Tests

* **Run standard tests**: `pytest` (This runs tests *without* the `judge` marker by default, as set in `pytest.ini`).
* **Run only judge tests**: `pytest -m judge`
* **Run all tests**: `pytest -m ""`

---

Happy coding, and may your outputs be stellar!