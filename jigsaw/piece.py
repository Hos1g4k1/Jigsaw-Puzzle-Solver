class Piece(object):

    '''
     Klasa koje predstavlja jedan deo slagalice
     
     image: Slika tog dela
     id: Jedinstveni identifikator
    '''

    def __init__(self, image, index):
        self.image = image[:]
        self.id = index

    def __getitem__(self, index):
        return self.image.__getitem__(index)

    def size(self):
        return self.image.shape[0]

    def shape(self):
        return self.image.shape
