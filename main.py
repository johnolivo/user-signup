#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        username= "Joe"
        text_area = "<textarea>" + username + "</textarea>"
        #Table
        username = "<td>""username""</td>"
        username_row = "<tr>" + username + "</tr>"
        password = "<td>""password""</td>"
        password_row ="<tr>" + password + "</tr>"
        verify_password = "<td>""Verify Password""</td>"
        verify_password_row ="<tr>" + verify_password + "</tr>"
        email = "<td>""email""</td>"
        email_row ="<tr>" + email + "</tr>"

        table_body = "<tbody>" + username_row + password_row + verify_password_row + email_row + "</tbody>"
        table = "<table>" + table_body + "</table>"

        submit = "<input type='submit'/>"
        form = "<form>" + table + "</form>"
        self.response.write(form)

    #def post(self):
        #return "<h2>"Thanks for signing up"<h2>"

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
