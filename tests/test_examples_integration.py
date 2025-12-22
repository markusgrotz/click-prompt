import unittest
import subprocess
import sys
from pathlib import Path


EXAMPLE_FILE = Path(__file__).parent.parent / "example.py"

CURSOR_UP = "\x1b[A"
CURSOR_DOWN = "\x1b[B"


class TestExample(unittest.TestCase):
    """
    Run examples

    prompt_toolkit behaves very differently when it is not connected to a real TTY.
    """

    def test_example_single_cmd(self):
        result = subprocess.run(
            [sys.executable, EXAMPLE_FILE, "single", "--fruit", "Peaches"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
        )
        self.assertEqual(result.returncode, 0)
        expected_output = "Peaches"
        actual_output = result.stdout.splitlines()[-1]
        self.assertEqual(expected_output, actual_output)

    def test_example_single_accept_default(self):
        result = subprocess.run(
            [sys.executable, EXAMPLE_FILE, "single"],
            input="\n",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
        )
        self.assertEqual(result.returncode, 0)
        expected_output = "Mangoes"
        actual_output = result.stdout.splitlines()[-1]
        self.assertEqual(expected_output, actual_output)

    def test_example_single_prompt(self):
        result = subprocess.run(
            [sys.executable, EXAMPLE_FILE, "single"],
            input=f"{CURSOR_DOWN}{CURSOR_DOWN}\n",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
        )
        self.assertEqual(result.returncode, 0)
        expected_output = "Pears"
        actual_output = result.stdout.splitlines()[-1]
        self.assertEqual(expected_output, actual_output)

    def test_example_confirm_yes(self):
        result = subprocess.run(
            [sys.executable, EXAMPLE_FILE, "confirm"],
            input="y\n",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
        )
        self.assertEqual(result.returncode, 0)
        actual_output = result.stdout.splitlines()[-1]
        self.assertEqual("True", actual_output)

    def test_example_confirm_no(self):
        result = subprocess.run(
            [sys.executable, EXAMPLE_FILE, "confirm"],
            input="n\n",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
        )
        self.assertEqual(result.returncode, 0)
        actual_output = result.stdout.splitlines()[-1]
        self.assertEqual("False", actual_output)

    def test_file_path_prompt(self):
        result = subprocess.run(
            [sys.executable, EXAMPLE_FILE, "file"],
            input="\n",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
        )
        self.assertEqual(result.returncode, 0)
        expected_output = "/tmp/foo"
        actual_output = result.stdout.splitlines()[-1]
        self.assertEqual(expected_output, actual_output)

    def test_file_path_cmd(self):
        path_value = "/tmp/click_prompt_test_file"
        result = subprocess.run(
            [sys.executable, EXAMPLE_FILE, "file", "--path", path_value],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
        )
        self.assertEqual(result.returncode, 0)
        actual_output = result.stdout.splitlines()[-1]
        self.assertEqual(path_value, actual_output)


if __name__ == "__main__":
    unittest.main()
