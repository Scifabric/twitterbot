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

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from helpers import check_empty, download_file
from ssnntwitter import client
from settings import URL, JSON_KEYFILE_NAME

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    JSON_KEYFILE_NAME, scope)

gc = gspread.authorize(credentials)

data = gc.open_by_url(URL)

projects = data.worksheets()


dashboard = projects.pop(0)

project_names = [p.title for p in projects]
last_project = dashboard.acell('A1').value
current_project_idx = 0

current_project_idx = project_names.index(last_project) + 1

if current_project_idx >= len(project_names):
    current_project_idx = 0

candidate = "%s" % project_names[current_project_idx]
p = data.worksheet(candidate)
tmp = p.find('last')
row = tmp.row + 1
tweet = p.cell(row, 1).value
if check_empty(tweet):
    row = 1
if row == 1:
    tweet = p.cell(row, 1).value

tweet_media = p.cell(row, 3).value
local_filename = None
if not check_empty(tweet_media):
    local_filename = download_file(tweet_media)

p.update_cell(tmp.row, 2, '')
p.update_cell(row, 2, 'last')

# Rotate sheets
dashboard.update_acell('A1', p.title)

print(local_filename)

if local_filename is None:
    print("Tweeting without image")
    client.update_status(status=tweet)
else:
    print("Tweeting with image")
    client.update_with_media(filename=local_filename, status=tweet)

print(tweet)
