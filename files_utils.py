
class FilesUtils:
    def __init__(self, case_id, target_directory):
        self._report_count = get_current_saver_count(target_directory)
        self.case_id = case_id

    def move_report_and_rename(self, file, target_directory):
        if file.name == "report-latest.html":
            print("New report found")
            file.rename(f"{target_directory}\\report{ self.case_id }-number-{self._report_count}.html")
            self._report_count += 1


def get_current_saver_count(target_directory):
    last_index = 0

    try:
        for item in target_directory.iterdir():
            if int(item.name[-6]) > last_index:
                last_index = int(item.name[-6])
        return last_index + 1
    except ValueError:
        return 0
