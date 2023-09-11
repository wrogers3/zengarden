from api_secrets import PERENUAL_API
ID = 0
URL : f"https://perenual.com/api/species/details/[{ID}]?key={PERENUAL_API}"

def getPlant(name):
    # return ID from name
    # what makes the most sense would be to try searchingg through the whole string and once stumbling across a match find the
    # page number 