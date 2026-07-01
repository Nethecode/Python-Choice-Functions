import shutil, sys, os
try:
    shutil.copy("choice.py", [p for p in sys.path if "site-packages" in p][0])
    print("SUCCESS")
except:
    print("ERROR")
input()