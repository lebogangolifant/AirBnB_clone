#0x00. AirBnB clone - The console

This is a command-line interface (CLI) for managing and interacting with the AirBnB Clone project. The AirBnB Clone project is an implementation of the Airbnb booking platform with a simplified data model. The command interpreter allows you to create, update, delete, and query instances of different classes in the project.

## Description of the Command Interpreter

The command interpreter provides a user-friendly interface for interacting with the AirBnB Clone project. It allows you to perform various actions on the data, such as creating instances, updating attributes, deleting instances, and querying instances based on different criteria.

### How to Start the Command Interpreter

To start the command interpreter, follow these steps:

1. Clone the repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run the `console.py` script using the following command:
   ```
   ./console.py
   ```
4. The command prompt `(hbnb)` indicates that the command interpreter is ready for input.

### How to Use the Command Interpreter

The command interpreter supports the following commands:

- `quit`: Exit the command interpreter.
- `EOF`: Exit the command interpreter.
- `create <class_name>`: Create a new instance of the specified class.
- `show <class_name> <instance_id>`: Display the string representation of an instance.
- `destroy <class_name> <instance_id>`: Delete an instance.
- `all` or `all <class_name>`: Display all instances or instances of a specific class.
- `update <class_name> <instance_id> <attribute_name> "<attribute_value>"`: Update an attribute of an instance.

### Examples

Using the command interpreter:

1. Create a new User instance:
   ```
   (hbnb) create User
   ```

2. Display information about a specific instance:
   ```
   (hbnb) User.show("246c227a-d5c1")
   ```

3. Delete an instance:
   ```
   (hbnb) User.destroy("Bar")
   ```

4. Display all instances of a specific class:
   ```
   (hbnb) User.all()
   ```

5. Update an attribute of an instance:
   ```
   (hbnb) User.update("38f22", "first_name", "John")
   ```

## Conclusion

The AirBnB Clone command interpreter provides an easy way to interact with the AirBnB Clone project, allowing you to manage instances and perform various operations on the data. 

