from flask import Flask, render_template, request

app = Flask(__name__)

def replace_words_in_content(content, replacements):
    for original_word, replacement_word in replacements:
        content = content.replace(original_word, replacement_word)
    return content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        file_content = request.form['file_content']
        replacements = []

        original_word = request.form.get('original_word')
        
        replacement_word = request.form.get('replacement_word')

        replacements.append((original_word, replacement_word))

        modified_content = replace_words_in_content(file_content, replacements)

        return render_template('result.html', old_content=file_content,modified_content=modified_content)

if __name__ == '__main__':
    app.run(debug=True)
