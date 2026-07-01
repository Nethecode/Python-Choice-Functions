@echo off
python -c "import shutil, sys, os; [os.remove(os.path.join(p, 'choice.py')) for p in sys.path if 'site-packages' in p and os.path.exists(os.path.join(p, 'choice.py'))]"
pip uninstall choice-functions