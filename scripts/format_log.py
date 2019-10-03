#!/usr/bin/env python

import sys

class LogStruct:
    commit_hash = ""
    author_name = ""
    committer_name = ""
    commit_date = ""
    subject = ""

    def __str__(self):
        return_value = "Commit hash: " + self.commit_hash +\
                       "\nAuthor name: " + self.author_name +\
                       "\nCommitter name: " + self.committer_name +\
                       "\nCommit date: " + self.commit_date +\
                       "\nSubject: " + self.subject
        return return_value

log=None
if (len(sys.argv) > 1):
	log = open("logDateRestricted.txt", "r");
else:
	log = open("log.txt", "r")
logs = []
log_split = []

for x in log:
    log_split = x.split("|")
    temp = LogStruct()
    temp.commit_hash = log_split[0]
    temp.author_name = log_split[1]
    temp.committer_name = log_split[2]
    temp.commit_date = log_split[3]
    temp.subject = log_split[4]
    logs.append(temp)

log.close()

if (len(sys.argv) > 1):
	log = open("logDateRestricted.txt", "w");
else:
	log = open("log.txt", "w")

for x in logs[:-1]:
    log.write(x.__str__())
    log.write("####################\n")

log.write(logs[-1].__str__())

log.close()
