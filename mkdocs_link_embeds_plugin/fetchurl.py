import urllib.request

from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

class FetchURL:

    # -----------------------------------------------------------------------------------------
    #   Initialize
    # -----------------------------------------------------------------------------------------

    def __init__( self ):
        self.html_parser    = 'html.parser'
        self.encoding       = "utf-8"
        pass

    # -----------------------------------------------------------------------------------------
    #   Get Page
    #   URLs without data should be handled in the same fashion as properly propogated sites
    #   with valid metadata. 
    # -----------------------------------------------------------------------------------------

    def get_page( self, url ):
        try:
            response    = urllib.request.urlopen( url )
        except:
            response    = ""

        try:
            encoding    = response.info( ).get_param( 'charset' )
            soup        = BeautifulSoup( response, self.html_parser, from_encoding=encoding )
        except:
            soup        = BeautifulSoup( response, self.html_parser )
            soup.prettify( "latin-1" )

        return soup

    # -----------------------------------------------------------------------------------------
    #   Get > Title
    # -----------------------------------------------------------------------------------------

    def get_title( self, soup ):
        if soup.findAll( "meta", property="og:title" ):
            return soup.find( "meta", property="og:title")["content"]
        else:
            return

    # -----------------------------------------------------------------------------------------
    #   Get > Description
    # -----------------------------------------------------------------------------------------

    def get_description( self, soup ):
        if soup.findAll( "meta", property="og:description" ):
            return soup.find( "meta", property="og:description")["content"]
        else:
            return

    # -----------------------------------------------------------------------------------------
    #   Get > Name
    # -----------------------------------------------------------------------------------------

    def get_site_name( self, soup ):
        if soup.findAll( "meta", property="og:site_name" ):
            return soup.find( "meta", property="og:site_name")["content"]
        else:
            return

    # -----------------------------------------------------------------------------------------
    #   Get > Image
    # -----------------------------------------------------------------------------------------

    def get_image( self, soup ):
        if soup.findAll( "meta", property="og:image" ):
            return soup.find( "meta", property="og:image")["content"]
        else:
            return

    # -----------------------------------------------------------------------------------------
    #   Get > Fav Icon
    # -----------------------------------------------------------------------------------------

    def get_favicon( self, soup ):
        lnk_favicon         = soup.find( 'link', rel='icon' ) or soup.find( 'link', rel='shortcut icon' )

        if lnk_favicon:
            url_favicon     = lnk_favicon.get( 'href' )
            url_parsed      = urlparse( url_favicon )

            if url_parsed.netloc != '':
                return url_favicon
            else:
                return
        else:
            return