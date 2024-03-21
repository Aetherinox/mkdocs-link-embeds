import re
import urllib.request
import requests

from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

class FetchURL:

    # -----------------------------------------------------------------------------------------
    #   Initialize
    # -----------------------------------------------------------------------------------------

    def __init__( self ):
        self.html_parser    = 'html.parser'
        self.encoding       = "utf-8"
        self.agent          = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
        pass

    # -----------------------------------------------------------------------------------------
    #   Get Page
    #   URLs without data should be handled in the same fashion as properly propogated sites
    #   with valid metadata. 
    # -----------------------------------------------------------------------------------------

    def get_page( self, url ):
        try:
            opener              = urllib.request.build_opener( )
            opener.addheaders   = [('User-agent', 'Mozilla/5.0')]
            response            = opener.open( url )
        except:
            response            = ""

        try:
            encoding            = response.info( ).get_param( 'charset' )
            soup                = BeautifulSoup( response, self.html_parser, from_encoding=encoding )
        except:
            soup                = BeautifulSoup( response, self.html_parser )
            soup.prettify       ( "latin-1" )

        return soup

    # -----------------------------------------------------------------------------------------
    #   Get > Title
    # -----------------------------------------------------------------------------------------

    def get_title( self, soup, title ):
        if soup.findAll( "meta", property="og:title" ):
            return soup.find( "meta", property="og:title")["content"]
        elif soup.findAll( 'title' ):
            return soup.find(' title' )
        else:
            return title

    # -----------------------------------------------------------------------------------------
    #   Get > Description
    # -----------------------------------------------------------------------------------------

    def get_description( self, soup, desc, url ):
        if soup.findAll( "meta", property="og:description" ):
            return soup.find( "meta", property="og:description")["content"]
        elif soup.findAll( 'meta', attrs={'name': 'description'} ):
            return soup.find( 'meta', attrs={ 'name': 'description' } )["content"]
        else:
            return desc

    # -----------------------------------------------------------------------------------------
    #   Get > Name
    # -----------------------------------------------------------------------------------------

    def get_site_name( self, soup, name ):
        if soup.findAll( "meta", property="og:site_name" ):
            return soup.find( "meta", property="og:site_name")["content"]
        elif soup.findAll( 'title' ):
            return soup.find(' title' )
        else:
            return name

    # -----------------------------------------------------------------------------------------
    #   Get > Image
    # -----------------------------------------------------------------------------------------

    def get_image( self, soup, image ):
        if soup.findAll( "meta", property="og:image" ):
            return soup.find( "meta", property="og:image")["content"]
        elif soup.findAll( "meta", property="twitter:image" ):
            return soup.find( "meta", property="twitter:image")["content"]
        else:
            return image

    # -----------------------------------------------------------------------------------------
    #   Get > Fav Icon
    #
    #   this is a very "step-by-step" manner of checking for fav icons. Just because there's
    #   so many ways that a favicon can be added.
    # -----------------------------------------------------------------------------------------

    def get_favicon( self, soup, url, favicon, input_favicon ):

        if input_favicon:
            return input_favicon

        lnk_favicon         = soup.find( 'link', rel='icon' ) or soup.find( 'link', rel='shortcut icon' )
        pattern             = r"^(?P<scheme>[^:\/?#]+):(?:\/\/)?(?:(?:(?P<login>[^:]+)(?::(?P<password>[^@]+)?)?@)?(?P<host>[^@\/?#:]*)(?::(?P<port>\d+)?)?)?(?P<path>[^?#]*)(?:\?(?P<query>[^#]*))?(?:#(?P<fragment>.*))?"

        if lnk_favicon:
            url_favicon     = lnk_favicon.get( 'href' )
            url_parsed      = urlparse( url_favicon )

            if url_parsed.netloc != '':
                return url_favicon
            else:
                match               = re.match( pattern, url )

                url_http            = match.group( "scheme" ) or "https"

                url_host            = ( match.group( "host" )[1:] if match.group( "host" ).startswith( '/' ) else match.group( "host" ) )   #   remove forward slash if 1st char
                url_host            = url_host.rstrip( '//' ) # remove last slash

                url_path            = ( match.group( "path" )[1:] if match.group( "path" ).startswith( '/' ) else match.group( "path" ) )   #   remove forward slash if 1st char
                url_path            = url_path.rstrip( '//' ) # remove last slash

                url_icon_local      = ( url_favicon[1:] if url_favicon.startswith('/') else url_favicon )   #   remove forward slash from local icon path if found
                domain              = url_http + "://" + url_host                            #   https://domain.com

                if domain and url_icon_local:
                    url_icon_local      = domain + "/" + url_icon_local     # create https://domain.com/ favicon.png
                    response            = requests.get( url_icon_local, headers=self.agent, timeout=( 1, 1 ) )
                    bSuccess            = False
                    
                    if response.status_code == 404:
                        bSuccess = False
                    else:
                        bSuccess = True

                    if not bSuccess:
                        domain          = url_http + "://" + url_host + "/" + url_path       # add /path/ to end of domain
                        url_icon_local  = domain + "/" + url_favicon

                        response        = requests.get( url_icon_local, headers=self.agent, timeout=( 1, 1 ) )

                        if response.status_code == 404:
                            bSuccess = False
                        else:
                            bSuccess = True

                    if bSuccess:
                        return url_icon_local
                    else:
                        return favicon

                    return favicon
                else:
                    return favicon
        else:
            return favicon