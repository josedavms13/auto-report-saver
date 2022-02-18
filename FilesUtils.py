from paths import default_target_directory


class FilesUtils:
    def __init__(self, label, intelliJ_report, to_save_target):
        self.intellij_report = intelliJ_report
        self.target_directory = to_save_target
        self._report_count = self.get_current_saver_count()
        self.label = label

    def move_report_and_rename(self, file):
        if file.name == "report-latest.html":
            print("New report found")
            file.rename(f"{self.target_directory}\\report-{self.label}-{self._report_count}.html")
            print(f"Saved: report-{self.label}-{self._report_count}.html")
            self._report_count += 1

    def get_current_saver_count(self):
        last_index = 0
        try:
            for item in self.target_directory.iterdir():
                if int(item.name[-6]) > last_index:
                    last_index = int(item.name[-6])
            return last_index + 1
        except ValueError:
            return 0
        except FileNotFoundError:
            self.target_directory.mkdir()
            self.get_current_saver_count()
