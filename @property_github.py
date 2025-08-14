class Article:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    @property
    def word_count(self):
        return len(self.content.split())

    @property
    def reading_time_minutes(self):
        # Average reading speed: 200 words/min
        return round(self.word_count / 200, 2)

def main():
    post = Article("Python Tricks", "Python is great! " * 450)
    print(f"Title: {post.title}")
    print(f"Word Count: {post.word_count}")
    print(f"Estimated Reading Time: {post.reading_time_minutes} minutes")

if __name__ == "__main__":
    main()
