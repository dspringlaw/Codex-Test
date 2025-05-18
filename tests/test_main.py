import unittest
from codex_test import main

class TestMain(unittest.TestCase):
    def test_main_runs(self):
        # capture output
        import io
        from contextlib import redirect_stdout
        buf = io.StringIO()
        with redirect_stdout(buf):
            main.main()
        self.assertIn("Codex-Test", buf.getvalue())

if __name__ == '__main__':
    unittest.main()
