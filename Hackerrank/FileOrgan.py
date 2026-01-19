import os
import shutil
from pathlib import Path
import mimetypes

class FileOrganizer:
    def __init__(self, directory):
        self.directory = Path(directory)
        self.categories = {
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
            'documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.md'],
            'videos': ['.mp4', '.avi', '.mov', '.mkv', '.flv'],
            'audio': ['.mp3', '.wav', '.flac', '.aac'],
            'archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
            'code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c']
        }
    
    def organize(self):
        """Organize files into categorized folders"""
        if not self.directory.exists():
            print(f"Directory {self.directory} doesn't exist")
            return
        
        # Create category directories
        for category in self.categories.keys():
            (self.directory / category).mkdir(exist_ok=True)
        
        # Process each file
        moved_files = 0
        for file_path in self.directory.iterdir():
            if file_path.is_file():
                category = self.categorize_file(file_path)
                if category:
                    dest = self.directory / category / file_path.name
                    shutil.move(str(file_path), str(dest))
                    moved_files += 1
                    print(f"Moved: {file_path.name} -> {category}/")
        
        print(f"\nOrganized {moved_files} files")
        return moved_files
    
    def categorize_file(self, file_path):
        """Determine file category based on extension"""
        ext = file_path.suffix.lower()
        
        for category, extensions in self.categories.items():
            if ext in extensions:
                return category
        
        # Try to guess from MIME type
        mime_type, _ = mimetypes.guess_type(file_path)
        if mime_type:
            if mime_type.startswith('image/'):
                return 'images'
            elif mime_type.startswith('video/'):
                return 'videos'
            elif mime_type.startswith('audio/'):
                return 'audio'
            elif mime_type.startswith('text/'):
                return 'documents'
        
        return 'other'

# Usage
organizer = FileOrganizer('./Downloads')
organizer.organize()