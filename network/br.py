from mechanize import Browser
browser = Browser()
response = browser.open('http://codewithharry.com')
print (response.code)
