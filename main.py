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

        # def create_table_row(label,input):
        #     label = "<td class ='label'>" + label + "</td>"
        #     input = "<td>" "<input type ='text' name= 'label' value =" + input + ">" + "</td>" + "</tr>"
        #     #validation = "<td class = 'error'>" + valid_input(validation) + "</tr>"
        #     #row_label_input = "<td>" "<input type='text' name='label' value =" + input + ">" + "</td>" + "</tr>"
        #     return label + input #row_intermediate_step + row_label_input
        # def create_table_row_with_validation(label,input, validation):
        #     label = "<td class ='label'>" + label + "</td>"
        #     input = "<td>" "<input type ='text' name= 'label' value =" + input + ">" + "</td>" #+ "</tr>"
        #     validation = "<td class = 'error'>" + valid_input(validation) + "</tr>"
        #     #row_label_input = "<td>" "<input type='text' name='label' value =" + input + ">" + "</td>" + "</tr>"
        #     return label + input + validation

    #     #Table row labels
    #     username = "Username"
    #     password = "Password"
    #     verify_password = "Verify Password"
    #     email = "Email (Optional)"
    #     #Table rows
    #     row_1 = create_table_row(username,"")
    #     row_2 = create_table_row(password,"")
    #     row_3 = create_table_row(verify_password,"")
    #     row_4 = create_table_row(email,"")
    #     #table structure
    #     table_body = ("<tbody>" + row_1 + row_2 + row_3 + row_4 + "</tbody>")
    #     table = "<table>" + table_body + "</table>"
    #
    #     submit = "<input type='submit'/>"
    #     form = "<form>" + table + submit + "</form>"
    #     #OTHER PARTS
    #     header = "<h2>User Signup</h2>"
    #     self.response.write(header + form)
    #
    # def get(post):
    #     #Table row labels
    #     username = "Username"
    #     password = "Password"
    #     verify_password = "Verify Password"
    #     email = "Email (Optional)"
    #     #SAMPLE INPUTS
    #     test = "test"
    #     validation = 'test validation'
    #     #Table rows
    #     row_1 = create_table_row_with_validation(username,"", validation)
    #     row_2 = create_table_row_with_validation(password,"", validation)
    #     row_3 = create_table_row_with_validation(verify_password,"", validation)
    #     row_4 = create_table_row_with_validation(email,"", validation)
    #     #table structure
    #     table_body = ("<tbody>" + row_1 + row_2 + row_3 + row_4 + "</tbody>")
    #     table = "<table>" + table_body + "</table>"
    #
    #     submit = "<input type='submit'/>"
    #     form = "<form>" + table + submit + "</form>"
    #     #OTHER PARTS
    #     header = "<h2>User Signup</h2>"
    #     post.response.write(header + form)


    #def post(self):
        #return "<h2>"Thanks for signing up"<h2>"
import webapp2
import re
#Form
form ="""
<title>
Sign Up
</title>
    <body>
        <h2>
            Welcome! Please enter your information below
        </h2>
        <form method = 'post'>
            <table>
                <tbody>
                    <tr>
                        <td class = 'label'>Username</td>
                        <td><input type = 'text' name = username value = "%(username)s"></td>
                        <td class = 'error'>
                            <div>%(Uerror)s </div>
                        </td>
                    </tr>
                    <tr>
                        <td class = 'label'>Password</td>
                        <td><input type = 'password' name = password value = "%(password)s"></td>
                        <td class = 'error'>
                            <div>%(Perror)s </div>
                        </td>
                    </tr>
                    <tr>
                        <td class = 'label'>Verify Password</td>
                        <td><input type = 'password' name = verify_password value ="%(verify_password)s"></td>
                        <td class = 'error'>
                        <div>%(VPerror)s </div>
                        </td>
                    </tr>
                    <tr>
                        <td class = 'label'>Email (Optional)</td>
                        <td><input type = 'text' name = email value = "%(email)s"></td>
                        <td class = 'error'>
                        <div>%(Eerror)s </div>
                        </td>
                    </tr>
                <tbody>
            </table>
        <input type = 'submit'>
    </form>
</body>"""
#Validation functions
username_validation = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
pasword_validation = re.compile("^.{3,20}$")
email_validation = re.compile("^[\S]+@[\S]+.[\S]+$")
def validate_username(username):
    return username_validation.match(username)
def validate_password(password):
    return username_validation.match(password)
def validate_email(email):
    return not email or email_validation.match(email)
#Web Pages
class MainHandler(webapp2.RequestHandler):
    def write_form(self, Uerror="", Perror="", VPerror="", Eerror="", username="", password="", verify_password="", email=""):
        self.response.out.write(form % {"Uerror": Uerror,
                                        "Perror": Perror,
                                        "VPerror": VPerror,
                                        "Eerror": Eerror,
                                        "username": username,
                                        "password": password,
                                        "verify_password": verify_password,
                                        "email": email})

    def get(self):
        self.write_form()

    def post(self):
        #Gather inputs
        username_input = self.request.get('username')
        password_input = self.request.get('password')
        verify_password_input = self.request.get('verify_password')
        email_input = self.request.get('email')
        #define which inputs are valid
        valid_username = validate_username(username_input)
        valid_password = validate_password(password_input)
        valid_verify_password = validate_password(verify_password_input)
        valid_email = validate_email(email_input)
        #What happens when there is an error
        have_error = False
        params = dict(username = username_input, email = email_input)
        if not (username_input and valid_username):
            params ['Uerror'] = "Please enter a valid username"
            have_error = True
        if not valid_password:
            params ['Perror'] = "Please enter a valid password"
            have_error = True
        if not valid_verify_password:
            params ['VPerror'] = "Passwords do not match"
            have_error = True
        if not (valid_email):
            params ['Eerror'] = "Please enter a valid email"
            have_error = True
        if have_error:
            self.write_form(**params)

        else:
            self.response.write("<h2>" + 'Thanks for signing up! ' + username_input + "</h2>")


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
