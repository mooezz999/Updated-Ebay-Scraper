




import csv
import requests
from bs4 import BeautifulSoup
def get_page(url):
    response = requests.get(url)

    if not response.ok:
        print('server responded:', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_detail_data(soup):
    try:
        title=soup.find('h1', id='itemTitle').text
    except:
           title = ''

    try:
        try:
            price=soup.find('span', id= 'prcIsum').text
        except:
            price = soup.find('span', id='mm-saleDscPrc').text


    except:
           price = ''
    try:
      if price=='':

         price = soup.find('span', id='prcIsum_bidPrice').text
    except:
            price=''
    try:
        sold=soup.find('a', {'class': 'vi-txt-underline'}).text
    except:
           sold = ''

    try:
        soldpercentag=soup.find_all('span', {'class': 'w2b-head'}).text
        if soldpercentag[-12:] == '%':
            soldpercentage=soldpercentag
    except:
           soldpercentage = ''

    try:
        sellername=soup.find('span', {'class': 'mbg-nw'}).text
    except:
           sellername = ''

    try:
        noofreviews = soup.find('span', {'class': 'mbg-l'}).text
    except:
        noofreviews = ''

    try:
        feedback = soup.find('div', id='si-fb').text
    except:
        feedback = ''

    try:
        shipping=soup.find('span', id='fshippingCost').text
    except:
           shipping = ''
    print(title[16:])
    print(price)
    print(sold)
    print(shipping)
    print(soldpercentage)
    print(sellername)
    print(noofreviews)
    print(feedback)
    data={
        'title': title[16:],
        'price': price,
        'sold': sold[:-5],
        'shipping':shipping,
        'soldpercentage':soldpercentage,
        'sellername':sellername,
        'noofreviews':noofreviews,
        'feedback':feedback
    }

    return data


def get_index_data(soup):
    try:
        links=soup.find_all('a', class_='s-item__link')
    except:
        links=[]

    urls=[item.get('href') for item in links]
    return urls

def write_csv(data, url):
    with open('pants555.csv', 'a') as csvfile:
        writer=csv.writer(csvfile)
        row = [data['title'],data['price'],data['sold'],data['shipping'],data['soldpercentage'],data['sellername'],data['noofreviews'],data['feedback'], url]
        writer.writerow(row)
def main():
#   url = 'https://www.ebay.com/itm/Fashion-Sport-Mens-Stainless-Steel-Case-Leather-Band-Quartz-Analog-Wrist-Watch/362768766864?_trkparms=ispr%3D1&hash=item5476b41790:g:qo0AAOSwENVdkCzN&amdata=enc%3AAQAFAAACcBaobrjLl8XobRIiIML1V4Imu%252Fn%252BzU5L90Z278x5ickkBSh1VzQSTzkTiSV5EE%252FHQcjGw9P7hxM4148ngRgcR2x34iU725vZvwfG3JxW3Whf14g0uujHCz%252FEqo4Kv0Oa7TURrlGFPqz2u0NPmd0xFY4rGE7lPxklmfSxSRI2D6cFYyDPhiyzmogr%252Bt0EHqcxLELXyFx1BLjLHLJZ%252BJeZk3waPMCpQ1aiVF2qOjQVzIGYslKLXBAUAaqWgCCH7NrJ%252F%252B5FqnoWaEoOnYm52ZlAwBQpMhkA7W6pT26bkVGBl9CfWeJBYv0cgRCTHaRiFfWdVsGrnIJEdG8nMqgMfmMKmB1OaiH2mJhc7rzYDDzevb0lzRhSvUw%252BdiyEsHEAqNnOvYXOJilW0lcxEZE5mZZoG9WlykRUCr3FCKHYpmPCsY5%252FpQdy7RwuBvjEeb33UgeBPUDAC%252BUNW%252BLBR6wLxXfPuZK1hMpwU7xqDZDOLE3hrPTwNTSA7fNllgHw8UrVz3coGq4ic8q3GLmHPMww45fu4oz1Bia7%252Ft5uPe2AYUwvstLHzpmuE0xQqUfv9qBLWLt%252Bm8xSFWR2Zc%252F5TPAOuiPP2BRPbih%252F2BPh7Rjv23zrlhpOU5TUS75uygroUI8fedyvVhYYWKx0z%252Ft94LjdriIl7IL9v9oENOSdmDz8zL%252FENNi%252FOs2cpWQShP11o3V6pbrRwkwBDyX%252Bw%252FMsuPDP8yXvcQaMoltubKMlesN%252F4gAgAZzvvsvCyzll%252BpkjUEtXrA2xdVQOiXoQW6mX%252F9OQ%252BCnAcbLgocFLmRpc9AWcXyUraWg7Ewns%252B7p8XB4%252BRjO7TtTCig%253D%253D%7Ccksum%3A362768766864f57cf9fc08034151bfe2d4f06d32766b%7Campid%3APL_CLK%7Cclp%3A2334524'
   #url='https://www.ebay.com/itm/Lip-Sleeping-Mask-LANEIGE-20g-3g-Smoothing-Dryness-Moisture-Lip-Balm-Lip-Care/143617947157?hash=item21704bf615:g:iZAAAOSw3e1e0Ulz&var=442576992073'
    #url='https://www.ebay.com/itm/Executive-Office-Chair-High-Back-Mesh-Chair-Seat-Office-Desk-Chairs-Height/231291032679?epid=21003304267&_trkparms=ispr%3D1&hash=item35da051467:g:D0UAAOSwrl5avtIu&amdata=enc%3AAQAFAAACcBaobrjLl8XobRIiIML1V4Imu%252Fn%252BzU5L90Z278x5ickkai8xCwosGKpC0NWj85e%252FB%252Bsmqw0mv9Lo%252FPWLzGQzPxGumm301ieGDGDDU%252BzHLweM%252BVKpffQPW3pVSETTHjMGnQPaEw2lVxMfiXwBQ8I%252FXtCgKH7Sl1mH76n2gpBAdmuWT4GuiDMy2moI%252Bhkkv0RjfywVzecsY9Z9e3GytCOvbsterhGfG35mmK8pJUA9krvFeDlSpCEHWPPS7Cjrb9keRJ03LhF8XaLvB2qrZcK703zDPRsl%252BPv%252By%252BeTAbkC1Dl443Gh1zGt2DNtgr3c%252BrVED3ZSqKestn4pPXwQQ7D0zoQk0uhWv3%252BD0mYre3qZ03g3jTctFzAlqi408mmEtef6JHCVuCPgJSGP9mKhnVy77XOquOqg4C3I%252B7HrD5fk0ErbVHZlXnqPAhNWSbDgPYHMlIQwih%252BbBCxvMhP24%252BvBapctX%252FOfULAGfY1sW4EJsRPhFeH%252BqMU0qthL2HY8EuswyE%252BUginIZBVdIWgqW5h3VQ%252BHAErfDNs7pMyg%252Fg2QcEIav95BOuI%252BJMK5tYuMTyR7YHSRhIuiVGpStf4GcqMlwQ%252FEvheXQOXH8B5v2vqnicXH8kkKxXHXLcHKfG0HyP8QU%252BmzIqTpImxPil%252BZK4zC7vV6KVmRnazoVfq2Ozobxw1DQ1un5AuwSAUq%252FykIjfWANS1L%252Fx4dnqA2K7ZO7bcWKLgHFj%252Bp%252BMmuVhlNmm1QYBuZTvtFCD5mBFh4Bkdu8ns%252ByMLld%252BbpsSUYIIn1xrQffpXOukqh6wcNcLPChRoq3JXv4AnhiYRnsgPZW3nX4V8aPA%253D%253D%7Ccksum%3A2312910326795fb7ab17559b42aa8c78f8d3a548bd16%7Campid%3APL_CLK%7Cclp%3A2334524'
    url='https://www.ebay.com/sch/i.html?_nkw=pants&_pgn='
    for page in range(100):
        products = get_index_data(get_page(url+ str(page)))
        for link in products:
            data= get_detail_data(get_page(link))
            write_csv(data, link)

if __name__=='__main__':
    main()