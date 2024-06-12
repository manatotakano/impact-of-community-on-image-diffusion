# Flickr Data Collection

This project collects data from Flickr and stores it in a MySQL database.

## Project Structure

- `/data` : Directory for data files
- `/scripts` : Directory for Python scripts
- `/config` : Directory for configuration files
- `/logs` : Directory for log files

## Setup

1. Install required packages:

   ```sh
   pip install -r requirements.txt
   ```

2. Configure database and API keys in `config/config.py`.

3. Run the main script:
   ```sh
   python scripts/main.py
   ```

## Requirements

- Python 3.8+
- MySQL
