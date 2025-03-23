from urllib.parse import urlparse, parse_qs

class URLTools:
    @staticmethod
    def parse(url):
        return urlparse(url)

    @staticmethod
    def parse_query_params(url):
        parsed_url = urlparse(url)
        return parse_qs(parsed_url.query)
