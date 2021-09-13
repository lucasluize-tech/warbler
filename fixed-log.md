## Part One

1. **Understand Modeling**:

    Follows(model) is a many-to-many relational table where many users can follow and be followed.

2. **Fix Logout**

    Done. session.pop , flash and redirect implemented.

3. **Fix User Profile**

    Injected user location, bio and header_image to HTML templates

4. **Fix User Cards**

    Also Injected the user-bio into the necessary HTML templates

5. **Fix Profile Edit**

    Done.  check for global user, check for password, and commit changes to database.

6. **Fix Homepage**

    Done. Put together a list of user_ids from user.following, and filtered with IN.


7. *Fix Card-Bio on Following.html // Maybe this was extra.*

8. **Research and Understand Login Strategy:**
    - How is the logged in user being kept track of?
  
        > We add the user to session, using the user ID.

    - What is Flask's g object?
        > it stands for global object and it's used to access other objects easily
    
    - What is the purpose of add_user_to_g?
        > Makes global access to the data of logged in user.
    
    - What does @app.before_request mean?
        > It means this code will run before each request. So it will always add user to global.

## Part Two

1. Adding a like to user likes :  
    
    Done. Implemented add_like POST route, added user like to db.

2. Like or dislike :
   
   Done. if Like exist for user delete like, else create.(used same route)

3. Profile page :
   
   Done. Dynamic number of likes, and if clicked will render page with all liked messages.

## TIME :

Started Wednesday 09/08/21 10:00 am
Break same day at 3:00 pm

Restarted Monday 09/13/21 10:00 am
Endend Monday 09/13/21 5:15 pm



