class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def articles(self):
        return self._articles

    @property
    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        return list({magazine.category for magazine in self.magazines})


class Magazine:
    all = []

    def __init__(self, name, category):
        if not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters.")
        if not category:
            raise ValueError("Category cannot be empty.")
        self._name = name
        self._category = category
        self._articles = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not (2 <= len(new_name) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not new_category:
            raise ValueError("Category cannot be empty.")
        self._category = new_category

    @property
    def articles(self):
        return self._articles

    @property
    def contributors(self):
        return list({article.author for article in self._articles})

    def contributing_authors(self):
        return [author for author in self.contributors if len([a for a in self._articles if a.author == author]) > 2]

    @classmethod
    def top_publisher(cls):
        return max(cls.all, key=lambda magazine: len(magazine.articles), default=None)


class Article:
    all = []  
    def __init__(self, author, magazine, title):
        # Initialize author, magazine, and title attributes
        self._author = author
        self._magazine = magazine
        self.title = title
        Article.all.append(self)  # Add the current instance to the class-level all list

    # Author property and setter to allow mutation
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        self._author = new_author

    # Magazine property and setter to allow mutation
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        self._magazine = new_magazine

