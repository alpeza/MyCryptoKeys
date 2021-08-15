import yaml
import os

curpath=os.path.dirname(os.path.abspath(__file__))
configp=os.path.join(curpath,'..','config.yaml')

with open(configp, 'r') as stream:
    try:
        config = yaml.safe_load(stream)
        storagefile=os.path.join(config['localpath'],config['storagename'])
    except yaml.YAMLError as exc:
        raise exc