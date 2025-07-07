import re
from playwright.sync_api import Page, expect, sync_playwright

# def test_example():
with sync_playwright() as p:
	browser = p.chromium.launch(headless=False)
	context = browser.new_context()
	page = context.new_page()
	page.goto("https://www.w3schools.com/")

	# Handle Google consent popup if present
	consent_selectors = [
		'button:has-text("I agree")',
		'button:has-text("Accept all")',
		'button:has-text("Accept")',
		'button[aria-label="Accept all"]',
		'button[aria-label="Accept"]',
		'text=I agree',
		'text=Accept all',
		'text=Accept',
		'button:has-text("Stay signed out")',
	]
	for selector in consent_selectors:
		try:
			if page.locator(selector).is_visible(timeout=3000):
				page.locator(selector).click()
				break
		except Exception:
			continue

	# Wait for the search box and search for 'playwright'
	page.get_by_role("button", name="Tutorials").click()
	page.get_by_label("Menu for tutorials").get_by_role("link", name="Learn JavaScript").click()
	expect(page.locator("h1")).to_contain_text("JavaScript Tutorial")
	# Verify the page title.
	if page.title() == "JavaScript Tutorial":
		print("Page title is correct")  
	else:
		print("Page title is incorrect")	

	# Wait for a Playwright link to be visible
	#expect(page.get_by_role("link", name=re.compile("Playwright", re.I))).to_be_visible()
	browser.close()


	