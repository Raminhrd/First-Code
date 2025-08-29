from typing import Union

class Car :
    def __init__(self , name : str, engine : Union[ str , int] , model : int , color : str) :
        self._name = name
        self._engine = str(engine)
        self._model = model
        self._color = color

    def set_name(self , name : str):
        self._name = name

    def set_engine(self , engine : Union[str , int]) :
        self._engine = str(engine)

    def set_model(self , model : str) :
        self._model = model

    def set_color(self , color : str) :
        self._color = color

    def get_name(self) :
        return self._name
    
    def get_engine(self) :
        return self._engine
    
    def get_model(self) :
        return self._model
    
    def get_color(self) :
        return self._color
    
    def __str__(self):
        return (f' Car Name is {self._name} With The {self._engine} Engine And Model {self._model} '
                f'And The Color is {self._color}')