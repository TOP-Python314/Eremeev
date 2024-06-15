from typing import Self

class ClassBuilder:
    
    """Формирует текст кода класса"""
    
    default_indent_spaces: int = 4
    
    def __init__(self, class_name: str):
        self.class_name = class_name
        self.attrs = []
        self.fields = []
        
    def add_inst_attr(self, name: str, value: str | int) -> Self:
        
        """Добавляет в конструктор атрибуты экземпляра со значениями"""
        
        attr = f'self.{name} = {value!r}'
        self.attrs.append(attr)
        return self
        
    def add_cls_field(self, name: str, value: str | int) -> Self:
        
        """Добавляет в класс поля класса со значениями"""
              
        field = f'{name} = {value!r}'
        self.fields.append(field)
        return self

    def __str__(self):
        
        """Возвращает строковое представление объекта ClassBuilder"""
       
        indent: str = ' ' *  self.default_indent_spaces
        field_str: str = ''
        attr_str: str  = ''
        if self.fields:
            field_str = '\n'.join([f'{indent}{field}' for field in self.fields]) + '\n\n'
        if self.attrs: 
            attr_str = '\n'.join([f'{indent*2}{attr}' for attr in self.attrs])     
        if not self.attrs and not self.fields:
            return f'class {self.class_name}:\n{indent}pass'

        return f'class {self.class_name}:\n'\
               f'{field_str}'\
               f'{indent}def __init__(self):\n'\
               f'{attr_str}'
               
               
               
               
# >>> cb = ClassBuilder('Person').add_inst_attr('name', 'Liliya').add_inst_attr('age', 33)
# >>> print(cb)
# class Person:
    # def __init__(self):
        # self.name = 'Liliya'
        # self.age = 33
# >>> cb = ClassBuilder('Person').add_cls_field('__protected', []).add_inst_attr('name', '').add_inst_attr('age', 0)
# >>> print(cb)
# class Person:
    # __protected = []

    # def __init__(self):
        # self.name = ''
        # self.age = 0
# >>> cb = ClassBuilder('Person')
# >>> print(cb)
# class Person:
    # pass
# >>>