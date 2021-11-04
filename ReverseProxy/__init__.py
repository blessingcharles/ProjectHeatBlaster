from flask import Flask
from ReverseProxy.utils import loginfo
from env.server_config import *
from ReverseProxy.mod_request_handlers.router import request_handlers

app = Flask(__name__)

def create_server(config_file : str ='env.server_config.ProductionConfig') -> None:

    app.config.from_object(config_file)
    #register module instances
    app.register_blueprint(request_handlers)
    loginfo(f"Server started at { app.config['HOST']} port : {app.config['PORT']}")
    app.run(host=app.config["HOST"] , port=app.config["PORT"])
