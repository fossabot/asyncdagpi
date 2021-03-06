class ImageFeatures:

    def __init__(self, value: str, description: str):
        self.value = value
        self.description = description

    def __str__(self) -> str:
        return self.value.replace("/", "")

    @classmethod
    def pixel(cls):
        """Pixelate an Image"""
        return cls("/pixel/", "Pixelate an Image")

    @classmethod
    def colors(cls):
        """Analyse and get an Image's Color Top 5 Colors"""
        return cls("/colors/", "Analyse and get an Image's Color Top 5 Colors")

    @classmethod
    def wanted(cls):
        """Get a wanted poster of an Image"""
        return cls("/wanted/", "Get a wanted poster of an Image")

    @classmethod
    def triggered(cls):
        """Get a triggered Image gif"""
        return cls("/triggered/", "Get a triggered Image gif")

    @classmethod
    def wasted(cls):
        """GTA V Wasted screen"""
        return cls("/wasted/", "GTA V Wasted screen")

    @classmethod
    def five_guys_one_girl(cls):
        """No I have never heard of this meme. Takes in 2 Image URL"""
        return cls("/5g1g/",
                   "No I have never heard of this meme. Takes in 2 Image URL")

    @classmethod
    def why_are_you_gay(cls):
        """The infamous Why are you gay. Takes in 2 Image URL"""
        return cls("/whyareyougay/",
                   "The infamous  Why are you gay. Takes in 2 Image URL")

    @classmethod
    def invert(cls):
        """Invert an Image"""
        return cls("/invert/", "Invert an Image")

    @classmethod
    def sobel(cls):
        """Cool SOBEL filter for Images. Only png's"""
        return cls("/sobel/", "Cool SOBEL filter for Images. Only png's")

    @classmethod
    def hog(cls):
        """Histogram of Oriented Gradients"""
        return cls("/hog/", "Histogram of Oriented Gradients")

    @classmethod
    def blur(cls):
        """Blurs an entire Image"""
        return cls("/blur/", "Blurs an entire Image")

    @classmethod
    def rgb(cls):
        """Get RGB information from an image"""
        return cls("/rgb/", "Get RGB information from an image")

    @classmethod
    def angel(cls):
        """Make an Image Angelic"""
        return cls("/angel/", "Make an Image angelic")

    @classmethod
    def satan(cls):
        """Make an Image the devil"""
        return cls("/satan/", "Make an Image the devil")

    @classmethod
    def hitler(cls):
        """Make an Image as bad as hitler"""
        return cls("/hitler/", "Make an Image as bad as hitler")

    @classmethod
    def obama(cls):
        """The obama meme of someone awarding themselves"""
        return cls("/obama/", "The obama meme of someone awarding themselves")

    @classmethod
    def bad(cls):
        """This image is bad."""
        return cls("/bad/", "This image is bad")

    @classmethod
    def sith(cls):
        """Laughs in Sithlord"""
        return cls("/sith/", "Laughs in Sithlord")

    @classmethod
    def jail(cls):
        """Put an Image behind bars"""
        return cls("/jail/", "Put an Image behind bars")

    @classmethod
    def gay(cls):
        """represent! Pastes a pride flag on an image"""
        return cls("/gay/", "represent! Pastes a pride flag on an image")

    @classmethod
    def trash(cls):
        """Makes an Image trash"""
        return cls("/trash/", "Makes an Image trash")

    @classmethod
    def deepfry(cls):
        """Deepfries an Image"""
        return cls("/deepfry/", "Deepfries an Image")

    @classmethod
    def ascii(cls):
        """Turns an Image into a ascii-fied image"""
        return cls("/ascii/", "Turns an Image into a ascii-fied image")

    @classmethod
    def charcoal(cls):
        """Turns an Image into a charcoal sketch"""
        return cls("/charcoal/", "Turns an Image into a charcoal sketch")

    @classmethod
    def poster(cls):
        """Posterizes an image"""
        return cls("/poster/", "Posterizes an image")

    @classmethod
    def sepia(cls):
        """Makes an image sepia tone"""
        return cls("/sepia/", "Makes an image sepia tone")

    @classmethod
    def polaroid(cls):
        """Frames an Image like a printed polaroid"""
        return cls("/polaroid/", "Frames an Image like a printed polaroid")

    @classmethod
    def swirl(cls):
        """Swirls the center of Image"""
        return cls("/swirl/", "Swirls the center of Image")

    @classmethod
    def paint(cls):
        """Turns an Image into an oil painting"""
        return cls("/paint/", "Turns an Image into an oil painting")

    @classmethod
    def night(cls):
        """Turns day into night on an Image"""
        return cls("/night/", "Turns day into night on an Image")

    @classmethod
    def solar(cls):
        """Solarizes an Image"""
        return cls("/solar/", "Solarizes an Image")

    @classmethod
    def thought_image(cls):
        """Wraps Image and Text into a thought
        Needs:
            - text
            - image
        """
        return cls("/thoughtimage/", "Wraps Image and Text into a thought")

    @classmethod
    def tweet(cls):
        """
        Generates an accurate fake tweet
        Needs:
            - text
            - image
            - username
        """
        return cls("/tweet/", "Generates an accurate fake tweet")

    @classmethod
    def discord(cls):
        """
        Generated a realistic Discord Message
        Needs:
            - text
            - image
            - quote
        """
        return cls("/discord/", "Generated a realistic Discord Message")
