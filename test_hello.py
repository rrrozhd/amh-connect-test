import subprocess
import sys
import unittest
from pathlib import Path

from hello import greet


class GreetTests(unittest.TestCase):
    def test_world(self):
        self.assertEqual(greet("world"), "Hello, world!")

    def test_other_names(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")

    def test_running_script_prints_world_greeting(self):
        script = Path(__file__).with_name("hello.py")
        result = subprocess.run(
            [sys.executable, str(script)],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(result.stdout, "Hello, world!\n")


if __name__ == "__main__":
    unittest.main()
