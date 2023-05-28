from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup
import logging
import pymongo
import os
import base64

logging.basicConfig(filename="scrapper.log", level=logging.INFO)

app = Flask(__name__)

# Custom filter for base64 encoding
@app.template_filter('custom_b64encode')
def custom_b64encode(image_data):
    return base64.b64encode(image_data).decode('utf-8')

@app.route("/", methods=['GET'])
def homepage():
    return render_template("index.html")

@app.route("/review", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            # query to search for images
            query = request.form['content'].replace(" ", "")

            # directory to store downloaded images
            save_directory = "images/"

            # create the directory if it doesn't exist
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)

            # fake user agent to avoid getting blocked by Google
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

            # fetch the search results page
            response = requests.get(f"https://www.google.com/search?q={query}&sxsrf=AJOqlzUuff1RXi2mm8I_OqOwT9VjfIDL7w:1676996143273&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiq-qK7gaf9AhXUgVYBHYReAfYQ_AUoA3oECAEQBQ&biw=1920&bih=937&dpr=1#imgrc=1th7VhSesfMJ4M")

            # parse the HTML using BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")

            # find all img tags
            image_tags = soup.find_all("img")

            # download each image and save it to the specified directory
            del image_tags[0]
            img_data = []
            for index, image_tag in enumerate(image_tags):
                # get the image source URL
                image_url = image_tag['src']

                # send a request to the image URL and save the image
                image_data = requests.get(image_url).content
                mydict = {"Index": index, "Image": image_data}
                img_data.append(mydict)
                with open(os.path.join(save_directory, f"{query}_{index}.jpg"), "wb") as f:
                    f.write(image_data)

            client = pymongo.MongoClient("mongodb+srv://pwskills:pwskills@cluster0.77r6aju.mongodb.net/?retryWrites=true&w=majority")
            db = client['image_scrap']
            review_col = db['image_scrap_data']
            review_col.insert_many(img_data)

            return render_template('results.html', img_data=img_data)
        except Exception as e:
            logging.error(e)
            return 'Something went wrong: ' + str(e)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
