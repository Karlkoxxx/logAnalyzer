import argparse
import json
import os
from collections import Counter

def parse_arguments():
    parser = argparse.ArgumentParser(description="Log file analyzer tool")
    parser.add_argument("input", nargs='+', help="Path to one or more input files")
    parser.add_argument("output", help="Path to save output in JSON format")
    parser.add_argument("--mfip", action="store_true", help="Most frequent IP")
    parser.add_argument("--lfip", action="store_true", help="Least frequent IP")
    parser.add_argument("--eps", action="store_true", help="Events per second")
    parser.add_argument("--bytes", action="store_true", help="Total amount of bytes exchanged")
    return parser.parse_args()

def read_log_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as file:
        return file.readlines()

def parse_log_entry(entry):
    fields = entry.split()
    return {
        "timestamp": float(fields[0]),
        "header_size": int(fields[1]),
        "client_ip": fields[2],
        "http_response": fields[3],
        "response_size": int(fields[4]),
        "http_method": fields[5],
        "url": fields[6],
        "username": fields[7],
        "access_type": fields[8],
        "response_type": fields[9],
    }

def analyze_logs(log_entries, options):
    ips = [entry['client_ip'] for entry in log_entries]
    timestamps = [entry['timestamp'] for entry in log_entries]
    total_bytes = sum(entry['response_size'] for entry in log_entries)

    results = {}
    if options.mfip:
        most_common_ip = Counter(ips).most_common(1)[0]
        results["most_frequent_ip"] = most_common_ip
    if options.lfip:
        least_common_ip = Counter(ips).most_common()[-1]
        results["least_frequent_ip"] = least_common_ip
    if options.eps:
        duration = max(timestamps) - min(timestamps)
        events_per_second = len(log_entries) / duration if duration > 0 else 0
        results["events_per_second"] = events_per_second
    if options.bytes:
        results["total_bytes_exchanged"] = total_bytes
    return results

def main():
    args = parse_arguments()
    all_log_entries = []
    
    for input_file in args.input:
        log_lines = read_log_file(input_file)
        for line in log_lines:
            if line.strip():  # Skip empty lines
                try:
                    log_entry = parse_log_entry(line)
                    all_log_entries.append(log_entry)
                except ValueError as e:
                    print(e)
                    continue
    
    results = analyze_logs(all_log_entries, args)
    
    with open(args.output, 'w') as output_file:
        json.dump(results, output_file, indent=4)

if __name__ == "__main__":
    main()
