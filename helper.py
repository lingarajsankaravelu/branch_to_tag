"""Created by Lingaraj Sankaravelu at 08:16 PM 17-10-21 using PyCharm"""

from json import load, dump
from pathlib import Path


class CleanUpHistoryHelper:
    """Used to record the  tagged names and deleted branch names to clean_up_history.json"""

    KEY_PROCESSED = 'processed'
    KEY_DELETED = 'deleted'
    KEY_TAGGED = 'tagged'

    def __init__(self):
        # Reads the data from the json file, named clean_up_history.json
        base_path = Path(__file__).parent
        self.file_path = (base_path / "clean_up_history.json").resolve()
        with open(self.file_path, 'r', encoding='utf-8') as file_object:
            self.json = load(file_object)
        # parse different key values from cleanup status map
        self.processed = self.json[self.KEY_PROCESSED]
        self.deleted = self.json[self.KEY_DELETED]
        self.tagged = self.json[self.KEY_TAGGED]

    def is_deleted(self, branch_name):
        """return True if branch name is deleted already false otherwise"""
        return branch_name in self.deleted

    def is_tagged(self, tag_name):
        """return True if branch name is tagged already false otherwise"""
        return tag_name in self.tagged

    def is_processed(self, branch_name):
        """return True if branch name is processed already false otherwise"""
        return branch_name in self.processed

    def mark_deleted(self, name):
        """Append the branchName to processed and deleted, also write the same to file"""
        if name not in self.processed:
            self.processed.append(name)
        if name not in self.deleted:
            self.deleted.append(name)
        self.write_to_file__()

    def mark_tagged(self, branch_name, tag_name):
        """Records the branch_name as processed,deleted and tag_name to tagged"""
        self.processed.append(branch_name)
        self.deleted.append(branch_name)
        self.tagged.append(tag_name)
        self.write_to_file__()

    def write_to_file__(self):
        """Writes the local processed, Deleted, Tagged array to json file"""
        self.json[self.KEY_PROCESSED] = self.processed
        self.json[self.KEY_DELETED] = self.deleted
        self.json[self.KEY_TAGGED] = self.tagged
        with open(self.file_path, 'w',  encoding='utf-8') as outfile:
            dump(self.json, outfile, indent=4)
