class VideoService:
    def play_video(self, video_id):
        return f"Play video {video_id}"


class VideoCache:
    def __init__(self):
        self.cache = {}
    
    def get_video(self, video_id):
        if video_id in self.cache:
            return f"Video {video_id} from cache"
        return None


class VideoProxy:
    def __init__(self):
        self.service = VideoService()
        self.cache = VideoCache()
    
    def play_video(self, video_id):
        cached = self.cache.get_video(video_id)
        if cached:
            return cached
        
        video = self.service.play_video(video_id)
        self.cache.cache[video_id] = video
        return video
        
player = VideoProxy()

print(player.play_video("video1"))
print(player.play_video("video1"))
print(player.play_video("video2"))
