
def analyze_log_file(filename='system.log'):
    # Initialize counters
    info_count = 0
    warning_count = 0
    error_count = 0

    # Store timestamps
    timestamps = []

    # Read file
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('[INFO]'):
                info_count += 1
            elif line.startswith('[WARNING]'):
                warning_count += 1
            elif line.startswith('[ERROR]'):
                error_count += 1

    # Extract timestamp
            try:
                timestamp = line.split(']')[1].strip().split(' - ')[0]
                timestamps.append(timestamp)
            except IndexError:
                pass

# ------------------------------------------------------------------------------------

# Print summary
    print("📊 analyze   log:")
    print(f"tedad payam hay INFO: {info_count}")
    print(f"tedad payam hay WARNING: {warning_count}")
    print(f"tedad payam hay ERROR: {error_count}")
    if timestamps:
        print(f"⏱️ first message: {timestamps[0]}")
        print(f"⏳ last message: {timestamps[-1]}")
        
# ------------------------------------------------------------------------------------


analyze_log_file('system.log')
