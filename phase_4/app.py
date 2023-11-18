from api import API

app = API()


@app.route("/book")
class BooksHandler:
    def get(self, req, resp):
        resp.text = "Books Page"

    def post(self, req, resp):
        resp.text = "Endpoint to create a book"


@app.route("/home")
def home(request, response):
    response.text = "Hello from the HOME page"


@app.route("/home/{age}")
def home2(request, response, age):
    response.text = f"Hello, {age}"


def about(request, response):
    response.text = "Hello from the ABOUT page"


app.add_route("/about", about)