import logging
import re
import pkgutil
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options, Config
from mkdocs_link_embeds_plugin.opengraph import OpenGraph

LOG = logging.getLogger( "mkdocs.plugins." + __name__ )

# ----------------------------------------------
#   define > default values
# ----------------------------------------------

meta_def_image                  = "https://user-images.githubusercontent.com/16578570/61557132-bbc14300-aa63-11e9-9a6c-188c880698ec.png"
meta_def_name                   = "Untitled"
meta_def_desc                   = "No description"

# ----------------------------------------------
#   Link Embed Plugin
# ----------------------------------------------

class LinkEmbedsPlugin( BasePlugin ):

    # ----------------------------------------------
    #   Config Options
    # ----------------------------------------------

    config_scheme = (
        ( "enabled", config_options.Type( bool, default=True ) ),
        ( 'default_image',  config_options.Type( str, default=f'{meta_def_image}' ) ),
        ( 'default_name',   config_options.Type( str, default=f'{meta_def_name}' ) ),
        ( 'default_desc',   config_options.Type( str, default=f'{meta_def_desc}' ) ),
    )

    # ----------------------------------------------
    #   Pattern / group regex
    # ----------------------------------------------

    CBLOCK_PATTERN              = re.compile( r"```embed(?=[^`]*?\nurl:(?P<url>[^`\n]+))?(?=[^`]*?\nname:(?P<name>[^`\n]+))?(?=[^`]*?\nbanner:(?P<banner>[^`\n]+))?(?=[^`]*?\nimage:(?P<image>[^`\n]+))?(?=[^`]*?\ndesc:(?P<desc>[^`\n]+))?[^`]*?```")

    def __init__( self ):
        self.opengraph          = OpenGraph( )
        self.url_pattern        = re.compile( "^((http|https)?://)?(?P<host>[a-zA-Z0-9./?:@\\-_=#]+\\.[a-zA-Z]{2,6})[a-zA-Z0-9.&/?:@\\-_=#가-힇]*$" )
        self.templ_fallback     = None
        self.templ_view         = None

    def on_config( self, config ):
        if not self.config.get( 'enabled' ):
            return config

        self.templ_view         = pkgutil.get_data( __name__, "resources/view.html" ).decode( 'utf-8' )
        self.templ_fallback     = pkgutil.get_data( __name__, "resources/fallback.html" ).decode( 'utf-8' )

        return config

    def on_page_markdown( self, markdown, page, config, files ):
        if not self.config.get( 'enabled' ):
            return markdown

        converted_markdown      = ""
        idx                     = 0

        for site in self.CBLOCK_PATTERN.finditer( markdown ):
            start               = site.start( )
            end                 = site.end( ) - 1

            input_url           = site.group( "url" )
            input_name          = site.group( "name" )
            input_desc          = site.group( "desc" )
            input_image         = site.group( "image" )

            lines               = input_url.splitlines( )
            html_output         = ""
            
            for i in lines:
                i = i.replace( " ", "" )

                if i[ 0 ] == "-" or i[ 0 ] == "*":
                    i = i[ 1: ]

                try:
                    soup                = self.opengraph.get_page( i )
                    html_view           = self.templ_view
                    link                = i

                    # ----------------------------------------------
                    #   Normal Template
                    #   fetch metadata for website (if available)
                    # ----------------------------------------------

                    box_name            = self.opengraph.get_og_title( soup )
                    box_desc            = self.opengraph.get_og_description( soup )
                    box_image           = self.opengraph.get_og_image( soup )

                    # ----------------------------------------------
                    #   Normal Template
                    #   check for user input values
                    # ----------------------------------------------

                    if input_name:
                        box_name        = re.sub( "[\"\']", "", input_name )
                    if input_desc:
                        box_desc        = re.sub( "[\"\']", "", input_desc )
                    if input_image:
                        box_image       = input_image

                    # ----------------------------------------------
                    #   Normal Template
                    #   check for null values
                    # ----------------------------------------------

                    if box_name is None:
                        if self.config[ 'default_name' ] and self.config[ 'default_name' ] != '':
                            box_name        = self.config[ 'default_name' ]
                        else:
                            box_name        = meta_def_name

                        box_name            = re.sub( "[\"\']", "", box_name )

                    if box_desc is None:
                        if self.config[ 'default_desc' ] and self.config[ 'default_desc' ] != '':
                            box_desc        = self.config[ 'default_desc' ]
                        else:
                            box_desc        = meta_def_desc

                        box_desc            = re.sub( "[\"\']", "", box_desc )

                    if box_image is None:
                        if self.config[ 'default_image' ] and self.config[ 'default_image' ] != '':
                            box_image       = self.config[ 'default_image' ]
                        else:
                            box_image       = meta_def_image

                    # ----------------------------------------------
                    #   build normal template
                    # ----------------------------------------------

                    html_view           = html_view.replace( "{{ link }}", link )
                    html_view           = html_view.replace( "{{ image-url }}", box_image )
                    html_view           = html_view.replace( "{{ name }}", box_name )
                    html_view           = html_view.replace( "{{ desc }}", box_desc )
                    html_output         += html_view

                # ----------------------------------------------
                #   opengraph found invalid data
                # ----------------------------------------------

                except:
                    url_match       = self.url_pattern.match( i )
                    
                    if url_match:
                        box_name    = url_match.group( 'host' )
                    else:
                        box_name    = "Invalid URL"

                    # ----------------------------------------------
                    #   Default Template
                    #   fallback values
                    # ----------------------------------------------

                    if box_name is None:
                        if self.config[ 'default_name' ] and self.config[ 'default_name' ] != '':
                            box_name        = self.config[ 'default_name' ]
                        else:
                            box_name        = meta_def_name

                    if self.config[ 'default_desc' ] and self.config[ 'default_desc' ] != '':
                        box_desc        = self.config[ 'default_desc' ]
                    else:
                        box_desc        = meta_def_desc

                    if self.config[ 'default_image' ] and self.config[ 'default_image' ] != '':
                        box_image       = self.config[ 'default_image' ]
                    else:
                        box_image       = meta_def_image

                    # ----------------------------------------------
                    #   Default Template
                    #   check for user input values
                    # ----------------------------------------------

                    if input_name:
                        box_name    = input_name
                    if input_desc:
                        box_desc    = input_desc
                    if input_image:
                        box_image   = input_image

                    # ----------------------------------------------
                    #   build fallback template
                    # ----------------------------------------------

                    html_fallback   = self.templ_fallback
                    html_fallback   = html_fallback.replace( "{{ link }}", i )
                    html_fallback   = html_fallback.replace( "{{ image-url }}", box_image )
                    html_fallback   = html_fallback.replace( "{{ name }}", box_name )
                    html_fallback   = html_fallback.replace( "{{ desc }}", box_desc )

                    html_output     += html_fallback

            converted_markdown      += markdown[ idx:start ]
            converted_markdown      += html_output
            idx                     = end + 1

        converted_markdown += markdown[ idx:len( markdown ) ]

        return converted_markdown