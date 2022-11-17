class Movie:
    def __init__(self, title):
        self._title = title

    def get_title(self):
        """
        this is the getter of 'title'

        Returns:
            str: movie title
        """
        return self._title

    def set_title(self, title):
        """
        with setters we can validate the
        new value before assigning it to
        the attribute

        Args:
            title (_type_): _description_
        """
        self._title = title


movie = Movie("The Good, The Bad, and The Ugly")
print(movie.get_title())

movie.set_title("Titanic")
print(movie.get_title())
