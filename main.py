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

def create_table_row(label,input):
    row_label = "<td>" "<class ='label'>" + label + "</td>"
    row_intermediate_step = "<tr>" + row_label
    row_label_input = "<td>" "<input type='text' name='label' value =" + input + ">" + "</td>" + "</tr>"
    return row_intermediate_step + row_label_input

class MainHandler(webapp2.RequestHandler):
    def get(self):
        username = "Username"
        password = "Password"
        verify_password = "Verify Password"
        email = "Email (Optional)"
        #text_area = "<textarea>" + username + "</textarea>"
        test = "Hello"
        #TableTest
        row_1 = create_table_row(username,test)
        row_2 = create_table_row(password,test)
        row_3 = create_table_row(verify_password,test)
        row_4 = create_table_row(email,test)
        #Table
        username = "<td class ='label'>""username""</td>"
        username_row = "<tr>" + username + "</tr>"
        password = "<td>""password""</td>"
        password_row ="<tr>" + password + "</tr>"
        verify_password = "<td>""Verify Password""</td>"
        verify_password_row ="<tr>" + verify_password + "</tr>"
        email = "<td>""email""</td>"
        email_row ="<tr>" + email + "</tr>"

        table_body = ("<tbody>" + username_row + password_row + verify_password_row + email_row +
        row_1 + row_2 + row_3 + row_4 +

        "</tbody>")
        table = "<table>" + table_body + "</table>"

        submit = "<input type='submit'/>"
        form = "<form>" + table + "</form>"
        self.response.write(form)

    #def post(self):
        #return "<h2>"Thanks for signing up"<h2>"

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
