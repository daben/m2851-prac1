import copy
import scrapy.utils.log
from colorlog import ColoredFormatter

COLORED_LOGGING = True

if COLORED_LOGGING:

    color_formatter = ColoredFormatter(
        (
            '-- %(log_color)s%(levelname)-5s%(reset)s '
            '%(yellow)s[%(asctime)s]%(reset)s'
            '%(white)s %(name)s'
            '%(bold_white)s.%(funcName)s%(bold_purple)s:%(lineno)d%(reset)s\n'
            '%(log_color)s%(message)s%(reset)s'
        ),
        datefmt='%y-%m-%d %H:%M:%S',
        log_colors={
            'DEBUG': 'bold_green',
            'INFO': 'bold_blue',
            'WARNING': 'red',
            'ERROR': 'bg_bold_red',
            'CRITICAL': 'red,bg_white',
        }
    )

    _get_handler = copy.copy(scrapy.utils.log._get_handler)

    def _get_handler_custom(*args, **kwargs):
        handler = _get_handler(*args, **kwargs)
        handler.setFormatter(color_formatter)
        return handler

    scrapy.utils.log._get_handler = _get_handler_custom
