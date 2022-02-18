import random
from pathlib import Path
from time import sleep
from FilesUtils import FilesUtils
from paths import default_intellij_report_file, default_target_directory

input("Please be sure that reports folder is empty, press enter")
report_directory = input("Paste here the absolute path of the last generated report in IntelliJ: ")
intellij_report_location = report_directory if report_directory else default_intellij_report_file
intellij_report = Path(intellij_report_location)


to_save_target_directory = input("Paste here the absolute path where you want to save generated reports: ")
to_save_target_location = to_save_target_directory if to_save_target_directory else default_target_directory
to_save_target = Path(to_save_target_location)
label = input("Type a label to name the report prefix: ")


fs = FilesUtils(label, intellij_report, to_save_target)
message_count = 0

while True:
    if intellij_report.exists():
        fs.move_report_and_rename(intellij_report)
        message_count = 0

    else:
        message_count += 1
        if message_count >= 20:
            messages_to_display = ["I still here watching",
                                   "I still working, watching...",
                                   "Still watching out for a new report to save"]
            print(random.choice(messages_to_display))
            message_count = 0
    sleep(3)
