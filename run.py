from ReverseProxy import create_server
from ReverseProxy.utils import loginfo


if __name__ == "__main__":
    create_server(config_file='env.server_config.DevelopmentConfig')