import urllib.request
from bs4 import BeautifulSoup

class OpenGraph:

    def __init__( self ):
        self.html_parser = 'html.parser'
        pass

    def get_page( self, url ):
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response,
                             self.html_parser,
                             from_encoding=response.info().get_param('charset'))
        return soup

    def get_title( self, soup ):
        if soup.findAll( "meta", property="og:title" ):
            return soup.find( "meta", property="og:title")["content"]
        else:
            return

    def get_description( self, soup ):
        if soup.findAll( "meta", property="og:description" ):
            return soup.find( "meta", property="og:description")["content"]
        else:
            return

    def get_site_name( self, soup ):
        if soup.findAll( "meta", property="og:site_name" ):
            return soup.find( "meta", property="og:site_name")["content"]
        else:
            return

    def get_image( self, soup ):
        if soup.findAll( "meta", property="og:image" ):
            return soup.find( "meta", property="og:image")["content"]
        else:
            return

    def get_favicon( self, soup ):
        for item in soup.find_all('link', attrs={'rel': re.compile("^(shortcut icon|icon)$", re.I)}):
            print(item.get('href'))
