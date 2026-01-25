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

     if os.path.isfile(filepath):
        _, ext = os.path.splitext(filepath)
        info['Extension'] = ext or 'None'
    
    return info

def list_directory(path='.'):
    """List contents of a directory with details"""
    print(f"📁 Contents of: {os.path.abspath(path)}")
    print("-"*60)
    
    items = os.listdir(path)
    items.sort()
    
    for item in items:
        item_path = os.path.join(path, item)
        is_dir = os.path.isdir(item_path)
        
        if is_dir:
            print(f"📂 {item}/")
        else:
            size = os.path.getsize(item_path)
            size_str = f"{size:,} bytes" if size < 1024 else f"{size/1024:.1f} KB"
            print(f"📄 {item:30} ({size_str})")
    
    print(f"\nTotal: {len(items)} items")
