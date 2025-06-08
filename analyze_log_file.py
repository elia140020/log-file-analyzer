import argparse

def analyze_log_file(filename='system.log', level=None):
    # Initialize counters
    info_count = 0
    warning_count = 0
    error_count = 0
    timestamps = []

    try:
        with open(filename, 'r' , encoding='utf-8') as f:
            for line in f:
                if line.startswith('[INFO]'):
                    if level is None or level == 'INFO':
                        info_count += 1
                elif line.startswith('[WARNING]'):
                    if level is None or level == 'WARNING':
                        warning_count += 1
                elif line.startswith('[ERROR]'):
                    if level is None or level == 'ERROR':
                        error_count += 1

                try:
                    timestamp = line.split(']')[1].strip().split(' - ')[0]
                    timestamps.append(timestamp)
                except IndexError:
                    pass

        print(" analyze log:")
        print(f"Number of messages: {info_count}")
        print(f"Number of messages: {warning_count}")
        print(f"Number of messages: {error_count}")
        if timestamps:
            print(f"first message: {timestamps[0]}")
            print(f"last message: {timestamps[-1]}")

    except FileNotFoundError:
        print(f" File not found: {filename}")

# ------------------------------------------------------------------------------------

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Log file analysis')
    parser.add_argument(
        'filename',
        nargs='?',
        default='system.log',
        help='Log file name (default: system.log)'
    )
    parser.add_argument(
        '--level',
        choices=['INFO', 'WARNING', 'ERROR'],
        help='Filter by message type'
    )

    args = parser.parse_args()
    analyze_log_file(args.filename, args.level)