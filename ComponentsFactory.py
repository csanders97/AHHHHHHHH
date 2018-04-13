class BaseComponent(object):

    def __init__(self):
        self.width = 1
        self.height = 1

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


class ButtonComponent(BaseComponent):

    def __init__(self):
        self.width = 10
        self.height = 10


class CanvasComponent(BaseComponent):

    def __init__(self):
        self.width = 20
        self.height = 20


class TextBoxComponent(BaseComponent):

    def __init__(self):
        self.width = 30
        self.height = 30


class LabelComponent(BaseComponent):

    def __init__(self):
        self.width = 40
        self.height = 40


class ComponentsFactory(object):
    @staticmethod
    def create_component(comp_type):
        if comp_type == 'Button':
            return ButtonComponent()
        elif comp_type == 'Canvas':
            return CanvasComponent()
        elif comp_type == 'TextBox':
            return TextBoxComponent()
        elif comp_type == 'Label':
            return LabelComponent()