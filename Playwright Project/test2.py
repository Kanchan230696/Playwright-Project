import re
from playwright.sync_api import Page, expect, sync_playwright

# def test_example():
with sync_playwright() as p:
	browser = p.chromium.launch(headless=False)
	context = browser.new_context()
	page = context.new_page()
	page.goto("https://www.google.com/")

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
	search_box = page.get_by_role("combobox", name="Search")
	search_box.wait_for(state="visible", timeout=15000)
	search_box.click()
	search_box.fill('playwright')
	search_box.press('Enter')
	page.get_by_role("link", name="Playwright: Fast and reliable").click()
	expect(page.get_by_label("Main", exact=True).get_by_role("link")).to_contain_text("Playwright")

	# Wait for a Playwright link to be visible
	#expect(page.get_by_role("link", name=re.compile("Playwright", re.I))).to_be_visible()
	browser.close()


	