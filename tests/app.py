from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)

    # Create a new page
    page = browser.new_page()

    # Visit the page
    page.goto("https://ifindcheaters.com")
    signin_button = page.get_by_role('button', name="sign in")

    #Find img
    page.get_by_alt_text("couple").highlight()

    #Fing Title
    page.get_by_title("Best Website to Find Out if Spouse is Cheating - Infidelity Website & App | iFindCheaters").highlight()


    #free_button = page.locator(".navigation__button.get-trial:text('try free')")
    signin_button.click()

    #Get the url
    print("Sign In", signin_button)

    browser.close()