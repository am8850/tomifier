def write_text(file_path: str, content: str) -> None:
    """
    Write text to a file
      :param file_path: The file path
      :param content: The content to write
    """
    with open(f'{file_path}', 'w') as f:
        f.write(content)

def write_bytes(file_path: str, content: str) -> None:
    """
    Write bytes to a file
      :param file_path: The file path
      :param content: The content to write
    """
    if not content:
        return
    bytes = str.encode(content)
    with open(f'{file_path}', 'wb') as f:
        f.write(bytes)