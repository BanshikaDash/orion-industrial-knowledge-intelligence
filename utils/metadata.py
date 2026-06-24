import os
def extract_metadata(file_path):
    return {
        "filename": os.path.basename(file_path),
        "extension": os.path.splitext(file_path)[1]
    }