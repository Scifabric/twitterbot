# -*- coding: utf8 -*-
# This file is part of twitterbot.
#
# Copyright (C) 2019 Scifabric LTD.
#
# twitterbot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# twitterbot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with twitterbot.  If not, see <http://www.gnu.org/licenses/>.

from birdy.twitter import UserClient
import tweepy
from settings import CONSUMER_KEY, CONSUMER_SECRET
from settings import ACCESS_TOKEN, ACCESS_TOKEN_SECRET

client = UserClient(CONSUMER_KEY,
                    CONSUMER_SECRET,
                    ACCESS_TOKEN,
                    ACCESS_TOKEN_SECRET)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

client = tweepy.API(auth)
