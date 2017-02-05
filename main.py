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
        #Old Table
        # username = "<td class ='label'>""username""</td>"
        # username_row = "<tr>" + username + "</tr>"
        # password = "<td>""password""</td>"
        # password_row ="<tr>" + password + "</tr>"
        # verify_password = "<td>""Verify Password""</td>"
        # verify_password_row ="<tr>" + verify_password + "</tr>"
        # email = "<td>""email""</td>"
        # email_row ="<tr>" + email + "</tr>"
import webapp2
import re
#VALIDATION??
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username).group(0)
#TABLE ROW OUTLINE
def create_table_row(label,input, validation):
    label = "<td class ='label'>" + label + "</td>"
    input = "<td>" "<input type ='text' name= 'label' value =" + input + ">" + "</td>" #+ "</tr>"
    validation = "<td class = 'error'>" + str(valid_username(validation)) + "</tr>"
    #row_label_input = "<td>" "<input type='text' name='label' value =" + input + ">" + "</td>" + "</tr>"
    return label + input + validation #row_intermediate_step + row_label_input
#MAIN FUNCTION
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #Table row labels
        username = "Username"
        password = "Password"
        verify_password = "Verify Password"
        email = "Email (Optional)"
        #SAMPLE INPUTS
        test = "test"
        validation = 'test validation'
        #Table rows
        row_1 = create_table_row(username,"",test)
        row_2 = create_table_row(password,"",test)
        row_3 = create_table_row(verify_password,"",test)
        row_4 = create_table_row(email,"",test)
        #table structure
        table_body = ("<tbody>" + row_1 + row_2 + row_3 + row_4 + "</tbody>")
        table = "<table>" + table_body + "</table>"

        submit = "<input type='submit'/>"
        form = "<form>" + table + "</form>"
        #OTHER PARTS
        header = "<h2>User Signup</h2>"
        submit_button = "<input type= 'submit'/>"


        self.response.write(header + form + submit_button)

    #def post(self):
        #return "<h2>"Thanks for signing up"<h2>"

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
