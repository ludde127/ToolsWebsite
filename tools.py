from flask import render_template


class Tool:
    def __init__(self, name: str, desc: str, template: str, js=None):
        self.name = name
        self.desc = desc
        self.template = template
        self.view = self.name.lower()
        self.js = js

    @property
    def js_call(self):
        if self.js:
            call_ = f"<script src='{self.js}'></script>"
        else:
            call_ = ""
        return call_


class Merit(Tool):
    def __init__(self):
        super().__init__("Merit",
                         "Använd detta för att beräkna ditt merit poäng i gymnasiet.",
                         "merit.html",
                         js="js/merit.js")
