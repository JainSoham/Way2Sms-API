# Way2Sms-API
This is free type of API (unofficial) that can be attached to website etc for sending Sms verification OTP or for marketing. Here you can enter all available login credential's to increse your message sending capacity.

## How to Use:
1. Clone this Repository (or download a zipped version)
2. Update a credentials.txt file in this folder. The first line of this file must have No. of Credentials you are providing and then in new line your username1 enclosed whithin two ^ characters. i.e. the second line must be ^username1^ and similarly, the third line of this file must be ^password1^ and then fourth & fifth line again are ^username2^ ^password2^. Provide as many username and password you have because per every UserName you have around 30 SMS ending capacity as per new update in website. 
3. Save this either in same directory of your project.

#### Way2Sms-API/credentials.txt (in the same folder as Sms_api.py):
```
i    (NO. of Credentials you are providing) 
^username1^
^password1^
^username2^
^password2^
..
^usernamei^
^passwordi^
```

#### Start with:
```python
import Sms_api
```
- Send SMS, print -> status of Message(Send or Not)
```python
Sms_api.sendmessage('Mobile_No','Message')
```
- Schedule Future SMS, print -> status of Message(Scheduled or Not)
```python
Sms_api.sendmessage('Mobile_No','Message','DD/HH/YYYY','HH:MM') #(HH:MM)(24Hr Format)(18:34)
```
##### Session will Logout Automatically after Sending or Scheduling SMS

#### Requires:
```
requests module
bs4 module
re module
```

# License
You are free to use any part of this code, as long as you credit the Author

# Author
Jain Soham Dungerchand, BITS Pilani.

**Free Messaging, Yeah!**
