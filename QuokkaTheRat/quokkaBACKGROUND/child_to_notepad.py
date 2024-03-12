import os
import sys
import win32com.shell.shell as shell


script = os.path.abspath(sys.argv[0])
shell.ShellExecuteEx(lpFile=sys.executable,lpParameters=script)
os.system("notepad")