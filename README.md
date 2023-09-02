# GuestsManager
This code essentially implements a simple interactive menu-driven guest management system that allows users to add, delete, search for,
list, and exit guests in the system. It utilizes an enum for menu options and a list to store guest names.
The program is structured around a loop that keeps running until the user decides to exit:

1. Import Statements: The code imports the Manager module and the IntEnum class from the enum library.
2. Print Welcome Message: A welcome message is printed to the console when the program starts.
3. Enum Definition: An enumeration named Menu is defined using the IntEnum class. This enum represents the menu options available in the program: Add, Delete, Search, All, and Exit.
4. Empty List: An empty list named list is created to store guest names.
5. Main Loop (Infinite): The program enters an infinite loop that displays a menu of options and waits for the user to input a choice.
6. User Input: The user is prompted to input a choice from the menu. The int() function is used to convert the input into an integer.
7. Option Handling:
  - If the user selects the "Add" option, the program prompts for a guest's name, adds it to the list, and confirms the addition.
  - If the user selects the "Delete" option, the program prompts for a name and uses the Manager.Remove() function to remove the guest from the list.
  - If the user selects the "Search" option, the program checks if the entered name is in the list and provides appropriate feedback.
  - If the user selects the "All" option, the program displays all guests in the list with their corresponding numbers.
  - If the user selects the "Exit" option, the program prints a goodbye message and exits the loop.
8. Invalid Choice Handling: If the user enters an invalid choice, the program informs them of the error.


