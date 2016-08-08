from flask import Flask
import animals

app = Flask(__name__)

class WebSnake(animal.Snake):
    art = """
                           ____
  ________________________/ O  \___/
 <_/_\_/_\_/_\_/_\_/_\_/_______/   \


    """

@app.route("/animals")
def menagerie():
    return animal.subclasses()

if __name__ == "__main__":
    app.run()
