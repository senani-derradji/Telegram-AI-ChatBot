from os import system

with open('requerements.txt','r') as file:
   for line in file:
      for module in line.split():
         cmd = system(f'python -c "import {module}"')
         if cmd == 0: print(f"{module} . exist")
         else:
            print(f"{module} . not exist\installing ...")
            system(f'pip install {module}')
            print(f"{module} . Done ...")
system("python chatBot/main.py")
