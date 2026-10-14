<!-- Commands to create virtual environment and install package -->
PS C:\Users\user\Downloads\Xalta-Training\Python-Bootcamp> python -m venv task06   
PS C:\Users\user\Downloads\Xalta-Training\Python-Bootcamp> task06\Scripts\activate
(task06) PS C:\Users\user\Downloads\Xalta-Training\Python-Bootcamp> pip install rich
Collecting rich
  Downloading rich-15.0.0-py3-none-any.whl.metadata (18 kB)
Collecting markdown-it-py>=2.2.0 (from rich)
  Downloading markdown_it_py-4.2.0-py3-none-any.whl.metadata (7.4 kB)
Collecting pygments<3.0.0,>=2.13.0 (from rich)
  Downloading pygments-2.21.0-py3-none-any.whl.metadata (2.5 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich)
  Downloading mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Downloading rich-15.0.0-py3-none-any.whl (310 kB)
Downloading pygments-2.21.0-py3-none-any.whl (1.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 930.6 kB/s  0:00:01
Downloading markdown_it_py-4.2.0-py3-none-any.whl (91 kB)
Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Installing collected packages: pygments, mdurl, markdown-it-py, rich
Successfully installed markdown-it-py-4.2.0 mdurl-0.1.2 pygments-2.21.0 rich-15.0.0
(task06) PS C:\Users\user\Downloads\Xalta-Training\Python-Bootcamp> pip install tabulate
Collecting tabulate
  Downloading tabulate-0.10.0-py3-none-any.whl.metadata (40 kB)
Downloading tabulate-0.10.0-py3-none-any.whl (39 kB)
Installing collected packages: tabulate
Successfully installed tabulate-0.10.0
(task06) PS C:\Users\user\Downloads\Xalta-Training\Python-Bootcamp> 


<!-- Assignment 3 output -->
History
PS C:\Users\user\Downloads\Xalta-Training\Python-Bootcamp\Day-06\Assignments\empmgr-project> git log --oneline --graph --all 
l
*   ed27480 (HEAD -> main, origin/main) merge feature\report and feature\validator
|\  
| * 487293d (feature/validation) validate salary and email inputs
* | 7b85f00 (feature/report) README change task 3 output updated
* | 3a481e6 Add Department summary report
|/  
* d8252e8 Add employee menu and dependencies
* c27382e Export employee package functions
* f600ad9 Add salary input validation
* 88613bc Add JSON employee storage
* a18a428 Add employee data model
* fdd07fc Added ignore rules