import os

from flask import Flask, url_for, render_template, request



app = Flask(__name__)



@app.route('/')

def render_main():

  return render_template('home.html')

@app.route('/quizpage')

def render_quizpage():

  return render_template('quizpage.html')




@app.route('/results', methods =["GET", "POST"])
def get_results():
  if request.method == "POST":
      
    cuisine = request.form.get("cuisine")
      
    cook_time = request.form.get("cook_time") 

    chefs_choice = request.form.get("random")
    string_blank = str()  
    if cuisine == None and cook_time == None and chefs_choice == None:
      string_blank= "No recipes found."  
      result_list, name = list(), list()
     
    else:
      result_list, name = find_recipe(cuisine, cook_time, chefs_choice)
      
 
  return render_template('results.html', length = len(result_list), results=result_list, recipe_name = name, no_results = string_blank)

    


if __name__=="__main__":

  app.run(host='0.0.0.0')

