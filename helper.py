# Created by Lingaraj Sankaravelu at 08:16 PM 17-10-21 using PyCharm
# Used to record the  tagged names and deleted branch names to clean_up_history.json

from json import load, dump
from pathlib import Path


class CleanUpHistoryHelper:

    KEY_PROCESSED = 'processed'
    KEY_DELETED = 'deleted'
    KEY_TAGGED = 'tagged'

    def __init__(self):
        # Reads the data from the json file stored under this project named clean_up_history.json
        base_path = Path(__file__).parent
        self.filePath = (base_path / "clean_up_history.json").resolve()
        with open(self.filePath, 'r') as file_object:
            self.json = load(file_object)
        # parse different key values from cleanup status map
        self.processed = self.json[self.KEY_PROCESSED]
        self.deleted = self.json[self.KEY_DELETED]
        self.tagged = self.json[self.KEY_TAGGED]

    def is_deleted(self, branch_name):
        return branch_name in self.deleted

    def is_tagged(self, tag_name):
        return tag_name in self.tagged

    def is_processed(self, branch_name):
        return branch_name in self.processed

    def mark_deleted(self, name):
        if name not in self.processed:
            self.processed.append(name)
        if name not in self.deleted:
            self.deleted.append(name)
        self.write_to_file__()

    # Marks the  branch as processed,tagged and deleted and write it to clean_up_history.json file
    def mark_tagged(self, branch_name, tag_name):
        self.processed.append(branch_name)
        self.deleted.append(branch_name)
        self.tagged.append(tag_name)
        self.write_to_file__()

    def write_to_file__(self):
        self.json[self.KEY_PROCESSED] = self.processed
        self.json[self.KEY_DELETED] = self.deleted
        self.json[self.KEY_TAGGED] = self.tagged
        with open(self.filePath, 'w') as outfile:
            dump(self.json, outfile, indent=4)