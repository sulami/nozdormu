from time import time

termc = {
    'bold': '\033[1m',
    'cyan': '\033[96m',
    'def': '\033[0m',
}

class BenchRunner:
    """
    The standard runner for a BenchSuite

    Runs benchmarks batch-wise interleaved (see run()) and times both
    the total time needed as well as the time per batch.
    """

    def run(self, suite):
        """
        Run the benchmarks interleaved until all tests are finished,
        runs them grouped by batch.
        """
        totalStart = time()
        noBatches = 0
        noBenchs = 0
        print('Starting benchmark session\n')
        for batch in suite:
            noBatches += 1
            benchsRunning = [b for b in batch]
            noBenchs += len(benchsRunning)
            batchStart = time()
            print('  Running Batch: {}'.format(batch))
            while len(benchsRunning) >= 1:
                for bench in benchsRunning:
                    if bench.totalTime < 0.001:
                        bench.run()
                    else:
                        benchsRunning.remove(bench)
                        print('    {}{}: {}{}'.format(termc['cyan'], bench,
                              bench.results(), termc['def']))
            print('  Batch finished, time: {}s\n'.format(
                  round(time() - batchStart, 2)))
        print('{}Benchmarking finished\n'
              '{} batches, {} benchmarks\n'
              'total time: {}s{}'.format(
              termc['bold'], noBatches, noBenchs,
              round(time() - totalStart, 2), termc['def']))

