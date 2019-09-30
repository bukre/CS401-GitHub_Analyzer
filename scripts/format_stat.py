#!/usr/bin/env python


class StatStruct:
    commit_hash = ""
    author_name = ""
    committer_name = ""
    commit_date = ""
    changed_files = []

    def __str__(self):
        return_value = "Commit hash: " + self.commit_hash +\
                       "\nAuthor name: " + self.author_name +\
                       "\nCommitter name: " + self.committer_name +\
                       "\nCommit date: " + self.commit_date +\
                       "\nChanged files: "
        for y in self.changed_files[:-1]:
            return_value += y + "|"
        return_value += self.changed_files[-1]
        return return_value


stat = open("stat.txt", "r")
commits = stat.read().split("#")
stats = []

# Take each commit as chunks of Strings. The new lines are indicated by '#' character in the bash file.
# Split the strings by '#' and then by '\n'. Remove any empty 'None' objects from the list.
# Final result. The first index of temp_string is the Git data, the rest is the changed files.
for x in commits[1:]:   # starting from 1 due to an empty string in index 0 caused by split '#'
    temp_stat = StatStruct()
    temp_string = list(filter(None, x.split("\n")))
    git_data_split = temp_string[0].split("|")
    temp_stat.commit_hash = git_data_split[0]
    temp_stat.author_name = git_data_split[1]
    temp_stat.committer_name = git_data_split[2]
    temp_stat.commit_date = git_data_split[3]
    temp_stat.changed_files = temp_string[1:]
    stats.append(temp_stat)


stat.close()
stat = open("stat.txt", "w")

for i in stats[:-1]:
    stat.write(i.__str__())
    stat.write("\n####################\n")
stat.write(stats[-1].__str__())

stat.close()
