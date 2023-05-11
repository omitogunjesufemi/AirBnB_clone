#!/usr/bin/python3
''' This module defines the command line interpreter '''
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    ''' This class contains the entry point for the command line interpreter'''
    prompt = '(hbnb) '

    classes = ['BaseModel']

    def do_quit(self, arg):
        ''' Exits tihe command line interpreter '''
        return True

    def do_EOF(self, arg):
        ''' Exits the command line interpreter '''
        return True

    def emptyline(self):
        ''' Executed when an empty line is passed as argument '''
        pass

    def do_create(self, line):
        '''creates an instance of Basemodel, saves it(to the JSON file),
            and prints the id '''
        line = line.split()
        if not line:
           print('** class name missing **')
           return
        if line[0] not in self.classes:
           print('** class doesn\'t exist **')
           return
        inst = eval(f'{line[0]}()')
        inst.save()
        print(inst.id)

    def do_show(self, line):
        ''' Prints the string representation of
            an instance based on the class name and id'''
        line = line.split()
        if not line:
            print('** class name missing **')
            return
        if line[0] not in self.classes:
            print('** class doesn\'t exist **')
            return
        if len(line) == 1:
            print('** instance id missing **')
            return
        if f'{line[0]}.{line[1]}' not in storage.all():
            print('** no instance found **')
            return
        inst_dict = storage.all()[f'{line[0]}.{line[1]}']
        inst = eval(f'{line[0]}(**{inst_dict})')
        print(inst)

    def do_destroy(self, line):
        ''' Deletes an instance based on the class name
            and id (save the change into the JSON file)'''
        line = line.split()
        if not line:
            print('** class name missing **')
            return
        if line[0] not in self.classes:
            print('** class doesn\'t exist **')
        if len(line) == 1:
            print('**instance id missing **')
        key = f'{line[0]}.{line[1]}'
        if key not in storage.all():
            print ('** no instance found **')
            return
        del storage.all()[key]
        #storage.save()

    def do_all(self, line):
        '''Prints all string representation of all instances
           based or not on the class name.
           Ex: $ all BaseModel or $ all '''
        if line:
            if line[0]  not in self.classes:
                print('** class doesn\'t exist **')
                return
        inst_list = []

        for key, value in storage.all():
            class_name = key.split('.')[0]
            inst =  eval(f'{class_name}(**{value})')
            inst_list.append(str(inst))

        print(inst_list)

    def do_update(self, line):
        ''' Updates an instance based on the class name and id
            by adding or updating attribute
            (save the change into the JSON file).
            Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"'''
        line = line.split()
        if not line:
            print('** class name missing **')
            return
        if line[0] not in self.classes:
            print('** class doesn\'t exist **')
            return
        if len(line) == 1:
            print('** instance id missing **')
            return
        if f'{line[0]}.{line[1]}' not in storage.all():
            print('** no instance found **')
            return
        if len(line) == 2:
            print('** attribute name missing **')
            return
        if len(line) == 3:
            print('** value missing **')
            return
        key = f'{line[0]}.{line[1]}'
        inst_dict = storage.all()[key]
        inst_dict[line[2]] = line[3]

if __name__ == '__main__':
    HBNBCommand().cmdloop()
