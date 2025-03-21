import ee
import pandas as pd

def initialize_gee(project, opt_url="https://earthengine-highvolume.googleapis.com"):
    """
    Initializes the Google Earth Engine API with a specified project and opt_url.
    
    Parameters:
        project (str): The GEE project ID.
        opt_url (str): The Earth Engine URL to use for initialization.
        
    Raises:
        RuntimeError: If initialization fails.
    """
    try:
        ee.Initialize(opt_url=opt_url, project=project)
    except Exception as e:
        raise RuntimeError(
            "Google Earth Engine is not initialized. "
            "Please run 'earthengine authenticate' in your terminal."
        ) from e
    
def getTaskStatus():
    tasks = ee.data.listOperations()
    tasks_list = []
    for task in tasks:
        if 'description' in task['metadata']:
            description = task['metadata']['description']
            state = task['metadata']['state']
            tasks_list.append({
                'name': task['name'],
                'description': description,
                'state': state
            })
    tasks_df = pd.DataFrame(tasks_list)
    print(tasks_df['state'].value_counts())
    return tasks_df