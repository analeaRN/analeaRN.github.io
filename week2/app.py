from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def start():
    title = "Another Day"
    
    text = """You decide to make a cake, but you gotta decide what flavor it's gonna be first!"""

    choices = [
        ('chocolate',"Make a chocolate cake! 🍫", url_for('static', filename='choco_cake.JPG')),
        ('carrot_cake',"Put together the best carrot cake the world will ever see. 🥕", url_for('static', filename='carrot_cake.JPG'))
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/chocolate")
def chocolate():
    title = "Yummy yummy chocoalte."
    
    text = """Wow good choice. Please make me some too. But... what about the filling?"""

    choices = [
        ('there_is_nothing_else',"MORE CHOCOLATE! 🍫", url_for('static', filename='choco_fill.JPG')),
        ('there_is_nothing_else',"Use Cream cheese as a filling.", url_for('static', filename='cream_cheese_fill.JPG'))
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/escape")
def carrot_cake():
    title = "No more carrots 🥕"
    
    text = """Sorry you don't have anny carrots. Maybe you can make a ^ cake?"""

    end_photo = url_for('static', filename='no_more_carrots.JPG')
    
    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices, end_photo=end_photo)



@app.route("/stairs")
def there_is_nothing_else():
    title = "🎂 And so it shall be. 🎂"
    
    text = """You make your cake, and you ate it too. ✨ What a wonderful day ✨"""

    end_photo = url_for('static', filename='end.JPG')

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices, end_photo=end_photo)