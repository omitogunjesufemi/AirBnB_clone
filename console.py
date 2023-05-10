#!/usr/bin/python3
''' This module defines the command line interpreter '''
import cmd


class HBNBCommand(cmd.Cmd):
    ''' This class contains the entry point for the command line interpreter'''
    prompt = '(hbnb) '

    def do_quit(self, arg):
        ''' Exits tihe command line interpreter '''
        return True

    def do_EOF(self, arg):
        ''' Exits the command line interpreter '''
        return True

    def emptyline(self):
        ''' Executed when an empty line is passed as argument '''
        pass

    def create(self, line):
        '''creates an instance of Basemodel, saves it(to the JSON file),
            and prints the id '''
        if len(line) < 2:
           print('** class name missing **')
           return
        if line[1] != 'Basemodel'
           print('** class doesn\'t exist **')
           return
        inst = Basemodel()
        print(inst.id)

    def show(self, line
if __name__ == '__main__':
    HBNBCommand().cmdloop()
