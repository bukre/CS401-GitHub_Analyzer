#!/bin/bash
# Some Git Bash commands used
# H  = Commit hash
# an = Author name
# cn = Committer name
# cd = Commit date
# s  = Subject (which dir was edited)

###
# Functions
###

currentDir=$(pwd)

function formatData()
{
	git log --name-only --pretty=format:"#%H|%an|%cn|%cd|%s" > "$currentDir/FormattedData.txt" 2>&1
	cd "$currentDir"
	python format_data.py
}

function formatDataDateRestriction()
{
	echo TODO
}


###
# Main body of script starts here
###

if [ "$#" -eq 0 ]; then
	printf "Please enter a command.\nEx: git_data_collector.sh -h"
	exit
fi

if [[ "$@" = "-h" ]]; then
	echo "-log -> Generates log.txt file with commit history and commit notes."
	exit
fi

if [[ "$#" != 0 ]] && [[ "$@" != "-h" ]]; then
	dateString=""
	declare -a commands
	IFS=' '
	read -a commands <<< "$@" # parse the input for multiple commands
	cd ..
	for i in "${commands[@]}"
	do
		if [ "$i" = "-log" ]; then
			formatData
#		elif [[ "$i" = *after* ]] || [[ "$i" = *before* ]]; then
#			dateString="${dateString} $i"
		else
			printf "Command not recognized.\nList of all the commands: git_data_collector -h\n"
		fi
	done
	
#	if [[ -n $dateString ]]; then
#		createStatWithDateRestriction $dateString
#	fi

fi

exit
