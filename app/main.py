from fastapi import FastAPI
from presidio_analyzer import AnalyzerEngine

app = FastAPI()
analyzer = AnalyzerEngine()

@app.get("/")
def home_page():
    text_to_be_analyzed = "Hi, My name is Yaroslav and my email is yaroslav@example.com"
    result = analyzer.analyze(text=text_to_be_analyzed, language="en")

    return result