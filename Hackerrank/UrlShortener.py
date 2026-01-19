import hashlib
import string
import random
from collections import defaultdict

class URLShortener:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "https://short.url/"
        self.analytics = defaultdict(lambda: {'clicks': 0, 'timestamps': []})
    
    def shorten(self, original_url, custom_code=None):
        """Shorten a URL"""
        if original_url in self.url_to_code and not custom_code:
            return self.base_url + self.url_to_code[original_url]
        
        if custom_code:
            if custom_code in self.code_to_url:
                raise ValueError("Custom code already exists")
            code = custom_code
        else:
            code = self.generate_code()
        
        self.url_to_code[original_url] = code
        self.code_to_url[code] = original_url
        
        return self.base_url + code
    
    def generate_code(self, length=6):
        """Generate random short code"""
        chars = string.ascii_letters + string.digits
        while True:
            code = ''.join(random.choice(chars) for _ in range(length))
            if code not in self.code_to_url:
                return code
    
    def expand(self, short_code):
        """Get original URL from short code"""
        if short_code in self.code_to_url:
            # Track analytics
            self.analytics[short_code]['clicks'] += 1
            self.analytics[short_code]['timestamps'].append(datetime.now().isoformat())
            
            return self.code_to_url[short_code]
        return None
    
    def get_analytics(self, short_code):
        """Get analytics for a short URL"""
        if short_code in self.analytics:
            return dict(self.analytics[short_code])
        return {'clicks': 0, 'timestamps': []}
    
    def get_top_urls(self, limit=10):
        """Get most clicked URLs"""
        sorted_analytics = sorted(
            self.analytics.items(),
            key=lambda x: x[1]['clicks'],
            reverse=True
        )
        return sorted_analytics[:limit]

# Usage
shortener = URLShortener()

# Shorten URLs
short_url1 = shortener.shorten("https://www.google.com/search?q=python+programming")
short_url2 = shortener.shorten("https://github.com/python", custom_code="PYTHON")

print(f"Short URL 1: {short_url1}")
print(f"Short URL 2: {short_url2}")

# Expand
original = shortener.expand("PYTHON")
print(f"Original: {original}")