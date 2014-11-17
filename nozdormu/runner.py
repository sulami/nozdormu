import json
import gc
from time import time

termc = {
    'def': '\033[0m',
    'bold': '\033[1m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'cyan': '\033[96m',
}

sub = lambda x, y: round((x - y) * 1000, 3)

class BenchRunner:
    """The standard runner for a BenchSuite"""

    def run(self, suite):
        """
        Run the benchmarks interleaved until all tests are finished,
        runs them grouped by batch. Compares to a possibly existing
        json baseline (.nozdormu) and writes a new one.  Benchmarks are
        run until they accumulate 1ms of runtime, but at least 16 times.
        """
        totalStart = time()
        noBatches = 0
        noBenchs = 0
        totalResults = []

        try: # to open the baseline file
            with open('.nozdormu', 'r') as f:
                baseline = json.loads(f.read())
        except FileNotFoundError:
            baseline = None

        self.output('Starting benchmark session\n')
        for batch in suite:
            gc.disable()
            baselineBatch = None
            if baseline:
                for b in baseline:
                    if b['batch'] == batch.__repr__():
                        baselineBatch = b['results']

            batchResults = []
            noBatches += 1
            benchsRunning = [b for b in batch]
            noBenchs += len(benchsRunning)
            batchStart = time()
            self.output('  Running Batch: {}'.format(batch))
            while len(benchsRunning) >= 1:
                for bench in benchsRunning:
                    if bench.totalTime < 0.001 or bench.count < 16:
                        bench.run()
                    else:
                        benchsRunning.remove(bench)

                        baselineBench = None
                        if baselineBatch:
                            for b in baselineBatch:
                                if b['name'] == bench.methodName:
                                    baselineBench = b
                        if not baselineBench:
                            baseComp = '{}{}{}'.format(termc['yellow'], 'new',
                                       termc['cyan'])
                        elif baselineBench['time'] >= bench.exact():
                            baseComp = '{}-{:.3}ms{}'.format(termc['green'],
                                sub(baselineBench['time'], bench.exact()),
                                termc['cyan'])
                        else:
                            baseComp = '{}+{:.3}ms{}'.format(termc['red'],
                                sub(bench.exact(), baselineBench['time']),
                                termc['cyan'])

                        self.output('    {}{}: {} ({}){}'.format( termc['cyan'],
                              bench, bench.results(), baseComp, termc['def']))
                        batchResults.append({'name': bench.methodName,
                                             'time': bench.exact(),
                                             'runs': bench.count, })

            self.output('  Batch finished, time: {}s\n'.format(
                        round(time() - batchStart, 2)))
            totalResults.append({'batch': batch.__repr__(),
                                 'results': batchResults,})
            gc.enable()

        self.output('{}Benchmarking finished\n'
                    '{} batches, {} benchmarks\n'
                    'total time: {}s{}'.format(
                    termc['bold'], noBatches, noBenchs,
                    round(time() - totalStart, 2), termc['def']))

        # Write the new baseline
        with open('.nozdormu', 'w') as f:
            f.write(json.dumps(totalResults, sort_keys=True, indent=2))

    def output(self, arg):
        """Print wrapper to easily supress output in tests"""
        print(arg)

