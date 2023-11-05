import requests
# import sys

def scrape(url):
    # url = 'https://www.amazon.in/Maybelline-Sensational-Waterproof-Lengthening-Volumizing/dp/B08H46YXYH/ref=pd_sbs_sccl_3_6/258-8342757-5026844?pd_rd_w=RsWlr&content-id=amzn1.sym.fdedbc61-3064-4c21-85ae-8ccd58c778a7&pf_rd_p=fdedbc61-3064-4c21-85ae-8ccd58c778a7&pf_rd_r=W0KK96D6CNNGHNS4NPP2&pd_rd_wg=YEXyP&pd_rd_r=52acea9b-532e-4707-aed4-202ee1f95e2e&pd_rd_i=B08H46YXYH&psc=1'
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0'

    headers = {
        'User-Agent': user_agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language':'en-US,en;q=0.5',
        'Connection':'keep-alive'
    }

    r = requests.get(url,headers=headers)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.content, 'html5lib')


    # print(r.content)

    title = soup.find('span', attrs = {'id':'productTitle'}).string.strip()
    current_price = soup.select('#corePriceDisplay_desktop_feature_div .reinventPricePriceToPayMargin > [aria-hidden] > .a-price-whole')[0].text.strip()
    # current_price = soup.select('.a-price .aok-align-center .reinventPricePriceToPayMargin .priceToPay')
    mrp_selector = soup.select('.a-price.a-text-price[data-a-strike=true] > [aria-hidden]')
    mrp = "0"
    if(mrp_selector):
        mrp = mrp_selector[0].text.strip()
        scraped_mrp = mrp.replace("₹","")
    
    review_count = soup.find('span', attrs = {'id':'acrCustomerReviewText'}).string.strip()
    rating = soup.select('.a-popover-trigger.a-declarative .a-size-base.a-color-base')[0].text.strip()


    print("Title: ",title)
    print("Current Price of the product: ",current_price)
    if(mrp!="0"):
        print("MRP of the product: ",scraped_mrp)
    else:
        print("MRP of the product: ",current_price)

    print("Review count of the product: ",review_count)
    print("Rating of the product: ",rating)

    return{
        'title': title,
        'current_price': current_price,
        'mrp': mrp,
        'review_count': review_count,
        'rating': rating
    }

# result = scrape('https://www.amazon.in/Canon-EOS-200D-II-Digital/dp/B07RJWB548/ref=sr_1_3?keywords=Canon%2BEOS%2B3000D%2BDSLR%2BCamera%2B1%2BCamera%2BBody%2C%2B18%2B-%2B55%2Bmm%2BLens%2B(Black)%23JustHere&nsdOptOutParam=true&qid=1698927570&sr=8-3&th=1')


# print(result['current_price'])





# urls = ["https://www.amazon.in/Maybelline-Sensational-Liquid-Lipstick-Nuance/dp/B099FNN755/?_encoding=UTF8&pd_rd_w=oMBHd&content-id=amzn1.sym.9020bbe5-8455-43c1-b13b-75bfbd7b2030&pf_rd_p=9020bbe5-8455-43c1-b13b-75bfbd7b2030&pf_rd_r=ER6KG665QTNZB6KY38XZ&pd_rd_wg=LPq76&pd_rd_r=6bab0c6c-8a3d-4681-aebe-ccf81e5410d0&ref_=pd_gw_Beauty&th=1", "https://www.amazon.in/dp/B00D2XGT8Y/ref=emc_b_5_i?th=1", "https://www.amazon.in/Maybelline-Sensational-Waterproof-Lengthening-Volumizing/dp/B08H46YXYH/ref=pd_sbs_sccl_3_6/258-8342757-5026844?pd_rd_w=RsWlr&content-id=amzn1.sym.fdedbc61-3064-4c21-85ae-8ccd58c778a7&pf_rd_p=fdedbc61-3064-4c21-85ae-8ccd58c778a7&pf_rd_r=W0KK96D6CNNGHNS4NPP2&pd_rd_wg=YEXyP&pd_rd_r=52acea9b-532e-4707-aed4-202ee1f95e2e&pd_rd_i=B08H46YXYH&psc=1", " https://www.amazon.in/dp/B07R6QKWZ5/ref=sspa_dk_detail_5?psc=1&pd_rd_i=B07R6QKWZ5&pd_rd_w=4EX3d&content-id=amzn1.sym.0fcdb56a-738b-4621-9da7-d47193883987&pf_rd_p=0fcdb56a-738b-4621-9da7-d47193883987&pf_rd_r=462F7PWHBQ92R73CFMC4&pd_rd_wg=RQcDQ&pd_rd_r=aecef37b-90d6-47a3-8e71-0fd655f7144d&s=beauty&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWwy", "https://www.amazon.in/dp/B0C53W7WJR/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B0C53W7WJR&pd_rd_w=InsSb&content-id=amzn1.sym.0fcdb56a-738b-4621-9da7-d47193883987&pf_rd_p=0fcdb56a-738b-4621-9da7-d47193883987&pf_rd_r=DK2NAMAJD5WBAYAAS5G2&pd_rd_wg=d6Xsq&pd_rd_r=4c28e109-6cf0-445a-b79d-670634b6d0aa&s=beauty&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWwy"]


# count = 0
# for x in urls:
#     scrape(x)

# scrape_amazon('https://www.amazon.in/Maybelline-Sensational-Liquid-Lipstick-Nuance/dp/B099FNN755/?_encoding=UTF8&pd_rd_w=oMBHd&content-id=amzn1.sym.9020bbe5-8455-43c1-b13b-75bfbd7b2030&pf_rd_p=9020bbe5-8455-43c1-b13b-75bfbd7b2030&pf_rd_r=ER6KG665QTNZB6KY38XZ&pd_rd_wg=LPq76&pd_rd_r=6bab0c6c-8a3d-4681-aebe-ccf81e5410d0&ref_=pd_gw_Beauty')

# sys.modules[__name__] = scrape_amazon


