from bs4 import BeautifulSoup
def getresult(res):
    soup = BeautifulSoup(res.text, "html.parser")
    return soup.td.text
