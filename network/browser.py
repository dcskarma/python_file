import mechanize
br = mechanize.Browser()
page = br.open('http://syngress.com/')
s_code = page.read()
print (s_code)

