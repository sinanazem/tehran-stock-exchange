import re 


def extract_date_from_file_path(file_path):
    pattern = r'(\d{4}-\d{2}-\d{2})'
    match = re.search(pattern, file_path)
    if match:
        extracted_date = match.group(1)
        return extracted_date
    else:
        return None