"""Created by Lingaraj Sankaravelu at 08:16 PM 17-10-21 using PyCharm"""
import logging as log
from subprocess import check_output
from os import chdir
from helper import CleanUpHistoryHelper
from color_logger import CustomFormatter


# Setting up Logger
log.getLogger().setLevel(log.INFO)
ch = log.StreamHandler()
ch.setLevel(log.INFO)
ch.setFormatter(CustomFormatter())
log.getLogger().addHandler(ch)

# Important: Your local git repo PATH
LOCAL_REPO_PATH = "/Users/linga/PycharmProjects/serverx/"

# Prefix used for tag name example: any branch will be tagged as archive/branch_name
TAG_PREFIX = "archive"

# Loads the clean_up_history.json file to the helper class
history = CleanUpHistoryHelper()


def set_local_repo():
    """Sets your project local repo"""
    chdir(LOCAL_REPO_PATH)
    log.info("Local Git repository path:%s", LOCAL_REPO_PATH)


def switch_to_master():
    """Switch to master  and pull to get all branches Info"""
    run_cmd("git stash")
    run_cmd("git checkout master")
    run_cmd("git pull")
    log.info("Switched to master branch and pulled")


def run_cmd(git_command, use_shell=True):
    """Run's the given git command, throws exception on failure"""
    return check_output(git_command, shell=use_shell)


def generate_tag_name(branch_name):
    """Creates the Tag Name eg: archive/branch_name"""
    return TAG_PREFIX+branch_name if branch_name.startswith("/") else TAG_PREFIX+"/"+branch_name


def create_tag(branch_name):
    """Create a tag for the given branch name"""
    tag_name = generate_tag_name(branch_name)
    run_cmd("git stash")
    run_cmd("git checkout "+branch_name)
    # git tag command specified as list to avoid getting "too many arguments error"
    tag_cmd = ["git",
               "tag",
               "-a",
               tag_name,
               "-m",
               "archived branch "+branch_name]
    run_cmd(tag_cmd, False)
    # pushes the created tag
    run_cmd("git push origin "+tag_name)
    log.info("Tag created: "+tag_name+"for branch:"+branch_name)
    return tag_name


def delete_branch(branch_name):
    """Delete the branch matching the branch_name"""
    run_cmd("git checkout master")
    # Delete the branch
    run_cmd("git branch -D "+branch_name)
    # Push the deleted branch to remote
    run_cmd("git push origin :"+branch_name)
    log.info("Deleted branch: %s", branch_name)


def delete_branches(branch_names):
    """Given the list of branches, delete branch one by one"""
    for name in branch_names:
        if history.is_processed(name):
            log.info("Branch Already Processed: %s", name)
        elif history.is_deleted(name):
            log.info("Branch Already Deleted: %s", name)
        else:
            delete_branch(name)
            # Marks the branch as processed and deleted in clean_up_history.json
            history.mark_deleted(name)


def create_tags(branch_names):
    """Given the list of branches, create tag and delete branch one by one"""
    for name in branch_names:
        # The branch is already tagged/processed
        if history.is_processed(name):
            log.info("Branch Already Processed,  Skipping:%s", name)
        else:
            tag_name = create_tag(name)
            delete_branch(name)
            history.mark_tagged(name, tag_name)


if __name__ == '__main__':
    set_local_repo()
    # Add the name of the branches for the tags to be created
    branches = []
    create_tags(branches)
