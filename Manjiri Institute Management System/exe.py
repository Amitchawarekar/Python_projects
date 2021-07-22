import cx_Freeze
import sys
import os
base = None
if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Program Files\Python38\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Program Files\Python38\tcl\tk8.6"

executables = [cx_Freeze.Executable("MOMS-1.py", base=base,icon='icon.ico')]

cx_Freeze.setup(
    name = "MOMS",
    options = {"build_exe": {"packages":["tkinter","os","sys","pymysql","time","PIL","tkcalendar","tempfile","pandas"], "include_files":['tcl86t.dll','tk86t.dll','Application forms','Backup','Database','image','Recipt','CertificateIssue.py','course.py','dashboard.py','enquiry_f.py','icon.ico','Recipt.py','Register.py','register_f.py','sample.py']}},
    version = "2.00",
    description = "MOMS is Manjiri Institute's Management System | Developed by Amit Chawarekar",
    executables = executables
    )
