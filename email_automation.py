#!/usr/bin/env python3
"""
Browser-Based Email Agent for AuditRAM Assignment

Usage:
    python email_agent.py --email YOUR_EMAIL --password YOUR_PASSWORD --to RECIPIENT --subject "SUBJECT" --body "BODY"

Dependencies:
    pip install selenium
"""

import sys
import time
import argparse
import subprocess
import os

def send_email_browser(login_email: str, password: str, to_addr: str, subject: str, body: str):
    """
    Send email using Selenium browser automation
    """
    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.chrome.service import Service as ChromeService
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import TimeoutException, NoSuchElementException
    except ImportError:
        print("\n✗ ERROR: Selenium not installed")
        print("Install with: pip install selenium")
        return False

    print("\n" + "="*60)
    print("BROWSER-BASED EMAIL AUTOMATION AGENT")
    print("="*60)
    
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    
    driver = None
    try:
        print("\n[1/6] Launching Chrome browser...")
        
        # Use Selenium Manager (built into Selenium 4.6+) - automatically handles ChromeDriver
        driver = webdriver.Chrome(options=options)
        print("      ✓ Browser launched successfully")
        
        wait = WebDriverWait(driver, 30)
        
        # Navigate to Gmail
        print("[2/6] Opening Gmail...")
        driver.get("https://mail.google.com/")
        time.sleep(3)
        
        # Check if already logged in
        try:
            compose_check = driver.find_element(By.XPATH, "//div[contains(text(), 'Compose')]")
            print("      ℹ Already logged in! Skipping login...")
        except NoSuchElementException:
            # Need to login
            print(f"[3/6] Logging in as {login_email}...")
            
            try:
                # Enter email
                email_field = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
                email_field.send_keys(login_email)
                time.sleep(1)
                email_field.send_keys(Keys.RETURN)
                time.sleep(4)
                
                # Enter password
                print("      Entering password...")
                password_field = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
                password_field.send_keys(password)
                time.sleep(1)
                password_field.send_keys(Keys.RETURN)
                
                print("      Waiting for Gmail to load...")
                time.sleep(10)
                
            except TimeoutException:
                print("\n✗ Login failed - Google may have blocked the attempt")
                print("\nKeeping browser open - please complete login manually...")
                input("After logging in, press Enter to continue...")
        
        # Wait for compose button
        print("[4/6] Looking for Compose button...")
        time.sleep(3)
        
        # Click Compose
        print("[5/6] Opening compose window...")
        try:
            compose_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Compose')]")))
            compose_btn.click()
            print("      ✓ Compose window opened")
            time.sleep(3)
        except Exception as e:
            print(f"      ✗ Could not find Compose button automatically")
            print("      Please click 'Compose' button manually in the browser...")
            input("Press Enter after clicking Compose...")
        
        # Fill recipient
        print("      Filling recipient...")
        try:
            to_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='To' or @name='to']")))
            to_field.send_keys(to_addr)
            print(f"      ✓ To: {to_addr}")
            time.sleep(1)
        except:
            # Try alternative selector
            try:
                to_field = driver.find_element(By.CSS_SELECTOR, "input[peoplekit-id='BbVjBd']")
                to_field.send_keys(to_addr)
                print(f"      ✓ To: {to_addr}")
            except Exception as e:
                print(f"      ⚠ Please fill recipient manually")
                input("Press Enter after filling recipient...")
        
        # Fill subject
        print("      Filling subject...")
        try:
            subject_field = driver.find_element(By.XPATH, "//input[@name='subjectbox']")
            subject_field.send_keys(subject)
            print(f"      ✓ Subject: {subject}")
            time.sleep(1)
        except Exception as e:
            print(f"      ⚠ Please fill subject manually")
            input("Press Enter after filling subject...")
        
        # Fill body
        print("      Filling email body...")
        try:
            body_field = driver.find_element(By.XPATH, "//div[@aria-label='Message Body']")
            body_field.click()
            time.sleep(0.5)
            body_field.send_keys(body)
            print(f"      ✓ Body filled")
            time.sleep(1)
        except:
            try:
                body_field = driver.find_element(By.CSS_SELECTOR, "div[role='textbox']")
                body_field.click()
                body_field.send_keys(body)
                print(f"      ✓ Body filled")
            except Exception as e:
                print(f"      ⚠ Please fill body manually")
                input("Press Enter after filling body...")
        
        # Send email
        print("\n[6/6] Sending email...")
        try:
            send_btn = driver.find_element(By.XPATH, "//div[@role='button' and contains(text(), 'Send')]")
            send_btn.click()
            print("      ✓ Send button clicked!")
        except:
            try:
                # Alternative: Use Tab + Enter
                driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + Keys.RETURN)
                print("      ✓ Send shortcut used (Ctrl+Enter)!")
            except:
                print("      ⚠ Please click Send button manually")
                input("Press Enter after clicking Send...")
        
        # Wait for confirmation
        print("\n      Waiting for confirmation...")
        time.sleep(4)
        
        try:
            confirmation = driver.find_element(By.XPATH, "//*[contains(text(), 'Message sent')]")
            print("\n" + "="*60)
            print("✅ EMAIL SENT SUCCESSFULLY!")
            print("="*60)
            time.sleep(2)
            return True
        except:
            print("\n" + "="*60)
            print("⚠ Please verify in browser if email was sent")
            print("="*60)
            input("\nPress Enter to close browser after verification...")
            return True
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        
        if driver:
            print("\n⚠ Browser will stay open for debugging")
            input("Press Enter to close...")
        
        return False
        
    finally:
        if driver:
            try:
                driver.quit()
            except:
                pass


def main():
    parser = argparse.ArgumentParser(description="Browser-Based Email Agent")
    
    parser.add_argument("--email", required=True, help="Your email address")
    parser.add_argument("--password", required=True, help="Your email password")
    parser.add_argument("--to", required=True, help="Recipient email")
    parser.add_argument("--subject", required=True, help="Email subject")
    parser.add_argument("--body", required=True, help="Email body")
    
    args = parser.parse_args()
    
    success = send_email_browser(args.email, args.password, args.to, args.subject, args.body)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()