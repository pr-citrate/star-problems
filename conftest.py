from typing import Callable, Optional

import pytest
import subprocess
import os
import sys

@pytest.fixture
def run_script() -> Callable[[str, Optional[str]], str]:
    def _runner(script_path: str, input_text: Optional[str]) -> str:
        base_path = os.path.dirname(__file__)
        script_path = os.path.join(base_path, script_path)

        if not os.path.exists(script_path):
            raise FileNotFoundError(f"{script_path} not found")

        command = [sys.executable, script_path]

        result = subprocess.run(
            command,
            input=input_text,
            capture_output=True,
            encoding="utf-8",
            text=True,
            check=False,
        )

        error_messages = []
        if result.returncode != 0:
            error_messages.append(f"Script failed with return code {result.returncode}.")

        if result.stderr:
            error_messages.append("Stderr was not empty.")

        if error_messages:
            pytest.fail(
                f"{"\n".join(error_messages)}\n\
                --- STDERR ---\n{result.stderr}",
                pytrace=False
            )

        return result.stdout.strip()
    return _runner
