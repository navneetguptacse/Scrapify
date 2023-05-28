# 🖼 Scrapify: Image Scraping Web Application

Scrapify is a web application built using Flask and Machine Learning that allows users to scrape and discover images effortlessly. With its intuitive interface and powerful backend, Scrapify simplifies the process of finding and exploring images based on user queries.

## Features

- **Image Scraping:** Enter your desired image query and click the search button to scrape images from various sources.
- **Machine Learning:** Leverage the power of machine learning algorithms to extract and curate relevant images based on user queries.
- **User-Friendly Interface:** The user interface is designed to be simple, intuitive, and accessible to users of all levels of technical expertise.

## Installation

1. Clone the repository: `git clone https://github.com/navneetguptacse/scrapify.git`
2. Navigate to the project directory: `cd scrapify`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - For Windows: `venv\Scripts\activate`
   - For macOS/Linux: `source venv/bin/activate`
5. Install the dependencies: `pip install -r requirements.txt`

## Usage

1. Run the Flask application:
   - For Windows (PowerShell): `$env:FLASK_APP = "app.py"; flask run`
   - For macOS/Linux: `export FLASK_APP=app.py && flask run`
2. Open your web browser and navigate to `http://localhost:5000`.
3. Enter your image query in the search bar and click the search button.
4. Browse through the scraped images and explore the results.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [https://ineuron.ai/](iNeuron.ai).

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/): A micro web framework for Python.
- [scikit-learn](https://scikit-learn.org/): A machine learning library for Python.
- [Unsplash API](https://unsplash.com/developers): Image API used for scraping images.
