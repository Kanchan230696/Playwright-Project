from playwright.sync_api import sync_playwright, expect

def test_login():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://digiuiqa.wellboreintegrity.com/#!")
        page.locator("#LormalLogin").check()
        expect(page.locator("#LormalLogin")).to_be_checked()
        page.get_by_role("textbox", name="Email").fill("kanchan.gaikwad@invasystems.com")
        page.get_by_role("textbox", name="Password").fill("g7U-7.0U")
        page.get_by_role("button", name="Sign In").click()
        page.screenshot(path="login_screenshot.png")
        page.video.path("login_video.webm")
        page.inner_html("body")
        
        # browser.close()
        #https://www.google.com/


#how to call main function in pytest    
if __name__ == "__main__":
    test_login()