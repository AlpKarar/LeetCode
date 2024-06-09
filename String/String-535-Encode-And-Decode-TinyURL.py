class Codec:
    matches = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        slash = 0
        idx = 0

        for i in range(len(longUrl)):
            if slash == 3:
                idx = i
                break
            if longUrl[i] == "/":
                slash += 1
        

        hashedUrl = longUrl[:idx+1] + str(hash(longUrl[idx:]))

        if hashedUrl not in Codec.matches:
            Codec.matches[hashedUrl] = longUrl
        
        return hashedUrl
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        longUrl = ""

        if shortUrl in Codec.matches:
            longUrl = Codec.matches[shortUrl]
        
        return longUrl
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))