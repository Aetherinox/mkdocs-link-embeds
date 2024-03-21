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
meta_def_favicon                = "https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/13a151b1-d7f9-4e27-909b-a26986ab0954"
meta_def_favicon_size           = 25
target_def_id                   = "new"
accent_def                      = "#ffffff1a"

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
        ( 'favicon_size',       config_options.Type( int, default=meta_def_favicon_size ) ),
        ( 'target',             config_options.Type( str, default=f'{target_def_id}' ) ),
        ( 'accent',             config_options.Type( str, default=f'{accent_def}' ) ),
    )

    # ------------------------------------------------------------------------------------------------------------------------------------------
    #   Pattern / group regex
    #
    #   note:   to patch "embed" should work with ^embed$. regex tester reports it being correct, but does
    #           not work in script. replaced using \bembed\b until it can be investigated.
    # ------------------------------------------------------------------------------------------------------------------------------------------

    #CBLOCK_PATTERN             = re.compile( r"(?<=\n)\n```\bembed\b(?=[^`]*?\nurl:(?P<url>[^`\n]+))?(?=[^`]*?\nname:(?P<name>[^`\n]+))?(?=[^`]*?\nbanner:(?P<banner>[^`\n]+))?(?=[^`]*?\nfavicon:(?P<favicon>[^`\n]+))?(?=[^`]*?\nfavicon_size:(?P<favicon_size>[^`\n]+))?(?=[^`]*?\nimage:(?P<image>[^`\n]+))?(?=[^`]*?\ndesc:(?P<desc>[^`\n]+))?[^`]*?```" )
    #CBLOCK_PATTERN             = re.compile( r"(?<=\n)\n```\bembed\b(?=[^`]*?\nurl:[\s+](?P<url>[^`\n]+))?(?=[^`]*?\nname:[\s+](?P<name>[^`\n]+))?(?=[^`]*?\nbanner:[\s+](?P<banner>[^`\n]+))?(?=[^`]*?\nfavicon:[\s+](?P<favicon>[^`\n]+))?(?=[^`]*?\nfavicon_size:[\s+](?P<favicon_size>[^`\n]+))?(?=[^`]*?\ntarget:[\s+](?P<target>[^`\n]+))?(?=[^`]*?\nimage:[\s+](?P<image>[^`\n]+))?(?=[^`]*?\ndesc:[\s+](?P<desc>[^`\n]+))?[^`]*?```" ) # replace \s with [^\S\n]++
    CBLOCK_PATTERN              = re.compile( r"(?<=\n)\n```\bembed\b(?=[^`]*?\nurl:? +(?P<url>[^`\n]*))?(?=[^`]*?\nname:? +(?P<name>[^`\n]*))?(?=[^`]*?\nimage:? +(?P<image>[^`\n]*))?(?=[^`]*?\nfavicon:? +(?P<favicon>[^`\n]*))?(?=[^`]*?\nfavicon_size:? +(?P<favicon_size>[^`\n]*))?(?=[^`]*?\ntarget:? +(?P<target>[^`\n]*))?(?=[^`]*?\naccent:? +(?P<accent>[^`\n]*))?(?=[^`]*?\ndesc:? +(?P<desc>[^`\n]*))?[^`]*?```" )

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
            else:
                box_name            = meta_def_name

            if self.config[ 'desc_default' ] and self.config[ 'desc_default' ] != '':
                box_desc            = self.config[ 'desc_default' ]
            else:
                box_desc            = meta_def_desc

            if self.config[ 'image_default' ] and self.config[ 'image_default' ] != '':
                box_image           = self.config[ 'image_default' ]
            else:
                box_image           = meta_def_image

            if self.config[ 'favicon_default' ] and self.config[ 'favicon_default' ] != '':
                box_favicon         = self.config[ 'favicon_default' ]
            else:
                box_favicon         = meta_def_favicon

            if self.config[ 'favicon_size' ] and self.config[ 'favicon_size' ] != '':
                box_favicon_size    = self.config[ 'favicon_size' ]
            else:
                box_favicon_size    = meta_def_favicon_size

            if self.config[ 'target' ] and self.config[ 'target' ] != '':
                box_target          = self.config[ 'target' ]
            else:
                box_target          = target_def_id

            if self.config[ 'accent' ] and self.config[ 'accent' ] != '':
                box_accent          = self.config[ 'accent' ]
            else:
                box_accent          = accent_def

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
            input_accent            = self.clean_input( site.group( "accent" ) )

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

                box_name                = self.fetchurl.get_title( soup, box_name )
                box_desc                = self.fetchurl.get_description( soup, box_desc, link )
                box_image               = self.fetchurl.get_image( soup, box_image )
                box_favicon             = not self.config.get( 'favicon_disabled' ) and self.fetchurl.get_favicon( soup, input_url, box_favicon, input_favicon ) or ""
                box_favicon_size        = str( self.config[ 'favicon_size' ] )
                box_target              = str( self.config[ 'target' ] )

                # -----------------------------------------------------------------------------------------
                #   Handle > Input Override > Name
                # -----------------------------------------------------------------------------------------
    
                if input_name:
                    box_name        = input_name

                # -----------------------------------------------------------------------------------------
                #   Handle > Input Override > Desc
                # -----------------------------------------------------------------------------------------

                if input_desc:
                    box_desc            = input_desc

                # -----------------------------------------------------------------------------------------
                #   Handle > Input Override > Image
                # -----------------------------------------------------------------------------------------

                if input_image:
                    box_image           = input_image

                if ( box_image == 'false' ) or ( box_image is None ) or ( not box_image ) or ( self.config.get( 'image_disabled' ) ):
                    style_image         = "display:none;"
                else:
                    style_image         = ""

                # -----------------------------------------------------------------------------------------
                #   Handle > Input Override > Favicon
                # -----------------------------------------------------------------------------------------

                if input_favicon:
                    box_favicon         = input_favicon

                if ( box_favicon == 'false' ) or ( box_favicon is None ) or ( not box_favicon ) or ( self.config.get( 'favicon_disabled' ) ):
                    style_favicon       = "display:none; padding-right: 0px;"
                else:
                    style_favicon       = f"padding-right: 7px; width: {box_favicon_size}px"

                # -----------------------------------------------------------------------------------------
                #   Handle > Input Override > Favicon Size
                # -----------------------------------------------------------------------------------------

                if input_favicon_size:
                    box_favicon_size    = input_favicon_size

                # -----------------------------------------------------------------------------------------
                #   Handle > Input Override > Target
                # -----------------------------------------------------------------------------------------

                if input_target:
                    box_target          = input_target

                if box_target == "_self" or box_target == "self" or box_target == "same" or box_target == "current":
                    box_target          = "_self"
                elif box_target == "_blank" or box_target == "blank" or box_target == "new" or box_target == "window" or box_target == "open":
                    box_target          = "_blank"
                else:
                    box_target          = self.config[ 'target' ]

                # -----------------------------------------------------------------------------------------
                #   Handle > Input Override > Accent
                # -----------------------------------------------------------------------------------------

                if input_accent:
                    box_accent      = input_accent

                #   remove # from beginning of string and add our own in case the user supplied it.
                box_accent          = ( box_accent[1:] if box_accent.startswith( '#' ) else box_accent )

                if ( box_accent == 'false' ) or ( box_accent is None ) or ( not box_accent ):
                    box_accent       = f"border: 2px solid #{accent_def}"
                else:
                    box_accent      = f"border: 2px solid #{box_accent}"

                # -----------------------------------------------------------------------------------------
                #   build template
                # -----------------------------------------------------------------------------------------

                html_view           = html_view.replace( "{{ link }}", link )
                html_view           = html_view.replace( "{{ image-url }}", box_image )
                html_view           = html_view.replace( "{{ image-style }}", style_image )
                html_view           = html_view.replace( "{{ name }}", box_name )
                html_view           = html_view.replace( "{{ desc }}", box_desc )
                html_view           = html_view.replace( "{{ favicon }}", box_favicon )
                html_view           = html_view.replace( "{{ favicon-style }}", style_favicon )
                html_view           = html_view.replace( "{{ target }}", box_target )
                html_view           = html_view.replace( "{{ accent }}", box_accent )

                html_output         += html_view

            converted_markdown      += markdown[ idx:start ]
            converted_markdown      += html_output
            idx                     = end + 1

        converted_markdown += markdown[ idx:len( markdown ) ]

        return converted_markdown