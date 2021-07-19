from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "Another Day"
    
    text = """You decide to make a cake, but you gotta decide what flavor it's gonna be first!"""

    choices = [
        ('chocolate',"Make a chocolate cake! 🍫"),
        ('carrot_cake',"Put together the best carrot cake the world will ever see. 🥕")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/chocolate")
def chocolate():
    title = "Yummy yummy chocoalte."
    
    text = """Wow good choice. Please make me some too. But... what about the filling?"""

    choices = [
        ('there_is_nothing_else',"MORE CHOCOLATE! 🍫"),
        ('there_is_nothing_else',"Use Cream cheese as a filling.")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/escape")
def carrot_cake():
    title = "No more carrots 🥕"
    
    text = """Sorry you don't have anny carrots. Maybe you can make a ^ cake?"""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/stairs")
def there_is_nothing_else():
    title = "🎂 And so it shall be. 🎂"
    
    text = """You make your cake, and you ate it too. ✨ What a wonderful day ✨"""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)