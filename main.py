from amazon import scrape as scrape_amazon
from flipkart import scrape as scrape_flipkart

print("Enter the url of the product(Amazon): ")
amazon_url = input()

print('\n------------------------------------------------------------------------------------------------\n')

print("Enter the url of the product(Flipkart): ")
flipkart_url = input()

print('\n------------------------------------------------------------------------------------------------\n')


print("       AMAZON \n ---------------------")

print(amazon_url)


amazon_product = scrape_amazon(amazon_url)
print('------------------------------------------------------------------------------------------------')

print('\n')
print("       FLIPKART \n ---------------------")

# print("Product details(Amazon):", amazon_product)

flipkart_product = scrape_flipkart(flipkart_url)

print('\n')
print('------------------------------------------------------------------------------------------------')
# print("Product details(Flipkart):", flipkart_product)

print("Price on amazon:",amazon_product['current_price'])


print("Price on flipkart:",flipkart_product['current_price'])




print('\n')

print('------------------------------------------------------------------------------------------------')




# print(result['current_price'])

if amazon_product['current_price'] < flipkart_product['current_price']:
    print("This product is available on amazon for the best price")
else:
    print("This product is available on flipkart for the best price")

print('\n------------------------------------------------------------------------------------------------')

