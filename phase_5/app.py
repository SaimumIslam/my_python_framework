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


def error(request, response):
    raise AssertionError("This handler should not be user")


app.add_route("/about", about)
app.add_route("/error", error)


def custom_exception_handler(request, response, exception_cls):
    response.text = "Oops! Something went wrong. Please, contact our customer support at +1-202-555-0127."


app.add_exception_handler(custom_exception_handler)