# Get credentials
import sys
val_username = sys.argv[1]
val_password = sys.argv[2]

# Start forever loop until all the comments are actually gone
while True:

	# Kill existing marionette processes, if any
	# This script expects use to be on Ubuntu 22.04, and have Firefox Marionette installed
	import os
	os.system('kill -9 $(ps -x | grep mario) 2>/dev/null')

	# Importing required libraries
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.common.by import By
	from time import sleep

	# Create a new Firefox driver instance
	driver = webdriver.Firefox()
	try:
		try:
			# Navigate to the webpage with the element to click
			driver.get("https://www.instagram.com/accounts/login/")
			sleep(3) # allow loading

			username = driver.find_element("xpath", '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input')
			username.send_keys(val_username)
			password = driver.find_element("xpath", '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input')
			password.send_keys(val_password)
			to_2fa = driver.find_element("xpath", '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button')
			to_2fa.click()
		except Exception as e:
			print("Error caught: "+str(e))

		# Authenticator 2FA buffer time
		sleep(20)

		# Open comments history
		driver.get("https://www.instagram.com/your_activity/interactions/comments")
		sleep(7) # allow loading

		while True:
			try:
				# Initialize body for scrolling
				body = driver.find_element(By.TAG_NAME,'body')

				for i in range(80):
					# Toggle on selection mode
					select_text = driver.find_element("xpath", "//*[contains(text(), 'Select')]")
					select_text.click()
					sleep(2) # allow loading

					# Start selecting
					targeted_style = 'mask-image: url("https://i.instagram.com/static/images/bloks/icons/generated/circle__outline__24-4x.png/2f71074dce25.png"); mask-size: contain; background-color: rgb(54, 54, 54); flex-shrink: 0; width: 24px; height: 24px;'
					focused_comments = driver.find_elements("xpath", f"//div[@style='{targeted_style}']")
					# 10 comments at a time
					for i in range(10):
						click_success = False
						click_tries = 3
						while not click_success and click_tries >= 0:
							try:
								focused_comments[i].click()
								click_success = True
							except:
								click_tries -= 1
								body.send_keys(Keys.PAGE_DOWN)
								sleep(.8)

					# Delete
					delete_button = driver.find_element("xpath", "//*[contains(text(), 'Delete')]")
					delete_button.click()

					# Delete confirm
					delete_confirm = driver.find_element("xpath", "//div[@class='_aacl _aacp _aacw _aac- _aad6']")
					delete_confirm.click()

					sleep(12)

				# Close the driver instance
				driver.quit()
				os.system('notify-send "Script Execution Completed" "Please check output for debugging"')

			# Exception when IG says something failed, and gives that alert with the OK button
			except Exception as e:
				print("Error caught: "+str(e))
				print("\nRestarting\n")
				sleep(15)
				restart_button = driver.find_element("xpath", "//*[contains(text(), 'OK')]")
				restart_button.click()
				sleep(15)
	# If the previous exception still faced an exception, restart the whole script again
	except:
		driver.quit()
		os.system("notify-send \"Script restarting, requires IG 2FA again\" \"Enter Ctrl-C in the console that this script is running on to force stop script running.\"")
