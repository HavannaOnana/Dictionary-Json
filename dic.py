from flask import Flask , redirect,request , render_template
import json

app=Flask(__name__,"/static")


def WordMeaning(searched_word):
    with open("data.json","r") as file:
      data=json.load(file)
    return data.get(searched_word.lower(),"Word not found in the dictionary")


@app.route("/",methods=["GET","POST"])
def Dictionary():
   if request.method=="POST":
      search_word=request.form["userText"]
      meaning=WordMeaning(search_word)
      if isinstance(meaning, list):
            meaning = " ".join(meaning)

      with open("dic.html","r") as f:
         page=""
         page=f.read()
         page=page.replace("{{content}}",str(meaning))
         page=page.replace("{{Word}}",str(search_word))
      return page
   else:
      with open("dic.html","r") as f:
         page=""
         page=f.read()
         page=page.replace("{{content}}","Word not found in the dictionary")
         page=page.replace("{{Word}}","")
      return page


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=True)