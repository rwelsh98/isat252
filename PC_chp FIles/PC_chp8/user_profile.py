"""
Your module description
"""
#Using arbitrary keyword arguments
def buildprofile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name']=first.title()
    user_info['last_name']=last.title()
    return user_info
    
user_profile=buildprofile('albert','einstein',location='princeton',field='physics')

print(user_profile)