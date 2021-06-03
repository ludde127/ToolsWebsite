from flask import render_template


class Tool:
    def __init__(self, name: str, desc: str, template: str):
        self.name = name
        self.desc = desc
        self.template = template
        self.view = self.name.lower()


class Merit(Tool):
    def __init__(self):
        super().__init__("Merit", "Använd detta för att beräkna ditt merit poäng i gymnasiet.", "merit.html")

