def format_time(arg):
    """Format timespans from seconds to smaller units with the right units"""
    if arg <= 1e-6:
        return '{}ns'.format(round(arg * 1000000000))
    elif arg <= 1e-3:
        return '{}μs'.format(round(arg * 1000000))
    elif arg <= 1:
        return '{}ms'.format(round(arg * 1000))
    else:
        return '{}s'.format(round(arg))

