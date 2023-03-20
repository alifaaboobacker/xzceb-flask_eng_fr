import machinetranslation
from flask import Flask
app=Flask("translator application")
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/englishToFrench')
def englishToFrench(englishText):
    text_to_translate=request.args.get(englishText)
    french_text=translator.english_to_french(text_to_translate)
    return french_text
@app.route('/frenchToEnglish')
def frenchToEnglish(translate_text):
    text_to_translate=request.args.get(translate_text)
    english_text=translator.french_to_english(text_to_translate)
    return english_text
if __name__ == "__main__":
    #app.run(debug = True, port = 5000)
    app.run(host = "0.0.0.0", port = 8080
