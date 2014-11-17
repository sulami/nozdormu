import json
from time import time

termc = {
    'bold': '\033[1m',
    'cyan': '\033[96m',
    'def': '\033[0m',
}

class BenchRunner:
    """The standard runner for a BenchSuite"""

    def run(self, suite):
        """
        Run the benchmarks interleaved until all tests are finished,
        runs them grouped by batch.
        """
        totalStart = time()
        noBatches = 0
        noBenchs = 0
        totalResults = []
        print('Starting benchmark session\n')
        for batch in suite:
            batchResults = []
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
                        batchResults.append({'name': bench.methodName,
                                             'time': bench.exact(),
                                             'runs': bench.count, })
            print('  Batch finished, time: {}s\n'.format(
                  round(time() - batchStart, 2)))
            totalResults.append({'batch': batch.__repr__(),
                                 'results': batchResults,})
        print('{}Benchmarking finished\n'
              '{} batches, {} benchmarks\n'
              'total time: {}s{}'.format(
              termc['bold'], noBatches, noBenchs,
              round(time() - totalStart, 2), termc['def']))
        with open('.titus', 'w') as f:
            f.write(json.dumps(totalResults, sort_keys=True, indent=2))

