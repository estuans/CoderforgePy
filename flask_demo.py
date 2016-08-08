from flask import Flask
from pprint import pformat
import animals

app = Flask(__name__)

class WebSnake(animals.Snake):
    art = """
                           ____
  ________________________/ O  \___/
 <_/_\_/_\_/_\_/_\_/_\_/_______/   \


    """

@app.route("/")
def hello():
    return "You've reached the server root, nothing to see here."

@app.route("/animals")
def menagerie():
    animal_list = animals.Animal.__subclasses__()
    animal_list = pformat([a.__name__, for a in animal_list])
    return animal_list + "\n"

@app.route("/art")
def sho

if __name__ == "__main__":
    app.run()
