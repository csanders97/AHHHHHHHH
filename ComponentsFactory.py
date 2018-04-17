from abc import ABC, abstractmethod
class BaseComponentFactory(ABC):

    def __init__(self, text, width, height, x_pos, y_pos):
        self.width = width
        self.height = height
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        super().__init__()

    @abstractmethod
    def get_width(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_text(self):
        pass

    @abstractmethod
    def get_x_pos(self):
        pass

    @abstractmethod
    def get_y_pos(self):
        pass


class ButtonComponent(BaseComponentFactory):

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_text(self):
        return self.text

    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos



class CanvasComponent(BaseComponentFactory):

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_text(self):
        return self.text

    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos


class TextBoxComponent(BaseComponentFactory):

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_text(self):
        return self.text

    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos


class LabelComponent(BaseComponentFactory):

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_text(self):
        return self.text

    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos


class ComponentsFactory(object):
    @staticmethod
    def create_component(comp_type, width, height, text, x_pos, y_pos):
        if comp_type == 'Button':
            return ButtonComponent(width, height, text, x_pos, y_pos)
        elif comp_type == 'Canvas':
            return CanvasComponent(width, height, text, x_pos, y_pos)
        elif comp_type == 'TextBox':
            return TextBoxComponent(width, height, text, x_pos, y_pos)
        elif comp_type == 'Label':
            return LabelComponent(width, height, text, x_pos, y_pos)