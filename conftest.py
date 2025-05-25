from subprocess import Popen
from typing import Callable, Optional

import pytest
import subprocess
import os
import sys


@pytest.fixture
def run_script() -> Callable[[str, str], str] | Callable[[str], str] :
    def _runner(answer_path: str, input_text: Optional[str] = None) -> str:
        process = start_process(answer_path)
        stdout, stderr = process.communicate(input_text)

        check_fail(process, stdout, stderr)

        return stdout

    return _runner


@pytest.fixture
def compare_output() -> Callable[[str, str, str], bool] | Callable[[str, str], bool]:
    def _runner(answer_path: str, expected_output: str, input_text: Optional[str] = None) -> bool:
        process = start_process(answer_path)
        stdout, stderr = process.communicate(input_text)

        check_fail(process, stdout, stderr)

        return stdout.rstrip() == expected_output.rstrip()

    return _runner


@pytest.fixture
def compare_script() -> Callable[[str, str, str], bool] | Callable[[str, str], bool]:
    def _runner(answer_path: str, expected_path: str, input_text: Optional[str] = None) -> bool:
        answer_process = start_process(answer_path)
        expected_process = start_process(expected_path)

        answer_stdout, answer_stderr = answer_process.communicate(input_text)
        expected_stdout, _ = expected_process.communicate(input_text)

        check_fail(answer_process, answer_stdout, answer_stderr)

        return answer_stdout.rstrip() == expected_stdout.rstrip()

    return _runner


def start_process(path: str) -> Popen[str]:
    base_path = os.path.dirname(__file__)
    path = os.path.join(base_path, path)

    if not os.path.exists(path):
        pytest.fail(f"[INVALID TEST] {path} does not exist", pytrace=False)

    command = [sys.executable, path]

    return subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        text=True,
    )


def check_fail(process: Popen[str], stdout, stderr) -> None:
    error_messages = []
    if process.returncode != 0:
        error_messages.append(f"Script failed with return code {process.returncode}.")

    if stderr:
        error_messages.append("Stderr was not empty.")
        error_messages.append(f"Stdout\n>>>\n{stdout}\n<<<")
        error_messages.append(f"Stderr\n>>>\n{stderr}\n<<<")

    if error_messages:
        pytest.fail(
            f"{"\n".join(error_messages)}",
            pytrace=False
        )
