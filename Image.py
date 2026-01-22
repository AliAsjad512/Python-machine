from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont
import os

class ImageProcessor:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.path = image_path
        self.format = self.image.format
        self.mode = self.image.mode
        self.size = self.image.size
    
    def display_info(self):
        """Display image information"""
        print(f"Format: {self.format}")
        print(f"Mode: {self.mode}")
        print(f"Size: {self.size}")
        print(f"Filename: {os.path.basename(self.path)}")
    
    def resize(self, width=None, height=None, maintain_ratio=True):
        """Resize image"""
        if maintain_ratio and width and height:
            self.image.thumbnail((width, height))
        else:
            if width and height:
                self.image = self.image.resize((width, height))
            elif width:
                ratio = width / self.image.width
                height = int(self.image.height * ratio)
                self.image = self.image.resize((width, height))
            elif height:
                ratio = height / self.image.height
                width = int(self.image.width * ratio)
                self.image = self.image.resize((width, height))
    
    def apply_filter(self, filter_name):
        """Apply various filters"""
        filters = {
            'blur': ImageFilter.BLUR,
            'contour': ImageFilter.CONTOUR,
            'detail': ImageFilter.DETAIL,
            'edge_enhance': ImageFilter.EDGE_ENHANCE,
            'emboss': ImageFilter.EMBOSS,
            'sharpen': ImageFilter.SHARPEN,
            'smooth': ImageFilter.SMOOTH,
            'grayscale': lambda img: img.convert('L')
        }
        
        if filter_name in filters:
            if callable(filters[filter_name]):
                self.image = filters[filter_name](self.image)
            else:
                self.image = self.image.filter(filters[filter_name])
    
    def adjust_brightness(self, factor):
        """Adjust brightness (factor > 1 = brighter, < 1 = darker)"""
        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(factor)
    
    def adjust_contrast(self, factor):
        """Adjust contrast"""
        enhancer = ImageEnhance.Contrast(self.image)
        self.image = enhancer.enhance(factor)
    
    def rotate(self, degrees):
        """Rotate image"""
        self.image = self.image.rotate(degrees, expand=True)
    
    def add_text(self, text, position=(10, 10), font_size=20, color='white'):
        """Add text watermark"""
        draw = ImageDraw.Draw(self.image)
        
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()
        
        draw.text(position, text, fill=color, font=font)
    
    def add_watermark(self, watermark_path, opacity=0.5):
        """Add image watermark"""
        watermark = Image.open(watermark_path).convert("RGBA")
        
        # Resize watermark
        wm_size = (self.image.width // 4, self.image.height // 4)
        watermark.thumbnail(wm_size)
        
        # Set opacity
        alpha = watermark.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
        watermark.putalpha(alpha)
        
        # Position at bottom right
        position = (
            self.image.width - watermark.width - 10,
            self.image.height - watermark.height - 10
        )
        
        self.image.paste(watermark, position, watermark)
    
    def save(self, output_path=None, format=None, quality=95):
        """Save processed image"""
        if not output_path:
            filename, ext = os.path.splitext(self.path)
            output_path = f"{filename}_processed{ext}"
        
        self.image.save(output_path, format=format or self.format, quality=quality)
        print(f"Image saved to: {output_path}")
        return output_path
    
    def show(self):
        """Display image"""
        self.image.show()

# Usage
processor = ImageProcessor('input.jpg')
processor.display_info()
processor.resize(width=800)
processor.apply_filter('grayscale')
processor.add_text("Sample Watermark", position=(20, 20))
processor.save('output.jpg')