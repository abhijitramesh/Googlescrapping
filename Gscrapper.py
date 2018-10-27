import selenium.webdriver as webdriver
def get_result(serch_term):
	url = "https://www.google.com"
	browser = webdriver.Firefox()
	browser.get(url)
	serch_box = browser.find_element_by_id("lst-ib")
	serch_box.send_keys(serch_term)
	serch_box.submit()
	links = browser.find_element_by_xpath("//h3//a")
	results = []
	for i in links:
		href = links.get_attribute("href")
		print(href)
		results.append(href)
		browser.close()
		return results

get_result(input())