# 🐍 MenuPy 🐍
## About 📖
MenuPy is a simple library to add easy menus and titles to your python text-based games.
## Installation 💾
- Hit the green "Code" button in the top right of this page
- Hit "Download Zip"
- Find the .zip file and extract it
- Open the command terminal in the newly extracted folder
- Type ``pip install -e .``
- You're done!
## How To Use 👾
### Importing
At the top of your python project, add ``from menupy import *``

### menu()
To add a simple menu with no title, do ``menu(list)``

In place of list, you need to add a list such as ``['Apple', 'Banana', 'Blueberry']``

### menuwithtitle()
To add a simple menu with a title, do ``menu(title, list)``

In place of title, you need to add a title such as ``'Where do you want to go?'``

In place of list, you need to add a list such as ``['School', 'Market', 'House]``
### title()
To add a simple title without a menu, do ``title(title)``

In place of title, you need to add a title such as ``'Greetings!'``
