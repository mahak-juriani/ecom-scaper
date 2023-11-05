import requests

def scrape(url):
    # url = 'https://www.flipkart.com/canon-eos-3000d-dslr-camera-1-body-18-55-mm-lens/p/itm6f665fea97bc2?pid=CAMF3DHJURPEMNRN&marketplace=FLIPKART'
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0'
    headers = {
        'User_Agent' : user_agent,
        'Cookie' : "T=TI169225236689700123987017221035868411998659485046478371205199787133; SN=VI35133763DECB47FF8B326106EC831815.TOK70888DE3E23D427D855227BA48F08312.1698858271.LO; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3MDA1ODYyNjEsImlhdCI6MTY5ODg1ODI2MSwiaXNzIjoia2V2bGFyIiwianRpIjoiZjBlZWIyMzQtZmJmMi00ZDUwLTgyMjUtNDgwZTBkMzllNjYxIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjkyMjUyMzY2ODk3MDAxMjM5ODcwMTcyMjEwMzU4Njg0MTE5OTg2NTk0ODUwNDY0NzgzNzEyMDUxOTk3ODcxMzMiLCJrZXZJZCI6IlZJMzUxMzM3NjNERUNCNDdGRjhCMzI2MTA2RUM4MzE4MTUiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.B6wZTJz8poXEmlXXFuHfDIJG3I5xkf8RZom_wHXv1Wg; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19663%7CMCMID%7C32873281606935493616824337684014555567%7CMCAID%7CNONE%7CMCOPTOUT-1698865453s%7CNONE%7CMCAAMLH-1698917422%7C12%7CMCAAMB-1699463053%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; S=d1t10KD8KPxY/Pz8/Pz8/ZD9dWg2fLHHWPjLdvV9v7Su9HXpupeRqaxWn7aWDIMVTzo02b9UtpGav8pHTLDR0DKzX8A==; _pxvid=285d6f7d-3cc4-11ee-8dbe-84a6fc1ccda1; vh=968; vw=1920; dpr=1; ULSN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTIzMTAwNjE2MTgxOTcxNFA1SVoxMTQiLCJma0RldiI6bnVsbH0sImV4cCI6MTcxMjM2OTI5OSwiaWF0IjoxNjk2NTg5Mjk5LCJqdGkiOiI5Mzg5NTNkZS00OGEyLTRlNjMtODQ4Mi0zN2NkYmFkMmQ3NDQifQ.IjbtoPHxoxiIbBcW2ECgwleQ2rAT1O_l5KF3BXkB8nM; fonts-loaded=en_loaded; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; pxcts=afe0f9e6-78d8-11ee-a4e7-e1a1efeaca0b; _px3=30d4771babcd57c862e432878595e6a5b20690a7738338972c50ea6371e3ccce:br6wtpv5XlXgQU47N1jVLkO/Z/rcMPTlaG2efPr9EBbWuiMbkN0yUxABihQ8dDqDJ/Ttp09VsW/6gDZFzF7XGA==:1000:O+L21eVtLlG1IJCIMieFWU3tQs321SyOIZMB3QOU4oyLV1f9f837199YeB5mUIXoKAt10tm8jHsm36mZ4vk1Ikt6Nuq9nHiWmFT+xJ59U915nxtOhWyADSOQMfxeQ18sKYXS1i2MNgawbzINXdUxk2Y8I1zl0nPdhCgcqFpHVsPv5gcf9g9OoE79Tj8BCbtaMEaBBC3qY8jQQpZbpGm30W8X/NwkUwGDKD4SWITNjPk=;"
    }
    # print(url)
    r = requests.get(url,headers=headers)
    
    # print(r.content)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.content, 'html5lib')

    title = soup.select('.B_NuCI')[0].text.strip()
    current_price = soup.select('._30jeq3._16Jk6d')[0].text.strip()
    scraped_current_price = current_price.replace("₹","")
    mrp = soup.select('._3I9_wc._2p6lqe')[0].text.strip()
    scraped_mrp = mrp.replace("₹","")
    x = soup.select('._2_R_DZ')[0].text.strip()
    # review_count = x.findChildren()


    print("Name of the product: ", title)
    print("Current Price of the product: ",scraped_current_price)
    print("MRP of the product: ",scraped_mrp)
    print("Review count of the product: ", x)

    return{
        'title': title,
        'current_price': scraped_current_price,
        'mrp': mrp,
        # 'review_count': review_count,
        # 'rating': rating
    }

# result = scrape('https://www.flipkart.com/canon-eos-3000d-dslr-camera-1-body-18-55-mm-lens/p/itm6f665fea97bc2?pid=CAMF3DHJURPEMNRN&marketplace=FLIPKART')


# print(result['current_price'])