import os

def get_api_version():
    """
    Returns the version of the API (test)
    """
    return {'version': os.getenv('API_VERSION', "10.0.5")}