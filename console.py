#!/usr/bin/python3
"""Module for the command interpreter entry point"""

import cmd
import models
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from collections import Counter


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class command interpreter"""

    prompt = "(hbnb) "

    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.__classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        all_objs = storage.all()
        if not args:
            print([str(value) for value in all_objs.values()])
            return
        try:
            if args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            if args[0] == "all":
                print([str(value) for value in all_objs.values()])
                return
            print([str(value) for key, value in all_objs.items()
                   if args[0] in key])
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        instance = all_objs[key]
        attr_name = args[2]
        attr_value = args[3]
        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            setattr(instance, attr_name, attr_type(attr_value))
            instance.save()
        else:
            setattr(instance, attr_name, attr_value)
            instance.save()

    def do_User(self, arg):
        """Retrieve all instances of User class"""
        self.do_all("User " + arg)

    def do_State(self, arg):
        """Retrieve all instances of State class"""
        self.do_all("State " + arg)

    def do_City(self, arg):
        """Retrieve all instances of City class"""
        self.do_all("City " + arg)

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        count = Counter(obj.__class__.__name__ for obj
                        in storage.all().values())
        print(count[class_name])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
