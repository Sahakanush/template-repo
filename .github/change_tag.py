import yaml
import sys

image = sys.argv[1]

with open('../../ArgoApps/app.yaml') as file:
  data_dict = yaml.load(file)
  data_dict['spec']['template']['spec']['containers'][0]['image'] = image
  
  with open('../../ArgoApps/app.yaml', 'w') as f:
        yaml.dump(data_dict, f)
