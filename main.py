from pathlib import Path
from time import sleep
from files_utils import FilesUtils, get_current_saver_count

from paths import reports, created_report_file, target_directory

case_id = input("Type the case ID: ")
directory = Path(reports)
created_report_file = Path(created_report_file)
target_directory = Path(target_directory)
fs = FilesUtils(case_id, target_directory)


message_count = 0

while True:
    if created_report_file.exists():
        for file in directory.iterdir():
            fs.move_report_and_rename(file, target_directory)
            message_count = 0
            break
    else:
        message_count += 1
        print(" * " * message_count)
        if message_count >= 4:
            message_count = 0
    sleep(3)
