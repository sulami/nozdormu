# coding: utf-8

def format_time(arg):
    """Format timespans from seconds to smaller units with the right units"""
    if arg <= 1e-6:
        return '{}ns'.format(int(arg * 1000000000))
    elif arg <= 1e-3:
        return '{}μs'.format(int(arg * 1000000))
    elif arg <= 1:
        return '{}ms'.format(int(arg * 1000))
    else:
        return '{}s'.format(int(arg))

