class DjangoLikeApp:
    def __init__(self):
        self.views = {}

    def route(self, path):
        def wrapper(func):
            self.views[path] = func
            return func
        return wrapper

    def dispatch(self, request):
        path = request.path
        view = self.views.get(path, self.not_found)
        return view(request)

    def not_found(self, request):
        return "404 Not Found"
