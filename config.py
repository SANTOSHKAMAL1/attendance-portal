import os
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.environ.get('MONGO_URI') or os.environ.get('MONGODB_URI') or ''
db_name = os.environ.get('MONGO_DB') or 'jain_bos_portal_dev'

if mongo_uri:
    try:
        from pymongo.uri_parser import parse_uri
        parsed = parse_uri(mongo_uri)
        if not parsed.get('database'):
            if '?' in mongo_uri:
                prefix, query = mongo_uri.split('?', 1)
                prefix = prefix.rstrip('/')
                mongo_uri = f"{prefix}/{db_name}?{query}"
            else:
                mongo_uri = f"{mongo_uri.rstrip('/')}/{db_name}?retryWrites=true&w=majority"
    except Exception:
        pass
    os.environ['MONGO_URI'] = mongo_uri

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    MONGO_URI = mongo_uri