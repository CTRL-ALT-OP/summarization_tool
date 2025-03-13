import os
import json


class Summarizer:
    def __init__(self, summary_path="storage/summaries"):
        self.summary_path = summary_path
        if not os.path.exists(self.summary_path):
            os.makedirs(self.summary_path)

    def save_summary(self, filename, summary_data):
        """Saves the summary data to a JSON file."""
        filepath = os.path.join(self.summary_path, filename)
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(summary_data, file, indent=4)

    def load_summary(self, filename):
        """Loads the summary data from a JSON file."""
        filepath = os.path.join(self.summary_path, filename)
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as file:
                return json.load(file)
        return {}

    def update_summary(self, filename, new_summary):
        """Updates an existing summary with new information."""
        existing_summary = self.load_summary(filename)
        existing_summary.update(new_summary)
        self.save_summary(filename, existing_summary)

    def generate_summary(self, code_changes):
        """Generates a structured summary from code changes."""
        summary = {
            "project": "",
            "modules": {},
        }

        for file, changes in code_changes.items():
            module_summary = {
                "functions": {},
                "classes": {},
            }

            for change in changes:
                if change["type"] == "function":
                    module_summary["functions"][change["name"]] = change["summary"]
                elif change["type"] == "class":
                    module_summary["classes"][change["name"]] = change["summary"]

            summary["modules"][file] = module_summary

        return summary
