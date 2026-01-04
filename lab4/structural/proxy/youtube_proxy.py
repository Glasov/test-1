"""
Паттерн Прокси (Proxy)
Заместитель контролирует доступ к оригинальному объекту.
"""

from abc import ABC, abstractmethod
import time

# Интерфейс видео
class YouTubeVideo(ABC):
    @abstractmethod
    def play(self) -> str:
        pass

# Реальный объект
class RealYouTubeVideo(YouTubeVideo):
    def __init__(self, title: str):
        self.title = title
        self._load_video()
    
    def _load_video(self):
        # Имитация загрузки тяжелого видео
        time.sleep(2)
        print(f"Видео '{self.title}' загружено")
    
    def play(self) -> str:
        return f"Воспроизведение видео: {self.title}"

# Прокси
class YouTubeProxy(YouTubeVideo):
    def __init__(self, title: str):
        self.title = title
        self.real_video = None
        self.cache = None
    
    def play(self) -> str:
        if self.real_video is None:
            print("Прокси: создаю реальный объект...")
            self.real_video = RealYouTubeVideo(self.title)
        
        if self.cache is None:
            self.cache = self.real_video.play()
        
        return self.cache
    
    def get_info(self) -> str:
        # Дополнительный метод в прокси
        return f"Информация о видео: {self.title} (просмотров: 1M, лайков: 50K)"
