from __future__ import print_function

import gc
import json
import sys

if sys.platform == 'win32':
    from time import clock as time
else:
    from time import time

from nozdormu.util import format_time

termc = {
    'def': '\033[0m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'cyan': '\033[96m',
}

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
        self.results = []

        try: # to open the baseline file
            with open('.nozdormu', 'r') as f:
                baseline = json.loads(f.read())
        except IOError:
            baseline = None

        self.output('Starting benchmark session\n')
        for batch in suite:
            gcold = gc.isenabled()
            gc.disable()

            baselineBatch = None
            if baseline:
                for b in baseline:
                    if b['batch'] == batch.__repr__():
                        baselineBatch = b['results']
                        break

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
                                    btime = b['time']
                                    break
                        bexact = bench.exact()
                        if not baselineBench:
                            baseComp = '{}{}{}'.format(termc['yellow'], 'new',
                                       termc['cyan'])
                        elif btime >= bexact:
                            baseComp = '{}-{} / {:.1f}%{}'.format(
                                termc['green'], format_time(btime - bexact),
                                100 - bexact * 100 / btime,
                                termc['cyan'])
                        else:
                            baseComp = '{}+{} / {:.1f}%{}'.format(
                                termc['red'], format_time(bexact - btime),
                                100 - btime * 100 / bexact,
                                termc['cyan'])

                        self.output('    {}{}: {} ({}){}'.format(termc['cyan'],
                              bench, bench.results(), baseComp, termc['def']))
                        batchResults.append({'name': bench.methodName,
                                             'time': bexact,
                                             'runs': bench.count, })

            self.output('  Batch finished, time: {}\n'.format(
                        format_time(time() - batchStart)))
            self.results.append({'batch': batch.__repr__(),
                                 'results': batchResults,})

            if gcold:
                gc.enable()

        self.output('Benchmarking finished\n'
                    '{} batches, {} benchmarks\n'
                    'total time: {}'.format(
                    noBatches, noBenchs, format_time(time() - totalStart)))

        # Write the new baseline
        with open('.nozdormu', 'w') as f:
            f.write(json.dumps(self.results, sort_keys=True, indent=2))

        return self.results

    def output(self, arg):
        """Print wrapper to easily supress output in tests"""
        print(arg)

