# Copyright (c) 2022 Mohamed Morsi
#
# This file is part of Mohamed Morsi's InstaBot Repository.
#
# InstaBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# InstaBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with InstaBot. If not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

############################################################################################################
############################################################################################################
# 					      Main program                                                 #
############################################################################################################
############################################################################################################
#!/usr/bin/env python3

from instapy import InstaPy
from instapy import smart_run


# login credentials
insta_username = ''
insta_password = ''



print( """
 /$$$$$$                       /$$               /$$$$$$$              /$$    
|_  $$_/                      | $$              | $$__  $$            | $$    
  | $$   /$$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$ | $$  \ $$  /$$$$$$  /$$$$$$  
  | $$  | $$__  $$ /$$_____/|_  $$_/   |____  $$| $$$$$$$  /$$__  $$|_  $$_/  
  | $$  | $$  \ $$|  $$$$$$   | $$      /$$$$$$$| $$__  $$| $$  \ $$  | $$    
  | $$  | $$  | $$ \____  $$  | $$ /$$ /$$__  $$| $$  \ $$| $$  | $$  | $$ /$$
 /$$$$$$| $$  | $$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$/  |  $$$$/
 |______/|__/  |__/|_______/    \___/   \_______/|_______/  \______/    \___/  
																																							
																																							
																																																					
	""")
session = InstaPy(username=insta_username, 
				password=insta_password, 
				headless_browser=False)

with smart_run(session):
		
	session.set_relationship_bounds(enabled=True,
					delimit_by_numbers=True,
					max_followers=14743,
					min_followers=8253,
					min_following=287)

	
	tags = ['twitter', 'netflix', 'instagram', 'whatsapp', 'tiktok', 'meta','pinterest','buzzfeed','vsco','spotify']
	session.follow_by_list(tags, sleep_delay=600, interact=False)
	
	session.follow_user_followers(['messenger','tumblr','medium','facebookapp'], amount=2, randomize=False, interact=False)

	session.unfollow_users( amount=18, custom_list_param='all', instapy_followed_enabled=True, nonFollowers=True, allFollowing=True)
	



	
