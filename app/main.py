from fastapi import FastAPI
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

app = FastAPI()
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

@app.get("/")
def home_page():
    text_to_be_analyzed = "Hi, My name is Yaroslav and my email is yaroslav@example.com"
    result = analyzer.analyze(text=text_to_be_analyzed, language="en")

    return result