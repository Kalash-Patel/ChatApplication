For Registration 

http://localhost:8000/api/registration

username=admin@gmail.com  -> use username to register email
password=123456

if username already exist then it gives a message "Email already exists" if all correct then message "Registration Successfull"

<!--------------------Login ---------------------->


Login
http://localhost:8000/api/login

email=admin@gmail.com  -> use email to login
password=123456

if email or password or both incorrect then it gives a 'HTTP_400_BAD_REQUEST' if all correct then message "status.HTTP_200_OK"
and after login user add into the OnlineUsers model so that the user seen as online

<!--------------------online user ---------------------->

to see online user
http://localhost:8000/api/online-users/

it get the data from OnlineUsers where all the login user is visible which is save during successfully login their account -> open url 'http://localhost:8000/api/online-users' to see all online users

<!-------------------------------- ---------------------------->
If the recipient is online and available, return a success message or status code.
If the recipient is offline or unavailable, return an error message or status code.

http://localhost:8000/api/chat/start/

username = "<user_name>"
we pass username to the body so that we can check if that user is online or not if online the we message "Successfull" and when not "Not Successfull"

<!------------------------------ ---------------------------------->
http://localhost:8000/api/chat/send/<str:group_name>/

when we pass some string after send in url it refer as a group and the user who open same group with same link they can actually in the same group and send message in group to each other at same time and both user can see their message

"http://localhost:8080/api/chat/send/india"
 here india is a group name and the users who open this link they actually join the group "india" and they can chat with all other users who join this group but out of this group members no one can read or send a message of "india" group