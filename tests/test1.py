import menupy
import subprocess
from menupy import *

menuwithtitle('Where do you want to go?', ['Market', 'School', 'House', 'Grandmas House'])
input()
subprocess.run('cls', shell=True)

menu(['Apple', 'Banana', 'Blueberries'])
input()
subprocess.run('cls', shell=True)

title('Hello there!')
input()
exit()