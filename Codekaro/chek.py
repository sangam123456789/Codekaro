import subprocess

command1 = "python manage.py dumpdata Home.dp --indent 4 > dp.json"
command2 = "python manage.py dumpdata Home.tree --indent 4 > tree.json"
subprocess.run(command2, shell=True)
subprocess.run(command1, shell=True)