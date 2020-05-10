from abc import ABC, abstractmethod


class UiControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class DropDownList(UiControl):
    def draw(self):
        print(" Drop down list ")


class TextBox(UiControl):
    def draw(self):
        print(" Text Box ")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
tb = TextBox()
draw([ddl, tb])
