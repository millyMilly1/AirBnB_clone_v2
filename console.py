#!/usr/bin/python3

"""
Console program that contains the entry point of the
command interpreter.
Uses the cmd module and a custom prompt '(HBNB) '
"""


import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand custom class to handle line-oriented commands
    Inherits from cmd.Cmd
    """
    def __init__(self):
        """Initializer for HBNBCommand class"""
        super().__init__()
        self.prompt = "(hbnb) "

    def do_quit(self, line):
        """Command to quit the program"""
        return True

    def do_EOF(self, line):
        """Command to check for 'EOF' and quit the program"""
        return True

    def do_create(self, className=None):
        """Creates a new instance of BaseModel"""
        if not className:
            print("** class name missing **")
            return
        else:
            try:
                my_model = globals()[className]()
                my_model.save()
                print("{}".format(my_model.id))
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                args = arg.split(" ")
                className, obj_id = args
                try:
                    temp_name = ".".join([className, obj_id])
                    storage_keys = list(storage.all().keys())
                    if storage_keys:
                        storage_keys_split = storage_keys[0].split(".")
                        if temp_name in storage.all().keys():
                            instances = storage.all()[temp_name]
                            if instances:
                                print(instances)
                            else:
                                print("** no instance found **")
                        elif (className == storage_keys_split[0]):
                            print("** no instance found **")
                        else:
                            print("** class doesn't exist **")
                    else:
                        print("** no instance found **")
                except KeyError:
                    print("** class doesn't exist **")
            except ValueError:
                print("** instance id missing **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                args = arg.split(" ")
                className, obj_id = args
                try:
                    temp_name = ".".join([className, obj_id])
                    if temp_name in storage.all().keys():
                        del storage.all()[temp_name]
                    else:
                        print("** no instance found **")
                except KeyError:
                    print("** class doesn't exist **")
            except ValueError:
                print("** instance id missing **")

    def do_all(self, arg=None):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        if not arg:
            all_instances = storage.all()
            print([str(instance) for instance in all_instances.values()])
        else:
            className = arg
            storage_keys = list(storage.all().keys())
#            className_instances = storage.all()
            for elements in storage_keys:
                storage_keys_split = storage_keys[0].split(".")
            if className == storage_keys_split[0]:
                print([
                    str(instance) for instance
                    in storage.all().values()
                    ])
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                className, obj_id, attrKey, attrValue = arg.split(" ")
                main_key = ".".join([className, obj_id])
                if main_key in storage.all().keys():
                    instance = storage.all()[main_key]
                    if instance:
                        if (
                                attrKey == "id" or
                                attrKey == "created_at"
                                or attrKey == "updated_at"):
                            return
                        else:
                            setattr(instance, attrKey, attrValue)
                            instance.save()
                    else:
                        print("** no instance found **")
                else:
                    classNameId = list(storage.all().keys())
                    name_id, class_id = classNameId[0].split(".")
                    if className != name_id:
                        print("** class doesn't exist **")
                    else:
                        print("** no instance found **")
            except ValueError:
                args = arg.split(" ")
                if len(args) == 0:
                    print("** class name missing **")
                elif len(args) == 1:
                    print("** instance id missing **")
                elif len(args) == 2:
                    print("** attribute name missing **")
                else:
                    print("** value missing **")

    def help_quit(self):
        """Help function for quit"""
        print("Command to exit the program")
        print("Usage: quit")

    def help_EOF(self):
        """Help function for do_EOF"""
        print("Command to exit the program")
        print("Usage: $ 'ctrl+d' or $ 'EOF'.")

    def help_create(self):
        """Help function for do_create"""
        print("Function to create new instance of class object.")
        print("Usage: $ create <class name>")

    def help_show(self):
        """Help function for do_show"""
        print("Function to show the instance of a class object.")
        print("Usage: $ show <class name> <instance id>")

    def help_destroy(self):
        """Help function for do_destroy"""
        print("Function to destroy an instance of a class object.")
        print("Usage: $ destroy <class name> <instance id>")

    def help_all(self):
        """Help function for do_all"""
        print("Function to print all the instance of a class object.")
        print("::\tIf <class name> is not specified, prints instances.")
        print(
                "::\tIf <class name> is specified, "
                "prints all instances of the class"
                )
        print("Usage: $ all or $ all <class name> ")

    def help_update(self):
        """Help function for do_update"""
        print("Function to update the attrributes of an instance.")
        print(
                "To identify the instance to update, "
                "the class name and id are required."
                )
        print(
                "The attributes, in keys and values pair to "
                "add to the instance are also required."
                )
        print(
                "Usage: $ update <class name> <instance id> "
                "<attribute key> <attribute value>"
                )


if __name__ == '__main__':
    HBNBCommand().cmdloop()
