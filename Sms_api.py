import sys, re, os, cgi
###Trying To import Required module### 
try:

	import requests

	print('Requests Modue exist')

except:

	sys.exit("\n\tModule ERROR:\n\t\'Requests\' module not installed.\n\run $sudo pip install requests")


try:

	from bs4 import BeautifulSoup

	print('BeautifulSoup4 Module Exist')

except:

	sys.exit("\n\tModule ERROR:\n\t\'bs4\' module not installed.\n\run $sudo pip install bs4")


###Trying To import Required module (end)### 



### Here we will login using provided credentials in credentials.txt by checking condition of how many messages are sent from given username### 

def login():

	try:

		credentials = open('credentials.txt','r')

		content = credentials.read()

		credentials = re.findall('(?<=\^)(\S+)(?=\^)',content)

		try:

			j  = re.search('\d+',content)

			i = int(j.group())

		except:
			{sys.exit("\nNo. of credentials are not given ")}

	except:
		sys.exit("\n\tFile ERROR:\n\tProblem reading the credentials.txt file.\n\tCheck if file exists.")

	print('Credentials Opened Successfully.')

	print('Checking Credentials.')

	if len(credentials) < (2*i):
		
		sys.exit("Problem with credentials.txt file.\nMake sure that you have entered both the username and password.")
		
	else:
		
		print(str(i) + '.  No. of Credentials are given')

	loginurl = 'http://site21.way2sms.com/Login1.action'
	
	k = 0
	
	while k < i:

		username = credentials[2*k]
		
		password = credentials[2*k+1]

		login_data = {'username': username,'password': password,'button': 'Login',}

		session = requests.Session()

		main = session.post(loginurl, data=login_data,timeout=100)

		sessionid = session.cookies.get_dict()['JSESSIONID'][4:]

		sent = messagesent(session,sessionid)

		if sent<29:

			break

		else:

			k=k+1

	if(k==i):

		sys.exit('Today\'s Quota Completed \n please add some more credentials')

	else:

		print('Successfully Logged In')

	return session,sessionid



#### This is for checking how messages are sent from given Username And Password ###
############### It's called only at the time of LogIn##########################


def messagesent(session,sessionid):

	sent_url = 'http://site21.way2sms.com/sentSMS?Token='+sessionid

	sent = session.get(sent_url,timeout=100)

	sentsoup = BeautifulSoup(sent.text,"html.parser")

	t = sentsoup.find("div",{"class":"hed"})

	sent = re.search('(Sent SMS \()(\d+)',str(t))

	sent = int(sent.group(2))

	return sent

	


################ This method will be called by the User for sending message ####################
################# It requires Mobile No. and message in ' '  ######################## 


def sendmessage(mobile,msg):

	if len(msg)>139 or len(mobile)!=10:

		sys.exit('\t Enter Message of len < 139 and\n\t Mobile No. correctly ')

	session,sessionid = login()

	payload={'ssaction':'ss','Token':sessionid,'mobile':mobile,'message':msg,'msgLen':'129'}

	msg_url='http://site21.way2sms.com/smstoss.action'

	send = session.post(msg_url,data=payload,timeout=100)

	status = re.search('(status=)(\d)',send.url)

	status = int(status.group(2))

	if status == 0:

		print('Message Sent Successfully')

	elif status == 3:

		print('Enter Correct Information')

	elif status == 8:

		print('No. registered as DND ')

	elif status == 6:

		print('This Mobile Quota Completed')

	logout(session)




################ This method will be called by the User for Scheduling Future Message ####################
################# It requires Mobile No., Message , Date(DD/MM/YYYY)ie.(08/08/2017) format  and Time(HH:MM)ie.(18:34) 24Hr Format in  ' '  ######################## 

def futuresms(mobile,msg,date,hh):

	if len(msg)>139 or len(mobile)!=10:

		sys.exit('\t Enter Message of len < 139 and\n\t Mobile No. correctly ')

	session,sessionid = login()

	payload={'Token':sessionid,'mobile':mobile,'sdate':date,'stime':hh,'message':msg,'msgLen':'138'}
	
	future_msg_url='http://site21.way2sms.com/schedulesms.action'

	future = session.post(future_msg_url,data=payload)

	status = re.search('(status=)(\d+)',future.url)

	status = int(status.group(2))

	if status == 10:

		print('Message Scheduled Successfully')

	elif status == 13:

		print('Message should be Scheduled within 30 Days')

	logout(session)



############### This function is called at end to get Logout of Our Session. ############
	
def logout(session):

	logout_url = 'http://site21.way2sms.com/main.action?'

	session.get(logout_url)

	session.close()

	print('Successfully Logged OUT')



######################.   Completed ######################



	
    