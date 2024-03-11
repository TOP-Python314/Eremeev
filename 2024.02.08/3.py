class ChessKing:
    
    """Описывает шахматную фигуру короля"""
    
    files: dict[str, int] = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    ranks: dict[str, int] = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8}
    
    def __init__(self, color: str = 'white', square: str = None):
        
        self.color = color
        if square is None:
            if color == 'white':
                self.square = 'e1'
            if color == 'black':
                self.square = 'e8'
        else:
            self.square = square
        
        
    def __repr__(self):
        return f'\'{self.color[0].upper()}K: {self.square}\''
        

    def __str__(self):
        return f'{self.color[0].upper()}K: {self.square}'
        
        
    def is_turn_valid(self, new_square: str) -> bool:
    
        """Принимает на вход строку нового поля и проверяет, возможен ли для данной фигуры ход с текущего поля на новое"""
               
        if (
                abs(self.files[self.square[0]] - self.files[new_square[0]]) <= 1
            and abs(self.ranks[self.square[1]] - self.ranks[new_square[1]]) <= 1
        ):
            return True
        
        
    def turn(self, new_square: str) -> None:
        
        """Принимает на вход строку нового поля и выполняет ход, выбрасывает ValueError в случае невозможности выполнить ход"""
        
        if not self.is_turn_valid(new_square):
            raise ValueError
        else:
            self.square = new_square

#>>> wk = ChessKing()
#>>> wk.color
#'white'
#>>> wk.square
#'e1'
#>>> wk.turn('e2')
#>>> wk
#'WK: e2'
#>>> wk.turn('d4')
#Traceback (most recent call last):
 # File "<stdin>", line 1, in <module>
 # File "E:\Users\doter\Desktop\python_main\dz\Eremeev\2024.02.08\3.py", line 44, in turn
  #  raise ValueError
#ValueError
#>>> bk = ChessKing('black')
#>>> print(bk)
#BK: e8            