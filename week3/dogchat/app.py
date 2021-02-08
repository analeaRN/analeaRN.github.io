from flask import Flask, render_template #opens flask from Flask
from fake_data import dogs, posts, get_dog_by_handle, get_user_posts

#python -m flask run
app = Flask(__name__, template_folder="templates", static_url_path='/static') # need to specify where is all of our trmplate folders. via arguments

#More about run

@app.route('/') #decorator; doesn't affect behavior of function; gives some info.
def feed():
    #return '<h1>This is the feed page</h1>' # this is what is returned to the page.
    # but we want it to return a page!!

    return render_template('feed.html', posts = posts, get_dog_by_handle=get_dog_by_handle) #name of file we want to use as template, you can pass through a function, but that
    #not the best way


@app.route('/dog/<string:handle>') # adding url parameters/ routes
def dog(handle):
    dog = get_dog_by_handle(handle)
    dog_posts = get_user_posts(handle)
    return render_template('dog.html', dog_name=dog['name'], dog_handle=dog['handle'], posts=dog_posts)

@app.route('/base') # This is where it lies.
def base():
    return render_template('base.html')


if __name__ == "__main__":
    app.run(debug=True)