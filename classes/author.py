class Author:

    def __init__(self, authorDetails: list):
        
        self.idAuthor = authorDetails[0]
        self.firstName = authorDetails[1]
        self.lastName = authorDetails[2]
        self.biography = authorDetails[3]
        self.publisher = authorDetails[4]