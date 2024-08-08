import os
import logging
import re
import pkgutil
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options, Config
from mkdocs_link_embeds_plugin.fetchurl import FetchURL
os.system("")

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
#   Color ASCII
# ------------------------------------------------------------------------------------------------------------------------------------------

class clr():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    GREY = '\033[90m'

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
    #   Truncate string
    # ------------------------------------------------------------------------------------------------------------------------------------------

    def truncate( self, str, limit ):
        truncated = re.search(fr'(.{{0,{limit}}})(?!\w)', str).group(1)

        if len(truncated) < len(str):
            truncated += "..."

        return truncated

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
        ( "verbose",            config_options.Type( bool, default=False ) ),
    )

    # ------------------------------------------------------------------------------------------------------------------------------------------
    #   Pattern / group regex
    #
    #   note:   to patch "embed" should work with ^embed$. regex tester reports it being correct, but does
    #           not work in script. replaced using \bembed\b until it can be investigated.
    # ------------------------------------------------------------------------------------------------------------------------------------------

    #CBLOCK_PATTERN         = re.compile( r"(?<=\n)\n```\bembed\b(?=[^`]*?\nurl:(?P<url>[^`\n]+))?(?=[^`]*?\nname:(?P<name>[^`\n]+))?(?=[^`]*?\nbanner:(?P<banner>[^`\n]+))?(?=[^`]*?\nfavicon:(?P<favicon>[^`\n]+))?(?=[^`]*?\nfavicon_size:(?P<favicon_size>[^`\n]+))?(?=[^`]*?\nimage:(?P<image>[^`\n]+))?(?=[^`]*?\ndesc:(?P<desc>[^`\n]+))?[^`]*?```" )
    #CBLOCK_PATTERN         = re.compile( r"(?<=\n)\n```\bembed\b(?=[^`]*?\nurl:[\s+](?P<url>[^`\n]+))?(?=[^`]*?\nname:[\s+](?P<name>[^`\n]+))?(?=[^`]*?\nbanner:[\s+](?P<banner>[^`\n]+))?(?=[^`]*?\nfavicon:[\s+](?P<favicon>[^`\n]+))?(?=[^`]*?\nfavicon_size:[\s+](?P<favicon_size>[^`\n]+))?(?=[^`]*?\ntarget:[\s+](?P<target>[^`\n]+))?(?=[^`]*?\nimage:[\s+](?P<image>[^`\n]+))?(?=[^`]*?\ndesc:[\s+](?P<desc>[^`\n]+))?[^`]*?```" ) # replace \s with [^\S\n]++
    CBLOCK_PATTERN          = re.compile( r"(?<=\n)\n```\bembed\b(?=[^`]*?\nurl:? +(?P<url>[^`\n]*))?(?=[^`]*?\nname:? +(?P<name>[^`\n]*))?(?=[^`]*?\nimage:? +(?P<image>[^`\n]*))?(?=[^`]*?\nfavicon:? +(?P<favicon>[^`\n]*))?(?=[^`]*?\nfavicon_size:? +(?P<favicon_size>[^`\n]*))?(?=[^`]*?\ntarget:? +(?P<target>[^`\n]*))?(?=[^`]*?\naccent:? +(?P<accent>[^`\n]*))?(?=[^`]*?\ndesc:? +(?P<desc>[^`\n]*))?[^`]*?```" )

    # ------------------------------------------------------------------------------------------------------------------------------------------
    #   Initialize
    # ------------------------------------------------------------------------------------------------------------------------------------------

    def __init__( self ):
        self.fetchurl       = FetchURL( )
        self.url_pattern    = re.compile( "^((http|https)?://)?(?P<host>[a-zA-Z0-9./?:@\\-_=#]+\\.[a-zA-Z]{2,6})[a-zA-Z0-9.&/?:@\\-_=#가-힇]*$" )
        self.templ_view     = None

    # ------------------------------------------------------------------------------------------------------------------------------------------
    #   On Config
    # ------------------------------------------------------------------------------------------------------------------------------------------

    def on_config( self, config: config_options.Config, **kwargs ):
        if not self.config.get( 'enabled' ):
            return config

        self.fetchurl       = FetchURL( config=self.config )
        self.templ_view     = pkgutil.get_data( __name__, "resources/view.html" ).decode( 'utf-8' )

        return config

    # ------------------------------------------------------------------------------------------------------------------------------------------
    #   On Page Markdown
    #
    #   @ref    : https://www.mkdocs.org/dev-guide/plugins/
    # ------------------------------------------------------------------------------------------------------------------------------------------

    def on_page_markdown( self, markdown, page, config, files ):
    
        if not self.config.get( 'enabled' ):
            return markdown

        converted_markdown  = []
        markdown_output     = ""
        idx                 = 0
        total               = sum(1 for _ in self.CBLOCK_PATTERN.finditer( markdown ))
        count_now           = 0

        for site in self.CBLOCK_PATTERN.finditer( markdown ):
            start           = site.start( )
            end             = site.end( ) - 1
            count_now       += 1

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
            html_output             = []

            for i in lines:
                i = i.replace( " ", "" )

                if i[ 0 ] == "-" or i[ 0 ] == "*":
                    i = i[ 1: ]

                # -----------------------------------------------------------------------------------------
                #   optimize > do not execute get_page unless any of the input parameters are missing
                # -----------------------------------------------------------------------------------------

                if not input_name or not input_desc or not input_image or not input_favicon:
                    soup                = self.fetchurl.initialize( i )

                #   html template code for embedded links
                html_view               = self.templ_view
                link                    = i

                # -----------------------------------------------------------------------------------------
                #   Normal Template
                #   fetch metadata for website (if available)
                # -----------------------------------------------------------------------------------------

                box_name                = not input_name and self.fetchurl.get_title( soup, box_name ) or input_name
                box_desc                = not input_desc and self.fetchurl.get_description( soup, box_desc, link ) or input_desc
                box_image               = not input_image and self.fetchurl.get_image( soup, box_image ) or input_image
                box_favicon             = not self.config.get( 'favicon_disabled' ) and ( not input_favicon and self.fetchurl.get_favicon( soup, input_url, box_favicon, input_favicon ) or input_favicon ) or ""
                box_favicon_size        = not input_favicon_size and str( self.config[ 'favicon_size' ] ) or input_favicon_size
                box_target              = not input_target and str( self.config[ 'target' ] ) or input_target

                # -----------------------------------------------------------------------------------------
                #   verbose
                # -----------------------------------------------------------------------------------------

                if self.config.get( 'verbose' ):
                    i_truncate = 60

                    if (count_now == 1):
                        print(clr.GREY + '---------------------------------------------------------------------------------------' + clr.RESET)

                    print(clr.YELLOW + '  [ Processing link #' + str(count_now) + ' of ' + str(total) + ' ]:' + '' + page.url + '' + clr.RESET)
                    print()
                    print(clr.GREY + '  box_name ........... :    ' + clr.WHITE + self.truncate( box_name, i_truncate ) )
                    print(clr.GREY + '  box_desc ........... :    ' + clr.WHITE + self.truncate( box_desc, i_truncate ) )
                    print(clr.GREY + '  box_image .......... :    ' + clr.WHITE + self.truncate( box_image, i_truncate ) )
                    print(clr.GREY + '  box_favicon ........ :    ' + clr.WHITE + self.truncate( box_favicon, i_truncate ) )
                    print(clr.GREY + '  box_favicon_size ... :    ' + clr.WHITE + self.truncate( box_favicon_size, i_truncate ) )
                    print(clr.GREY + '  box_target ......... :    ' + clr.WHITE + self.truncate( box_target, i_truncate ) )

                    if (count_now == total):
                        print(clr.GREY + '---------------------------------------------------------------------------------------' + clr.RESET)
                    else:
                        print()

                # -----------------------------------------------------------------------------------------
                #   Handle > Input Override > Image
                # -----------------------------------------------------------------------------------------

                if ( box_image == 'false' ) or ( box_image is None ) or ( not box_image ) or ( self.config.get( 'image_disabled' ) ):
                    style_image         = "display:none;"
                else:
                    style_image         = ""

                # -----------------------------------------------------------------------------------------
                #   Handle > Input Override > Favicon
                # -----------------------------------------------------------------------------------------

                if ( box_favicon == 'false' ) or ( box_favicon is None ) or ( not box_favicon ) or ( self.config.get( 'favicon_disabled' ) ):
                    style_favicon       = "display:none; padding-right: 0px;"
                else:
                    style_favicon       = f"padding-right: 7px; width: {box_favicon_size}px"

                # -----------------------------------------------------------------------------------------
                #   Handle > Input Override > Target
                # -----------------------------------------------------------------------------------------

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
                #
                #   within the html template for embedded links, replace all {{ VARIBLES }} with actual
                #   values
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

                #   assign embedded html with filled out values to new var
                #   {{ VARIABLES }} have been replaced with actual values for each link
                html_output.append(html_view)

            #   converted_markdown should still be empty at this point
            #   all of the html before the next url embed
            converted_markdown.append(markdown[ idx:start ])

            #   add the embedded box html
            converted_markdown.append(''.join(html_output))
            idx                     = end + 1

        #   append the remaining markdown to the converted_markdown
        converted_markdown.append(markdown[ idx:len( markdown ) ])

        #   combined string with output
        markdown_output = ''.join(converted_markdown)

        return markdown_output