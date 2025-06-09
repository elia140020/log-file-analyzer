import argparse


def analyze_log_file(filename='system.log', level=None, output=None):
    # Initialize counters
    info_count = 0
    warning_count = 0
    error_count = 0
    timestamps = []
    filtered_lines = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('[INFO]'):
                    if level is None or level == 'INFO':
                        info_count += 1
                        if output and (level == 'INFO' or level is None):
                            filtered_lines.append(line)
                elif line.startswith('[WARNING]'):
                    if level is None or level == 'WARNING':
                        warning_count += 1
                        if output and (level == 'WARNING' or level is None):
                            filtered_lines.append(line)
                elif line.startswith('[ERROR]'):
                    if level is None or level == 'ERROR':
                        error_count += 1
                        if output and (level == 'ERROR' or level is None):
                            filtered_lines.append(line)

                try:
                    timestamp = line.split(']')[1].strip().split(' - ')[0]
                    timestamps.append(timestamp)
                except IndexError:
                    pass

        print(" analyze log:")
        print(f"Number of messages: {info_count}")
        print(f"Number of messages: {warning_count}")
        print(f"Number of messages: {error_count}")

        # Alert if nothing is found
        if level and info_count + warning_count + error_count == 0:
            print(f"No messages of level {level} found.")
            return

        if timestamps:
            print(f"first message: {timestamps[0]}")
            print(f"last message: {timestamps[-1]}")
        if output and filtered_lines:
            try:
                with open(output,'w',encoding='utf-8') as out_file:
                    out_file.writelines(filtered_lines)
                print(f'Filtered messages saved to: {output}')
            except Exception as e:
                print(f"Error writing to output file: {e}")
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
    parser.add_argument(
        '--output',
        help='File to save filtered log message (optional)'
    )

    args = parser.parse_args()
    analyze_log_file(args.filename, args.level , args.output)
