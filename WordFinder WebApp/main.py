from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from nltk.corpus import words
import itertools, time, nltk
from collections import defaultdict
from typing import Set, List

# Download word list if not already downloaded
nltk.download('words')

class Operation(BaseModel):
    letters: str

app = FastAPI()

# Return a webpage to Access the Application
@app.get("/", response_class=HTMLResponse)
def main():
    return '''
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FastAPI Word Finder</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
                padding: 0;
                background-color: #f4f4f4;
                color: #333;
            }
            h1 {
                color: #333;
                text-align: center;
            }
            input[type="text"] {
                padding: 10px;
                font-size: 16px;
                width: calc(100% - 22px);
                margin-bottom: 10px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                color: #fff;
                background-color: #007bff;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
            #check {
                display: inline-block;
                margin-left: 10px;
                font-size: 13px;
                border: 1px solid #ccc0;
                padding: 6px;
                border-radius: 4px;
            }
            pre {
                background-color: #fff;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 4px;
                white-space: pre-wrap; /* Ensure long lines wrap */
                word-wrap: break-word; /* Break long words */
                max-height: 200px;
                overflow-y: auto;
            }
        </style>
        <script>
            async function updateList() {
                document.getElementById('check').innerText = 'Checking';
                document.getElementById('check').style.border = '1px solid #ccc';
                const letters = document.getElementById('element').value;
                const response = await fetch('/check', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ letters })
                });
                const result = await response.json();
                document.getElementById('result').innerText = JSON.stringify(result, null, 2);
                document.getElementById('check').innerText = 'Done Check other';
            }
        </script>
    </head>
    <body>
        <h1>FastAPI Word Finder</h1>
        <input type="text" id="element" placeholder="Enter letters">
        <br>
        <div>
            <button onclick="updateList()">Check</button>
            <div id="check"></div>
        </div>
        <pre id="result">{}</pre>
    </body>
    </html>
    '''

# post api to return the finded words
@app.post("/check")
async def check_words(op: Operation):
    letter = op.letters.lower()
    result = find_words_using_all_letters(letter)
    return {"result": list(result)}

word_list = set(words.words())
word_lengths = defaultdict(set)
# Create sets of words on basis of lenght of word
for word in word_list:
    word_lengths[len(word)].add(word)

def find_words_using_all_letters(letters):
    possible_words = set()
    start = time.time()
    letters = letters.lower()
    length = len(letters)

    # Generate permutations of the exact length needed
    if length < 15:   
        if length in word_lengths:
            permutations = set(itertools.permutations(letters, length)) # All possible permutations to check
            for combo in permutations:
                word = ''.join(combo)
                if word in word_lengths[length]: 
                    possible_words.add(word)
                    
    end = time.time()
    timetaken = f'Time Taken {end-start} sec'
    possible_words.add(timetaken)
    return possible_words
