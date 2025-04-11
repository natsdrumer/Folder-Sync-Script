import os
import shutil
import time
import logging
import argparse

# Setup logging
logging.basicConfig(filename='sync_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def sync_folders(source, replica):
    # Ensure the source exists
    if not os.path.exists(source):
        print(f"Source folder {source} does not exist.")
        return

    # Ensure the replica exists, create if it doesn't
    if not os.path.exists(replica):
        os.makedirs(replica)
    
    # Synchronize source -> replica
    for item in os.listdir(source):
        source_item = os.path.join(source, item)
        replica_item = os.path.join(replica, item)
        
        if os.path.isdir(source_item):
            # Recursive call to sync subdirectories
            sync_folders(source_item, replica_item)
        else:
            # Copy file if it's new or modified
            if not os.path.exists(replica_item) or os.path.getmtime(source_item) > os.path.getmtime(replica_item):
                shutil.copy2(source_item, replica_item)
                logging.info(f"File copied: {source_item} -> {replica_item}")
                print(f"File copied: {source_item} -> {replica_item}")
    
    # Delete files from replica that no longer exist in the source
    for item in os.listdir(replica):
        replica_item = os.path.join(replica, item)
        source_item = os.path.join(source, item)
        if not os.path.exists(source_item):
            os.remove(replica_item)
            logging.info(f"File removed: {replica_item}")
            print(f"File removed: {replica_item}")

def main():
    parser = argparse.ArgumentParser(description="Synchronize two folders.")
    parser.add_argument('source', type=str, help="Path to the source folder")
    parser.add_argument('replica', type=str, help="Path to the replica folder")
    parser.add_argument('interval', type=int, help="Synchronization interval in seconds")
    parser.add_argument('logfile', type=str, help="Path to the log file")

    args = parser.parse_args()

    logging.basicConfig(filename=args.logfile, level=logging.INFO, format='%(asctime)s - %(message)s')

    while True:
        sync_folders(args.source, args.replica)
        time.sleep(args.interval)

if __name__ == "__main__":
    main()
