#!/usr/bin/python
# This script is used to the Get gerrit Diff code using the REST API and
# copies that to the FOSSID server for scanning
import os
import sys
import re
import paramiko
from requests.auth import HTTPBasicAuth
from pygerrit.rest import GerritRestAPI
from paramiko import SSHClient
from scp import SCPClient
from requests.exceptions import RequestException
# Getting all the Gerrit required parameters
GERRIT_CHANGE_ID = sys.argv[1]
GERRIT_PATCHSET_REVISION = sys.argv[2]
GERRIT_PROJECT = sys.argv[3]
print GERRIT_PATCHSET_REVISION
print GERRIT_CHANGE_ID
print GERRIT_PROJECT
# Getting the Username and password for Gerrit from Jenkins
GERRIT_USERNAME = sys.argv[4]
GERRIT_PASSWORD = sys.argv[5]
print GERRIT_USERNAME
print GERRIT_PASSWORD
# Getting the Jenkins home variable
JENKINS_HOME = sys.argv[6]
print JENKINS_HOME
# Getting Gerrit Environment details
GERRIT_ENV = sys.argv[7]
print GERRIT_ENV

# Connecting to the Gerrit using the authentication
auth = HTTPBasicAuth(GERRIT_USERNAME, GERRIT_PASSWORD)
rest = GerritRestAPI(url='https://' + GERRIT_ENV, auth=auth)
try:
    # Getting the Gerrit Patch set using the REST API
    CHANGES = rest.get("changes/{0}/revisions/{1}/patch".format(
        GERRIT_CHANGE_ID, GERRIT_PATCHSET_REVISION))
except RequestException as error:
    print error
    exit(1)
print CHANGES

try:
    # Saving the Diff on the Jenkins server.
    f = open("Patchset.txt", "w")
    f.write(CHANGES.encode('utf8'))
except IOError as error:
    print "The exceptions are"
    print error
    exit(1)
except NameError as error:
    print "The exceptions are"
    print error
    exit(1)
print "This file patchset details are saved. That step is done"

# Need to search for the ticket type in  Subject: word in the file
print "The Ticket Type used for the specific changeset "
try:
    term = "Subject:"
    f = open("Patchset.txt", "r")
    for x in f:
      if term in x:
        data = x
    f.close()
except IOError as error:
    print "The exceptions are"
    print error
    exit(1)
except NameError as error:
    print "The exceptions are"
    print error
    exit(1)
print data
print "Step to check and accept only specific Ticket Types: DELIA, RDKALL, RDKB, XRE, RDK"
data = data.split()
ticketnumber = data[2]
ticketnumber = ticketnumber.split('-')
tickettype = ticketnumber[0]
print tickettype
validticket = ["DELIA","RDKALL","RDKB","XRE","RDK"]
if tickettype in validticket:
 print "THIS IS A VALID TICKET"
else:
 print "This is NOT A VALID TICKET TYPE"
