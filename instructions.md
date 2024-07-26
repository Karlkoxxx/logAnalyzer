# Log Analyzer Tool

## Description

A command-line tool to analyze the content of log files. The tool should accepts the log file location and operations as input arguments and outputs results in JSON format.

## Requirements

- Python >= 3.11

## Setup

### 1. Clone the repository:
```
git clone https://github.com/Karlkoxxx/logAnalyzer.git
cd log_analyzer
```
### 2. Install the package:
#### standalone
```
pip install -r requirements.txt
```

#### docker
```
docker build -t log_analyzer .
```

## Run
### standalone
```
python log_analyzer.py input_file_path output_file_path --mfip --lfip --eps --bytes
```
### docker
```
docker run -v $(pwd):/usr/src/app log_analyzer input_file_path output_file_path  --mfip --lfip --eps --bytes output output.json
```