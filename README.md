# Vulnerable-Login-Attack-Simulator  

![Vulnerable-Login-Attack-Simulator](https://scontent.fdac138-1.fna.fbcdn.net/v/t39.30808-6/472193249_122132934644552158_5447736108512529037_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=100&ccb=1-7&_nc_sid=127cfc&_nc_ohc=Y4Zm0VW0ebMQ7kNvgHwwMbt&_nc_zt=23&_nc_ht=scontent.fdac138-1.fna&_nc_gid=AcrxiLp1Jtq05FDgaDdMRNZ&oh=00_AYDYOsDzBHpe5jn-i0YviFcTyMF0YMf_cOMj7h6EqGkopg&oe=677CCB96)

Welcome to **Vulnerable-Login-Attack-Simulator**, a practical project to understand the basics of web application vulnerabilities and ethical hacking. This repository includes a vulnerable login page and Python scripts to exploit its weaknesses, providing a safe environment for learning web penetration testing techniques.  

---

## Features  
- **Vulnerable Login Page**: A Flask-based web application with a regex vulnerability in username validation.  
- **Exploitation Scripts**: Two Python scripts for testing attacks:
  - **Single Payload Attack**: Exploits the regex vulnerability in username validation.
  - **Brute Force Attack**: Tests a list of usernames and passwords to gain access.  
- **User-Friendly Code**: Clear and concise examples, suitable for beginners in cybersecurity.  

---

## How to Set Up  

### Prerequisites  
- Python 3.x installed on your system.  
- `Flask` and `requests` libraries (install using `pip`).  

### Installation Steps  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/Vulnerable-Login-Attack-Simulator.git
   ```
2. Navigate to the project directory:  
   ```bash
   cd Vulnerable-Login-Attack-Simulator
   ```
3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

4. Start the vulnerable login page:  
   ```bash
   python LoginPage_(1st open and run on vsCode)
   ```
   The app will run on `http://localhost:8080/login`.  

5. Run the attacking scripts as needed:
   ```bash
   cd Attack_(Open with other vsCode window)
   ```
   - **Single Payload Attack**: `Attacking_Code_(fixed--username).py`  
   - **Brute Force Attack**: `Attacking_Code_(not-fixed).py`  

---

## How to Use  

### Flask Application  
The login page accepts a username and password input, with a regex-based vulnerability in username validation. Use this page as the target for the provided attack scripts.  

### Attack Scripts  
1. **Single Payload Attack**  
   - Exploits the regex vulnerability by crafting a specific username to bypass validation.  
   - Run the script:  
     ```bash
     python Attacking_Code_(fixed--username).py
     ```

2. **Brute Force Attack**  
   - Iterates through a list of usernames and passwords to test possible combinations.  
   - Run the script:  
     ```bash
     python Attacking_Code_(not-fixed).py
     ```  

---

## Learning Objectives  
- Understand the role of regex validation in securing web forms.  
- Explore brute-force attacks and their impact on weak login systems.  
- Learn ethical hacking and basic web penetration testing techniques.  

---

## Contributions  
Contributions are welcome! If you'd like to enhance the scripts, improve the login application, or add new challenges, feel free to fork the repo and submit a pull request.  

---

## Disclaimer  
This repository is intended for educational purposes only. Always follow ethical guidelines and ensure you have permission before testing security vulnerabilities on any system.  

---

## License  
This project is licensed under the [MIT License](LICENSE).  
