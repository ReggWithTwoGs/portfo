from flask import Flask, render_template, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/<username>/<int:post_id>')
def show_user_profile(username=None, post_id =None): # set to default 
    # show the user profile for that user
    return render_template('index.html', name=username, post_id=post_id)

@app.route("/")
def my_home():
    return render_template('index_.html')

# lets dynamically link to the page instead of making a new route for each HTML link.
@app.route("/<string:page_name>")
def about(page_name):
    return render_template(page_name)



"""

#If you had a contact page and wanted to print a thank you page to user 
#Building portfolio 4 through 6 teaches how to store data youd recieve 

def write_to_file(data):
    with open(database.txt, mode='a') as database
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open(database.csv, newline = " ", mode='a') as database2
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    csv_writer = csv.writer(database2, delimiter=',',  quotechar ='"', quoting =csv.QUOTE_MINIMAL)
    csv_writer.writerow(email,subject,message)


@app.route('submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
         data =request.form.to_dict()
         print(data)
         return redirect ('/thankyoupage.html')
         except:
          return 'did not save to data base'
    else:
        return ' something went wrong , please try again  '


    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

"""
"""
we dont need these routes anymore since we used the sting page name 

@app.route("/components.html")
def components():
    return "<p>Reginald doesnt need a blog !</p>"

@app.route("/work.html")
def work():
    return "<p>This is the blog id have about my dog in 2020, if i had a dog in 2020</p>"

"""