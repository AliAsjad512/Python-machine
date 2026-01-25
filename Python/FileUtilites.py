def file_info(filepath):
    """Get detailed information about a file"""
    if not os.path.exists(filepath):
        return f"File not found: {filepath}"
    
    stats = os.stat(filepath)
    size_kb = stats.st_size / 1024
    
    info = {
        'Filename': os.path.basename(filepath),
        'Path': os.path.dirname(filepath),
        'Size': f"{size_kb:.2f} KB",
        'Created': datetime.datetime.fromtimestamp(stats.st_ctime),
        'Modified': datetime.datetime.fromtimestamp(stats.st_mtime),
        'Type': 'Directory' if os.path.isdir(filepath) else 'File'
    }