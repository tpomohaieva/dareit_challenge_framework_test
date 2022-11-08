# Task 1: software configuration

## Subtask 1: Why did I choose to participate in the Dare IT Challenge?

I'm always up to new challenges and constant learning. 
My journey in IT started with technical support role, and then I slowly transitioned in software development (frontend). Since automation QA would require both coding and soft skills 
I thought Dare IT challenge is something I want to try myself in.
I trust this challenge will bring me lots of knowledge and new acquaintances.

---

# Task 2: selectors

1. #### login_form_xpath
   - `//*[@id="__next"]/form`
   - `//*[contains(@class,"jss")][1]`
   - `//child::div/form`

2. #### login_form_title_xpath
   - `//*[@id="__next"]//h5`
   - `//h5[contains(text(), 'Scouts Panel')]`
   - `//child::form//h5`
  
3. #### login_input_xpath
    - `//*[@id="login"]`
    - `//input[@id="login"]`
    - `//child::form//*[@id="login"]` 
    - `//form//*[@id="login"]`
  
4. #### password_input_xpath
    - `//*[@id="password"]`
    - `//input[@id="password"]`
    - `//input[@name="password"]`
    - `//child::form//*[@id="password"]` 
    - `//form//*[@type="password"]`
  
5. #### remind_password_hyperlink_xpath
    - `//*[@id="__next"]/form/div/div[1]/a`
    - `//*[text()="Remind password"]`
    - `//child::div/a`
    - `//child::form//a`

6. #### sign_in_btn_xpath
    - `//*[@id="__next"]/form//button`
    - `//form//button`
    - `//*[@type='submit']`
    - `//*[text()="Sign in"]/parent::*`
  
7. #### select_language_btn_xpath
    - `//*[@id="__next"]//*[contains(@class, 'select')]`
    - `//form//*[@role='button']`
    - `//child::form//*[@role='button']`