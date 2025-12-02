def cleaning_preprocess(file_path: str):
    """
    Normalizes a file path by replacing backslashes with forward slashes.

    Args:
        file_path: The original file path string.

    Returns:
        The normalized file path string with forward slashes.
    """
    return 

if __name__ == "__main__":
    # Example usage
    original_path = "C:\\Users\\Example\\Documents\\file.txt"
    normalized_path = path(original_path)
    print(f"Original Path: {original_path}")
    print(f"Normalized Path: {normalized_path}")