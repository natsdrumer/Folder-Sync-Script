# Folder-Sync-Script
This project is a Python script that automatically synchronizes two folders: a source folder and a replica folder. The synchronization is one-way — the replica folder is periodically updated to exactly match the content of the source folder.

⚙️ Features
Automatic synchronization at user-defined intervals.

New or modified files in the source folder are copied to the replica.

Files deleted from the source folder are also removed from the replica.

All operations (copying, updating, deletion) are logged to both the console and a log file.

Source folder, replica folder, synchronization interval, and log file path are provided via command-line arguments.

🐍 Requirements
Python 3.6 or higher

▶️ How to Use
Run the script with the following arguments:
python sync.py <source_folder> <replica_folder> <interval_in_seconds> <log_file_path>

Example:
python sync.py /home/user/source /home/user/replica 10 /home/user/logs/sync_log.txt

In this example:
The folder /home/user/replica will be updated every 10 seconds to match /home/user/source.
All operations will be logged to /home/user/logs/sync_log.txt.

📁 Project Structure
│
├── sync.py           # Main synchronization script
├── README.md         # Documentation

📝 Logging
Each operation is timestamped and logged both to the console and to the specified log file. Example output:
2025-04-11 14:32:10,123 - File copied: /source/file1.txt -> /replica/file1.txt
2025-04-11 14:32:20,456 - File removed: /replica/old_file.txt

🔒 License
This project is licensed under the MIT License. See the LICENSE file for more details.

🙋 Author
Natanael Duarte

If you have any questions or suggestions, feel free to open an issue or get in touch!

