# BranchToTag  
### Python based script to create git tags for the given branch names.   
Recently I had to come up with an easy way to cleanup a Git repository with some 200+ branches, Where we also wanted to archive few branches as tags. 
  
## Features  
   - Create git Tags and delete the tagged branches.  
   - Delete the given branches without tagging.   
   - Maintain the history of the script process under clean_up_history.json  
  
## How To Use (Changes required in main.py)  

1. Set your local repo path  
```  
LOCAL_REPO_PATH = "/Users/PycharmProjects/your_local_project_git_folder/"  
```  

2. If you want to create git tags and delete the tagged branches.   

```  
if __name__ == '__main__':  
 set_local_repo() 
 branches = ['branch_name_1', branch_name_2 ...] 
 create_tags(branches)````  
```

 3. If you want to just delete some git branches  

```
if __name__ == '__main__':  
 set_local_repo() 
 branches = ['branch_name_1', branch_name_2 ...] 
 delete_branches(branches)```  
```  

4. If you wish to change the prefix of the tag modify this. 

```
TAG_PREFIX = "archive"
```

## Run   
    main.py  
  
## clean_up_history.json  
Either the script is creating tag or deleting a given a branch. It will be recorded in the clean_up_history.json for future reference.   
```yaml  
{  
 //name of the branch which are already processed by the script  
 "processed": [],  
 // name of the branch which are deleted 
 "deleted": [], 
 //name of the tags created by the script 
 "tagged": []
 }  
```  
  
## Contributing   
 Love your input! I wanted to make contributing to this project as easy and transparent as possible, whether it's:  
    - Reporting a bug  
    - Discussing the current state of the code  
    - Submitting a fix  
  
## License  
```  
MIT License  
  
Copyright (c) 2021 Lingaraj Sankaravelu  
  
Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:  
  
The above copyright notice and this permission notice shall be included in all  
copies or substantial portions of the Software.  
  
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.  
```