import logging
import re
import pkgutil
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options, Config
from mkdocs_link_embeds_plugin.opengraph import OpenGraph

LOG = logging.getLogger( "mkdocs.plugins." + __name__ )

# ------------------------------------------------------------------------------------------------------------------------------------------
#   define > default values
# ------------------------------------------------------------------------------------------------------------------------------------------

meta_def_name                   = "Untitled"
meta_def_desc                   = "No description"
meta_def_image                  = "https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/98179e23-ce03-4101-a858-56db0cd0e8f0"
meta_def_favicon                = "https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/b37da9c6-6f17-4c3f-9c94-c346a6f31bfa"
favicon_def_size                = 25

# ------------------------------------------------------------------------------------------------------------------------------------------
#   Link Embed Plugin
# ------------------------------------------------------------------------------------------------------------------------------------------

class LinkEmbedsPlugin( BasePlugin ):

    # ------------------------------------------------------------------------------------------------------------------------------------------
    #   Config Options
    # ------------------------------------------------------------------------------------------------------------------------------------------

    config_scheme = (
        ( "enabled",            config_options.Type( bool, default=True ) ),
        ( 'name_default',       config_options.Type( str, default=f'{meta_def_name}' ) ),
        ( 'desc_default',       config_options.Type( str, default=f'{meta_def_desc}' ) ),
        ( "favicon_disabled",   config_options.Type( bool, default=False ) ),
        ( 'favicon_default',    config_options.Type( str, default=f'{meta_def_favicon}' ) ),
        ( 'favicon_size',       config_options.Type( int, default=favicon_def_size ) ),
        ( "image_disabled",     config_options.Type( bool, default=False ) ),
        ( 'image_default',      config_options.Type( str, default=f'{meta_def_image}' ) ),
    )

    # ------------------------------------------------------------------------------------------------------------------------------------------
    #   Pattern / group regex
    #
    #   note:   to patch "embed" should work with ^embed$. regex tester reports it being correct, but does
    #           not work in script. replaced using \bembed\b until it can be investigated.
    # ------------------------------------------------------------------------------------------------------------------------------------------

    #CBLOCK_PATTERN             = re.compile( r"```embed$(?=[^`]*?\nurl:(?P<url>[^`\n]+))?(?=[^`]*?\nname:(?P<name>[^`\n]+))?(?=[^`]*?\nbanner:(?P<banner>[^`\n]+))?(?=[^`]*?\nimage:(?P<image>[^`\n]+))?(?=[^`]*?\ndesc:(?P<desc>[^`\n]+))?[^`]*?```")
    #CBLOCK_PATTERN             = re.compile( r"(?<=\n)\n```embed(?=[^`]*?\nurl:(?P<url>[^`\n]+))?(?=[^`]*?\nname:(?P<name>[^`\n]+))?(?=[^`]*?\nbanner:(?P<banner>[^`\n]+))?(?=[^`]*?\nimage:(?P<image>[^`\n]+))?(?=[^`]*?\ndesc:(?P<desc>[^`\n]+))?[^`]*?```")
    #CBLOCK_PATTERN             = re.compile( r"(?<=\n)\n```embed(?=[^`]*?\nurl:(?P<url>[^`\n]+))?(?=[^`]*?\nname:(?P<name>[^`\n]+))?(?=[^`]*?\nbanner:(?P<banner>[^`\n]+))?(?=[^`]*?\nfavicon:(?P<favicon>[^`\n]+))?(?=[^`]*?\nimage:(?P<image>[^`\n]+))?(?=[^`]*?\ndesc:(?P<desc>[^`\n]+))?[^`]*?```" )
    #CBLOCK_PATTERN             = re.compile( r"(?<=\n)\n```\bembed\b(?=[^`]*?\nurl:(?P<url>[^`\n]+))?(?=[^`]*?\nname:(?P<name>[^`\n]+))?(?=[^`]*?\nbanner:(?P<banner>[^`\n]+))?(?=[^`]*?\nfavicon:(?P<favicon>[^`\n]+))?(?=[^`]*?\nimage:(?P<image>[^`\n]+))?(?=[^`]*?\ndesc:(?P<desc>[^`\n]+))?[^`]*?```" )
    CBLOCK_PATTERN              = re.compile( r"(?<=\n)\n```\bembed\b(?=[^`]*?\nurl:(?P<url>[^`\n]+))?(?=[^`]*?\nname:(?P<name>[^`\n]+))?(?=[^`]*?\nbanner:(?P<banner>[^`\n]+))?(?=[^`]*?\nfavicon:(?P<favicon>[^`\n]+))?(?=[^`]*?\nfavicon_size:(?P<favicon_size>[^`\n]+))?(?=[^`]*?\nimage:(?P<image>[^`\n]+))?(?=[^`]*?\ndesc:(?P<desc>[^`\n]+))?[^`]*?```" )

    # ------------------------------------------------------------------------------------------------------------------------------------------
    #   Initialize
    # ------------------------------------------------------------------------------------------------------------------------------------------

    def __init__( self ):
        self.opengraph          = OpenGraph( )
        self.url_pattern        = re.compile( "^((http|https)?://)?(?P<host>[a-zA-Z0-9./?:@\\-_=#]+\\.[a-zA-Z]{2,6})[a-zA-Z0-9.&/?:@\\-_=#가-힇]*$" )
        self.templ_fallback     = None
        self.templ_view         = None

    # ------------------------------------------------------------------------------------------------------------------------------------------
    #   On Config
    # ------------------------------------------------------------------------------------------------------------------------------------------

    def on_config( self, config ):
        if not self.config.get( 'enabled' ):
            return config

        self.templ_view         = pkgutil.get_data( __name__, "resources/view.html" ).decode( 'utf-8' )
        self.templ_fallback     = pkgutil.get_data( __name__, "resources/fallback.html" ).decode( 'utf-8' )

        return config

    # ------------------------------------------------------------------------------------------------------------------------------------------
    #   On Page Markdown
    # ------------------------------------------------------------------------------------------------------------------------------------------

    def on_page_markdown( self, markdown, page, config, files ):
        if not self.config.get( 'enabled' ):
            return markdown

        converted_markdown          = ""
        idx                         = 0

        for site in self.CBLOCK_PATTERN.finditer( markdown ):
            start                   = site.start( )
            end                     = site.end( ) - 1

            input_url               = site.group( "url" )
            input_name              = site.group( "name" )
            input_desc              = site.group( "desc" )
            input_image             = site.group( "image" )
            input_favicon           = site.group( "favicon" )
            input_favicon_size      = site.group( "favicon_size" )

            lines                   = input_url.splitlines( )
            html_output             = ""
            
            for i in lines:
                i = i.replace( " ", "" )

                if i[ 0 ] == "-" or i[ 0 ] == "*":
                    i = i[ 1: ]

                try:
                    soup                    = self.opengraph.get_page( i )
                    html_view               = self.templ_view
                    link                    = i

                    # -----------------------------------------------------------------------------------------
                    #   Normal Template
                    #   fetch metadata for website (if available)
                    # -----------------------------------------------------------------------------------------

                    box_name                = self.opengraph.get_title( soup )
                    box_desc                = self.opengraph.get_description( soup )
                    box_image               = self.opengraph.get_image( soup )
                    box_favicon             = self.opengraph.get_favicon( soup )
                    box_favicon_size        = str( self.config[ 'favicon_size' ] )

                    # -----------------------------------------------------------------------------------------
                    #   Normal Template
                    #   check for user input values
                    # -----------------------------------------------------------------------------------------

                    if input_name:
                        box_name            = input_name.strip( )
                        box_name            = re.sub( "[\"\']", "", box_name )    # clean quotation marks
                    if input_desc:
                        box_desc            = input_desc.strip( )
                        box_desc            = re.sub( "[\"\']", "", box_desc )    # clean quotation marks
                    if input_image:
                        box_image           = input_image.strip( )
                    if input_favicon:
                        box_favicon         = input_favicon.strip( )
                    if input_favicon_size:
                        box_favicon_size    = str( input_favicon_size.strip( ) )

                    # -----------------------------------------------------------------------------------------
                    #   Normal Template
                    #   check for null values
                    # -----------------------------------------------------------------------------------------

                    if box_name is None:
                        if self.config[ 'name_default' ] and self.config[ 'name_default' ] != '':
                            box_name        = self.config[ 'name_default' ]
                        else:
                            box_name        = meta_def_name

                        box_name            = re.sub( "[\"\']", "", box_name )

                    if box_desc is None:
                        if self.config[ 'desc_default' ] and self.config[ 'desc_default' ] != '':
                            box_desc        = self.config[ 'desc_default' ]
                        else:
                            box_desc        = meta_def_desc

                        box_desc            = re.sub( "[\"\']", "", box_desc )

                    # -----------------------------------------------------------------------------------------
                    #   Object > Image
                    # -----------------------------------------------------------------------------------------

                    if box_image is None:
                        if self.config[ 'image_default' ] and self.config[ 'image_default' ] != '':
                            box_image       = self.config[ 'image_default' ]
                        else:
                            box_image       = meta_def_image

                    if ( box_image == 'false' ) or ( box_image is None ) or ( not box_image ) or ( self.config.get( 'image_disabled' ) ):
                        style_image         = "display:none;"
                    else:
                        style_image         = ""

                    # -----------------------------------------------------------------------------------------
                    #   Object > Fav Icon
                    # -----------------------------------------------------------------------------------------

                    if box_favicon is None:
                        if self.config[ 'favicon_default' ] and self.config[ 'favicon_default' ] != '':
                            box_favicon     = self.config[ 'favicon_default' ]
                        else:
                            box_favicon     = meta_def_favicon

                    if ( box_favicon == 'false' ) or ( box_favicon is None ) or ( not box_favicon ) or ( self.config.get( 'favicon_disabled' ) ):
                        style_favicon       = "display:none; padding-right: 0px;"
                    else:
                        style_favicon       = f"padding-right: 7px; width: {box_favicon_size}px"

                    # -----------------------------------------------------------------------------------------
                    #   build normal template
                    # -----------------------------------------------------------------------------------------

                    html_view           = html_view.replace( "{{ link }}", link )
                    html_view           = html_view.replace( "{{ image-url }}", box_image )
                    html_view           = html_view.replace( "{{ image-style }}", style_image )
                    html_view           = html_view.replace( "{{ name }}", box_name )
                    html_view           = html_view.replace( "{{ desc }}", box_desc )
                    html_view           = html_view.replace( "{{ favicon }}", box_favicon )
                    html_view           = html_view.replace( "{{ favicon-style }}", style_favicon )

                    html_output         += html_view

                # -----------------------------------------------------------------------------------------
                #   opengraph found invalid data
                # -----------------------------------------------------------------------------------------

                except:
                    url_match       = self.url_pattern.match( i )
                    
                    if url_match:
                        box_name    = url_match.group( 'host' )
                    else:
                        box_name    = "Invalid URL"

                    # -----------------------------------------------------------------------------------------
                    #   Default Template
                    #   fallback values
                    # -----------------------------------------------------------------------------------------

                    if box_name is None:
                        if self.config[ 'name_default' ] and self.config[ 'name_default' ] != '':
                            box_name    = self.config[ 'name_default' ]
                        else:
                            box_name    = meta_def_name

                    if self.config[ 'desc_default' ] and self.config[ 'desc_default' ] != '':
                        box_desc        = self.config[ 'desc_default' ]
                    else:
                        box_desc        = meta_def_desc

                    if self.config[ 'image_default' ] and self.config[ 'image_default' ] != '':
                        box_image       = self.config[ 'image_default' ]
                    else:
                        box_image       = meta_def_image

                    if self.config[ 'favicon_default' ] and self.config[ 'favicon_default' ] != '':
                        box_favicon     = self.config[ 'favicon_default' ]
                    else:
                        box_favicon     = meta_def_favicon

                    # -----------------------------------------------------------------------------------------
                    #   Default Template
                    #   check for user input values
                    # -----------------------------------------------------------------------------------------

                    if input_name:
                        box_name            = input_name
                    if input_desc:
                        box_desc            = input_desc
                    if input_image:
                        box_image           = input_image
                    if input_favicon:
                        box_favicon         = input_favicon
                    if input_favicon_size:
                        box_favicon_size    = input_favicon_size

                    # -----------------------------------------------------------------------------------------
                    #   build fallback template
                    # -----------------------------------------------------------------------------------------

                    html_fallback   = self.templ_fallback
                    html_fallback   = html_fallback.replace( "{{ link }}", i )
                    html_fallback   = html_fallback.replace( "{{ image-url }}", box_image )
                    html_fallback   = html_fallback.replace( "{{ name }}", box_name )
                    html_fallback   = html_fallback.replace( "{{ desc }}", box_desc )
                    html_fallback   = html_fallback.replace( "{{ favicon }}", box_favicon )

                    html_output     += html_fallback

            converted_markdown      += markdown[ idx:start ]
            converted_markdown      += html_output
            idx                     = end + 1

        converted_markdown += markdown[ idx:len( markdown ) ]

        return converted_markdown