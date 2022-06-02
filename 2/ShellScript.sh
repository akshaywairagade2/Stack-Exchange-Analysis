#!/bin/bash
# Program to count the number of different Badges and the number of users per badge.
echo -e '\n\n'
echo "The count of number of users per batch is:-"
cat Badges.xml | awk '/(Name=")(.*")/{print "\t" $4}' | sort -t '=' -k 2 | uniq -c | sort -t '=' -k 1 | sed 's/Name=//g'
echo -e '\n\n'
echo "The total number of badges are:-"
cat Badges.xml | awk '/(Name=")(.*")/{print $4}' | sort -t '=' -k 2 | uniq -c | sort -t '=' -k 1 | wc -l
