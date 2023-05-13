#!/usr/bin/python3
''' This module defines the command line interpreter '''
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    ''' This class contains the entry point for the command line interpreter'''
    prompt = '(hbnb) '

    classes = {'BaseModel': BaseModel,
               'User': User, 'State': State,
               'City': City, 'Amenity': Amenity,
               'Place': Place, 'Review': Review}

    # --- Default Methods ---
    def precmd(self, line):
        ''' Reformats input formatted like function calls
            Ex: <class name>.all() would be formatted to => all <class name>

            Ex 2: <class name>.show(<id>) would be formatted to =>
            show <class name> <id>
        '''
        if line.endswith('()'):
            line = line.strip().strip('()')
            class_and_cmd = line.split('.')
            class_ = class_and_cmd[0]
            cmd = class_and_cmd[1]
            line = cmd + ' ' + class_
            return line

        if line.endswith(')'):
            line = line.strip().strip(')').split('(')
            class_and_cmd = line[0].split('.')
            class_ = class_and_cmd[0]
            cmd = class_and_cmd[1]
            id_and_attrs = line[1]

            if '{' not in id_and_attrs:
                id_and_attrs = id_and_attrs.replace(',', '')
            else:
                id_and_attrs = id_and_attrs.replace(',', '', 1)

            line = cmd + ' ' + class_ + ' ' + id_and_attrs

        return line

    def do_quit(self, arg):
        ''' Exits tihe command line interpreter '''
        return True

    def do_EOF(self, arg):
        ''' Exits the command line interpreter '''
        print()
        return True

    # --- Overridden Methods ---
    def emptyline(self):
        ''' Executed when an empty line is passed as argument '''
        pass

    # --- Program Methods ---
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
        inst = self.classes[line[0]]()
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
        line[1] = line[1].strip('"')
        if f'{line[0]}.{line[1]}' not in storage.all():
            print('** no instance found **')
            return

        inst_obj = storage.all()[f'{line[0]}.{line[1]}']
        print(inst_obj)

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
        line[1] = line[1].strip('"')
        key = f'{line[0]}.{line[1]}'
        if key not in storage.all():
            print('** no instance found **')
            return
        storage.all().pop(key)
        storage.save()

    def do_count(self, line):
        '''Retrieves the number of instances of a classs '''

        line = line.split()
        count = 0
        for key in storage.all():
            if line[0].strip() in key:
                count += 1
        print(count)

    def do_all(self, line):
        '''Prints all string representation of all instances
           based or not on the class name.
           Ex: $ all BaseModel or $ all '''
        if line:
            line = line.split()
            if line[0] not in self.classes:
                print('** class doesn\'t exist **')
                return

        inst_list = []
        for key, value in storage.all().items():
            if line:
                if key.startswith(line[0]):
                    inst_list.append(str(value))
            else:
                class_name = key.split('.')[0]
                inst_list.append(str(value))
        print(inst_list)

    def do_update(self, line):
        ''' Updates an instance based on the class name and id
            by adding or updating attribute
            (save the change into the JSON file).
            Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"'''

        if '{' in line:
            line = line.split(' ', 2)
        else:
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
        line[1] = line[1].strip('"')
        if f'{line[0]}.{line[1]}' not in storage.all():
            print('** no instance found **')
            return
        if len(line) == 2:
            print('** attribute name missing **')
            return
        if len(line) == 3 and '{' not in line[2]:
            print('** value missing **')
            return
        key = f'{line[0]}.{line[1]}'
        inst = storage.all()[key]
        line[2] = line[2].strip()
        if line[2].startswith('{') and line[2].endswith('}'):
            dict_ = eval(line[2].replace('"', '\''))
            for key, value in dict_.items():
                setattr(inst, key, value)
        else:
            setattr(inst, line[2].strip('"'), line[3].strip('"'))
            inst.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
