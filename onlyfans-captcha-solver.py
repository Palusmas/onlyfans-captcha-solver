import capsolver
from urllib.parse import urlparse

# Change these values
PARSED_PROXY = "http://username:password@host:port"
capsolver.api_key = "Your pay per usage key"

def solve_recaptcha_v3_enterprise():
    solution = capsolver.solve({
        "type": "ReCaptchaV3EnterpriseTask",
        "websiteURL": "https://onlyfans.com",
        "websiteKey": "6LcvNcwdAAAAAMWAuNRXH74u3QePsEzTm6GEjx0J",
        "apiDomain": "www.recaptcha.net",
        "pageAction": "login",
        "proxy": PARSED_PROXY
    })
    return solution

def main():
    
    print("Solving onlyfans captcha")
    solution = solve_recaptcha_v3_enterprise()
    
    token = solution["gRecaptchaResponse"]
    
    print("Token Solution " + token)
    
if __name__ == "__main__":
    main()
