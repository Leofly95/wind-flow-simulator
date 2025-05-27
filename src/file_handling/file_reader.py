def load_image(filepath):
    import cv2
    image = cv2.imread(filepath)
    if image is None:
        raise FileNotFoundError(f"Image file not found: {filepath}")
    return image

def load_json(filepath):
    import json
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data