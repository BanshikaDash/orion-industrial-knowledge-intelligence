import re
def extract_entities(text):
    equipment = re.findall(r'(Compressor\sC\d+|Pump\sP\d+|Generator\sG\d+)', text)
    dates = re.findall(r'\d{4}-\d{2}-\d{2}', text)
    return {
        "equipment": equipment,
        "dates": dates
    }