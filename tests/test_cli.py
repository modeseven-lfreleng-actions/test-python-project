#!/usr/bin/env python3

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 The Linux Foundation

import os
import subprocess
import sys

from typer.testing import Result

from lfreleng_test_python_project.cli import app


def assert_no_internal_error(result: Result) -> None:
    """Fail if the command ended in an exception other than a clean exit.

    CliRunner.invoke catches exceptions, so an internal error would
    otherwise pass silently. Usage errors end in SystemExit; the exit
    code they carry differs across the supported typer versions, so it
    is not asserted here.
    """
    if result.exception is not None:
        assert isinstance(result.exception, SystemExit), repr(result.exception)


def test_help_empty(runner):
    """No arguments must not end in an internal error."""
    assert_no_internal_error(runner.invoke(app, []))


def test_hello(runner):
    result = runner.invoke(app, ["hello", "Matt"])
    assert result.exit_code == 0
    assert "Hello Matt" in result.stdout


def test_dinosaur(runner):
    """Test unicode characters like 🦖."""
    result = runner.invoke(app, ["hello", "🦖"])
    assert result.exit_code == 0
    assert "Hello 🦖" in result.stdout


def test_hello_empty(runner):
    """A missing NAME must not end in an internal error."""
    assert_no_internal_error(runner.invoke(app, ["hello"]))


def test_goodbye(runner):
    result = runner.invoke(app, ["goodbye", "Xv"])
    assert result.exit_code == 0
    assert "Bye Xv!" in result.stdout


def test_goodbye_formal(runner):
    result = runner.invoke(app, ["goodbye", "Xv", "--formal"])
    assert result.exit_code == 0
    assert "Goodbye Ms. Xv. Have a good day." in result.stdout


def test_goodbye_empty(runner):
    """A missing NAME must not end in an internal error."""
    assert_no_internal_error(runner.invoke(app, ["goodbye"]))


def test_script_completion_run():
    file_path = os.path.normpath("src/lfreleng-test-python-project/cli.py")
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", "-m", "typer", file_path, "run"],
        capture_output=True,
        encoding="utf-8",
    )
    assert "" in result.stdout
