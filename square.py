from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)
        
    def set_length(self,new_length):
        super().set_length(new_length)
        super().set_height(new_length)

    def set_height(self, new_height):
        super().set_length(new_height)
        super().set_height(new_height)

        


        
