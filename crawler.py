import urllib.request as req
import bs4  #BeautifulSoup helps us to analyze HTML

def getOffers(url):
    request=req.Request(url, headers={
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    })
    with req.urlopen(request) as response:
        data=response.read().decode('utf-8')
    
    root=bs4.BeautifulSoup(data, 'html.parser')
    titles=root.find_all('h3', class_='font-light break-words text-lg md:text-xl text-liquorice leading-snug cursor-pointer') # Find the offers'

    with open('offers.txt', 'w', encoding='utf-8') as file: #Write the result to a text file
        for title in titles:
         print(title.text)
         file.write(title.text+"\n")


pageURL="https://www.vouchercodes.co.uk/featured-voucher-codes.html"
getOffers(pageURL)

