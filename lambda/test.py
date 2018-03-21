import json
import datetime
import dateutil.parser
import logging.config

from lxml import etree

from requests import Session
from zeep import Client
from zeep import Plugin
from zeep.helpers import serialize_object
from zeep.transports import Transport
from zeep.plugins import HistoryPlugin

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'zeep.transports': {
            'level': 'DEBUG',
            'propagate': True,
            'handlers': ['console'],
        },
    }
})

def handler(event, context):
    bodyJSON = json.loads(event['body'])

    return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(bodyJSONs)
        }
