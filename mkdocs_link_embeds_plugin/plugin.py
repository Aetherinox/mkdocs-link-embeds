import logging
import re
import pkgutil
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options, Config
from mkdocs_link_embeds_plugin.fetchurl import FetchURL

LOG = logging.getLogger( "mkdocs.plugins." + __name__ )

# ------------------------------------------------------------------------------------------------------------------------------------------
#   define > default values
# ------------------------------------------------------------------------------------------------------------------------------------------

meta_def_name                   = "Untitled"
meta_def_desc                   = "No description"
meta_def_image                  = "https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/98179e23-ce03-4101-a858-56db0cd0e8f0"
meta_def_favicon                = "https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/b37da9c6-6f17-4c3f-9c94-c346a6f31bfa"
favicon_def_size                = 25
target_def_id                   = "new"

# ------------------------------------------------------------------------------------------------------------------------------------------
#   Link Embed Plugin
# ------------------------------------------------------------------------------------------------------------------------------------------

class LinkEmbedsPlugin( BasePlugin ):

    # ------------------------------------------------------------------------------------------------------------------------------------------
    #   Clean Input Values
    #
    #   @note:      as ov v0.1.7, whitespace cleanup should not be needed anymore.
    # ------------------------------------------------------------------------------------------------------------------------------------------

    def clean_input( self, val ):
        if not val or val is None:
            return val
    
        val     = val.strip( )
        val     = re.sub( "[\"\']", "", val )

        return val

    # ------------------------------------------------------------------------------------------------------------------------------------------
    #   Config Options
    # ------------------------------------------------------------------------------------------------------------------------------------------

    config_scheme = (
        ( "enabled",            config_options.Type( bool, default=True ) ),
        ( 'name_default',       config_options.Type( str, default=f'{meta_def_name}' ) ),
        ( 'desc_default',       config_options.Type( str, default=f'{meta_def_desc}' ) ),
        ( "image_disabled",     config_options.Type( bool, default=False ) ),
        ( 'image_default',      config_options.Type( str, default=f'{meta_def_image}' ) ),
        ( "favicon_disabled",   config_options.Type( bool, default=False ) ),
        ( 'favicon_default',    config_options.Type( str, default=f'{meta_def_favicon}' ) ),
        ( 'favicon_size',       config_options.Type( int, default=favicon_def_size ) ),
        ( 'target',             config_options.Type( str, default=f'{target_def_id}' ) ),
    )

    # ------------------------------------------------------------------------------------------------------------------------------------------
    #   Pattern / group regex
    #
    #   note:   to patch "embed" should work with ^embed$. regex tester reports it being correct, but does
    #           not work in script. replaced using \bembed\b until it can be investigated.
    # ------------------------------------------------------------------------------------------------------------------------------------------

    #CBLOCK_PATTERN             = re.compile( r"(?<=\n)\n```\bembed\b(?=[^`]*?\nurl:(?P<url>[^`\n]+))?(?=[^`]*?\nname:(?P<name>[^`\n]+))?(?=[^`]*?\nbanner:(?P<banner>[^`\n]+))?(?=[^`]*?\nfavicon:(?P<favicon>[^`\n]+))?(?=[^`]*?\nfavicon_size:(?P<favicon_size>[^`\n]+))?(?=[^`]*?\nimage:(?P<image>[^`\n]+))?(?=[^`]*?\ndesc:(?P<desc>[^`\n]+))?[^`]*?```" )
    CBLOCK_PATTERN              = re.compile( r"(?<=\n)\n```\bembed\b(?=[^`]*?\nurl:[\s+](?P<url>[^`\n]+))?(?=[^`]*?\nname:[\s+](?P<name>[^`\n]+))?(?=[^`]*?\nbanner:[\s+](?P<banner>[^`\n]+))?(?=[^`]*?\nfavicon:[\s+](?P<favicon>[^`\n]+))?(?=[^`]*?\nfavicon_size:[\s+](?P<favicon_size>[^`\n]+))?(?=[^`]*?\ntarget:[\s+](?P<target>[^`\n]+))?(?=[^`]*?\nimage:[\s+](?P<image>[^`\n]+))?(?=[^`]*?\ndesc:[\s+](?P<desc>[^`\n]+))?[^`]*?```" )

    # ------------------------------------------------------------------------------------------------------------------------------------------
    #   Initialize
    # ------------------------------------------------------------------------------------------------------------------------------------------

    def __init__( self ):
        self.fetchurl           = FetchURL( )
        self.url_pattern        = re.compile( "^((http|https)?://)?(?P<host>[a-zA-Z0-9./?:@\\-_=#]+\\.[a-zA-Z]{2,6})[a-zA-Z0-9.&/?:@\\-_=#가-힇]*$" )
        self.templ_view         = None

    # ------------------------------------------------------------------------------------------------------------------------------------------
    #   On Config
    # ------------------------------------------------------------------------------------------------------------------------------------------

    def on_config( self, config ):
        if not self.config.get( 'enabled' ):
            return config

        self.templ_view         = pkgutil.get_data( __name__, "resources/view.html" ).decode( 'utf-8' )

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

            # -----------------------------------------------------------------------------------------
            #   set defaults
            # -----------------------------------------------------------------------------------------

            if self.config[ 'name_default' ] and self.config[ 'name_default' ] != '':
                box_name            = self.config[ 'name_default' ]

            if self.config[ 'desc_default' ] and self.config[ 'desc_default' ] != '':
                box_desc            = self.config[ 'desc_default' ]

            if self.config[ 'image_default' ] and self.config[ 'image_default' ] != '':
                box_image           = self.config[ 'image_default' ]

            if self.config[ 'favicon_default' ] and self.config[ 'favicon_default' ] != '':
                box_favicon         = self.config[ 'favicon_default' ]

            if self.config[ 'favicon_size' ] and self.config[ 'favicon_size' ] != '':
                box_favicon_size    = self.config[ 'favicon_size' ]

            if self.config[ 'target' ] and self.config[ 'target' ] != '':
                box_target          = self.config[ 'target' ]

            # -----------------------------------------------------------------------------------------
            #   pull any user inputs provided
            # -----------------------------------------------------------------------------------------

            input_url               = self.clean_input( site.group( "url" ) )
            input_name              = self.clean_input( site.group( "name" ) )
            input_desc              = self.clean_input( site.group( "desc" ) )
            input_image             = self.clean_input( site.group( "image" ) )
            input_favicon           = self.clean_input( site.group( "favicon" ) )
            input_favicon_size      = self.clean_input( site.group( "favicon_size" ) )
            input_target            = self.clean_input( site.group( "target" ) )

            lines                   = input_url.splitlines( )
            html_output             = ""
            
            for i in lines:
                i = i.replace( " ", "" )

                if i[ 0 ] == "-" or i[ 0 ] == "*":
                    i = i[ 1: ]

                soup                    = self.fetchurl.get_page( i )
                html_view               = self.templ_view
                link                    = i

                # -----------------------------------------------------------------------------------------
                #   Normal Template
                #   fetch metadata for website (if available)
                # -----------------------------------------------------------------------------------------

                box_name                = self.fetchurl.get_title( soup )
                box_desc                = self.fetchurl.get_description( soup )
                box_image               = self.fetchurl.get_image( soup )
                box_favicon             = self.fetchurl.get_favicon( soup )
                box_favicon_size        = str( self.config[ 'favicon_size' ] )
                box_target              = str( self.config[ 'target' ] )

                # -----------------------------------------------------------------------------------------
                #   Normal Template
                #   check for null values
                # -----------------------------------------------------------------------------------------

                if box_name is None:
                    if self.config[ 'name_default' ]:
                        box_name        = self.config[ 'name_default' ]
                    else:
                        box_name        = meta_def_name

                    box_name            = re.sub( "[\"\']", "", box_name )

                if box_desc is None:
                    if self.config[ 'desc_default' ]:
                        box_desc        = self.config[ 'desc_default' ]
                    else:
                        box_desc        = meta_def_desc

                    box_desc            = re.sub( "[\"\']", "", box_desc )

                # -----------------------------------------------------------------------------------------
                #   Object > Image
                # -----------------------------------------------------------------------------------------

                if box_image is None:
                    if self.config[ 'image_default' ]:
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
                    if self.config[ 'favicon_default' ]:
                        box_favicon     = self.config[ 'favicon_default' ]
                    else:
                        box_favicon     = meta_def_favicon

                if ( box_favicon == 'false' ) or ( box_favicon is None ) or ( not box_favicon ) or ( self.config.get( 'favicon_disabled' ) ):
                    style_favicon       = "display:none; padding-right: 0px;"
                else:
                    style_favicon       = f"padding-right: 7px; width: {box_favicon_size}px"

                # -----------------------------------------------------------------------------------------
                #   Object > Target = None
                # -----------------------------------------------------------------------------------------

                if box_target is None:
                    if self.config[ 'target' ]:
                        box_target      = self.config[ 'target' ]
                    else:
                        box_target      = meta_def_favicon

                # -----------------------------------------------------------------------------------------
                #   Object > Target = Define Keywords
                # -----------------------------------------------------------------------------------------

                if box_target == "_self" or box_target == "self" or box_target == "same" or box_target == "current":
                    box_target      = "_self"
                elif box_target == "_blank" or box_target == "blank" or box_target == "new" or box_target == "window" or box_target == "open":
                    box_target      = "_blank"
                else:
                    box_target      = self.config[ 'target' ]

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
                html_view           = html_view.replace( "{{ target }}", box_target )

                html_output         += html_view

            converted_markdown      += markdown[ idx:start ]
            converted_markdown      += html_output
            idx                     = end + 1

        converted_markdown += markdown[ idx:len( markdown ) ]

        return converted_markdown