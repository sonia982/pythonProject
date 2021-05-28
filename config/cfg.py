import configparser

config = configparser.ConfigParser.RawConfigParser()
config.read('config/etl_job_config.ini')
