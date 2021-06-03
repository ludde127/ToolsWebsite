from flask import Flask, redirect, render_template
from tools import Merit
app = Flask(__name__, static_url_path='', static_folder="static", template_folder="templates")

_tools = {"merit": Merit()}
_tools_classes = list(_tools.values())


class Project:
    name = "Verktygslådan"
    author = "Ludvig Lindholm"


project = Project()


def render(template, **kwargs):
    return render_template(template, project=project, **kwargs)


@app.route('/merit')
def merit():
    return render(_tools["merit"].template)


@app.route("/")
def index():
    _tools = [Merit()]
    return render("index.html", tools=_tools_classes)


if __name__ == "__main__":
    app.run(debug=True)