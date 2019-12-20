import os
import sys

project_path_common = os.path.join(os.path.abspath('.'), 'common')
project_path_db = os.path.join(os.path.abspath('.'), 'db')
sys.path.append(project_path_common)
sys.path.append(project_path_db)
