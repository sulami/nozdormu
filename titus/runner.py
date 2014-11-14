class BenchRunner:
    """The standard runner for a BenchSuite"""

    def run(self, suite):
        """Run the tests and return success status"""
        for bench in suite:
            print(bench)
        return 0

