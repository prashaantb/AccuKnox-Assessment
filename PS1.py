from playwright.sync_api import sync_playwright
import time

BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
ADMIN_USERNAME = "Admin"
ADMIN_PASSWORD = "admin123"
NEW_USER_NAME = "testuser123"

def run_tests():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Login
        page.goto(BASE_URL)
        page.fill('input[name="username"]', ADMIN_USERNAME)
        page.fill('input[name="password"]', ADMIN_PASSWORD)
        page.click('button[type="submit"]')

        # Navigate to Admin
        page.click('a:has-text("Admin")')

        # Add New User
        page.click('button:has-text("Add")')
        page.fill('input[placeholder="Type for hints..."]', "John Freakin' Wick")
        time.sleep(1)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        page.locator('div[role="combobox"]').nth(1).click()
        page.get_by_text("Admin").click()
        page.locator('div[role="combobox"]').nth(2).click()
        page.get_by_text("Enabled").click()
        page.fill('input[name="username"]', NEW_USER_NAME)
        page.fill('input[name="password"]', "Test@1234")
        page.fill('input[name="confirmPassword"]', "Test@1234")
        page.click('button:has-text("Save")')

        # Search the user
        time.sleep(2)
        page.fill('input[placeholder="Username"]', NEW_USER_NAME)
        page.click('button:has-text("Search")')
        assert page.get_by_text(NEW_USER_NAME), "User not found"

        # Edit User
        page.click(f'xpath=//div[text()="{NEW_USER_NAME}"]/ancestor::div[contains(@class,"oxd-table-row")]/descendant::button[1]')
        time.sleep(1)
        page.locator('div[role="combobox"]').nth(1).click()
        page.get_by_text("ESS").click()
        page.click('button:has-text("Save")')
        time.sleep(1)

        # Validate Updates
        page.fill('input[placeholder="Username"]', NEW_USER_NAME)
        page.click('button:has-text("Search")')
        assert page.get_by_text("ESS"), "Role not updated"

        # Delete User
        page.click(f'xpath=//div[text()="{NEW_USER_NAME}"]/ancestor::div[contains(@class,"oxd-table-row")]/descendant::button[2]')
        page.click('button:has-text("Yes, Delete")')
        time.sleep(1)

        # Confirm deletion
        page.fill('input[placeholder="Username"]', NEW_USER_NAME)
        page.click('button:has-text("Search")')
        assert page.get_by_text("No Records Found"), "User not deleted"

        print("✅ All test cases passed.")

        browser.close()

if __name__ == "__main__":
    run_tests()
