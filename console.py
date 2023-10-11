#!/usr/bin/python3

"""
Console program that contains the entry point of the
command interpreter.
Uses the cmd module and a custom prompt '(HBNB) '
"""


import cmd
from models.base_model import BaseModel
from models import storage
#from sys import argv


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

    def help_quit(self):
        """Help function for quit"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help function for do_EOF"""
        print("EOF Command to exit the program")

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
                    temp_name= ".".join([className, obj_id])
                    if temp_name in storage.all().keys():
                        instances = storage.all()[temp_name]
                        if instances:
                            print(instances)
                        else:
                            print("** no instance found **")
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
                    temp_name= ".".join([className, obj_id])
                    if temp_name in storage.all().keys():
                        del storage.all()[temp_name]
                    else:
                        print("** no instance found **")
                except KeyError:
                    print("** class doesn't exist **")
            except ValueError:
                print("** instance id missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
