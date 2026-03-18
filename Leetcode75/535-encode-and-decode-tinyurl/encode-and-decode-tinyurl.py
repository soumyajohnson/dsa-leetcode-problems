class Codec:
    def __init__(self):
        self.store={}
        self.chars="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def generate(self) -> str:
        return ''.join(random.choice(self.chars) for _ in range(6))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key=self.generate()
        while key in self.store:
            key=self.generate()
        self.store[key]=longUrl
        return "http://tinyurl.com/"+key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key=shortUrl.split('/')[-1]
        return self.store[key]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))