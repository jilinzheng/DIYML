def create_dataset(type):
    """
    Create a dataset with [type] data.
    
    :param type: the type of data the dataset is expected to hold
    :returns: same as param type
    """
    return type

def upload_dataset(source, target_dataset):
    """
    Upload dataset from source to target_dataset.

    :param source: the source of the dataset (specifics WIP)
    :param target_dataset: the ID or name of the dataset for the upload
    :returns: the ID of the dataset that was the upload target
    """
    return target_dataset

def delete_dataset(target_dataset):
    """
    Delete the target_dataset.
    
    :param target_dataset: the ID or name of the dataset to be deleted
    :returns; the ID of the dataset that was deleted
    """
    return target_dataset


def create_label(label_name, label_description=None):
    """
    Create a label_name with optional label_description.
    
    :param label_name: name of the label to be created
    :param label_description: optional description of the label
    :returns: the newly-created label name
    """
    return label_name

def add_label(target_dataset, target_data, label_name):
    """
    Update target_data in a target_dataset with an existing label_name.
    
    :param target_dataset: the ID or name of the dataset that contains of the data to be labeled
    :param target_data: the ID or name of the data to be labeled
    :param label_name: the label to update the data with
    :returns: a dictionary consisting of the dataset and data that was labeled, as well as the label name
    """
    return {target_dataset, target_data, label_name}

def remove_label(target_dataset, target_data, label_name):
    """
    Update target_data in a target_dataset by removing its existing label_name.
    
    :param target_dataset: the ID or name of the dataset that contains the data whose label shall be removed
    :param target_data: the ID or name of the data whose label shall be removed
    :param label_name: the label to be removed
    :returns: a dictionary consisting of the dataset and data whose label was removed, as well as the label name
    """
    return {target_dataset, target_data, label_name}

def delete_label(label_name):
    """
    Delete the selected label_name, and also remove any instances of the label_name from existing data/datasets. Can be an expensive operation.
    
    :param label_name: the label name to be deleted
    :returns: the label name deleted
    """
    return label_name