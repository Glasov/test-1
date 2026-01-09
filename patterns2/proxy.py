cat > proxy.py << 'EOF'
class Image:
    def display(self):
        pass

class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()
    
    def load_from_disk(self):
        print(f"Загрузка {self.filename}")
    
    def display(self):
        print(f"Показ {self.filename}")

class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None
    
    def display(self):
        if not self.real_image:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

# Пример
if __name__ == "__main__":
    image = ProxyImage("photo.jpg")
    image.display()  # Загружает и показывает
    image.display()  # Только показывает (уже загружено)
EOF