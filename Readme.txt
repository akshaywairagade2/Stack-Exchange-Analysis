Dataset Collected from  https://archive.org/details/stackexchange

Used Map Reduce technique for analyzing this huge dataset.

Used Hadoop for parallel processing and analyzed huge quantity of data using 5 cluster.

Here are the few things we analyzed according to the folder numbers provided.
1.Analyzed the fields in each file to create a "schema".

2.Using simple shell commands, (grep, wc, sort, uniq, awk etc.) I counted the number of different Badges and the number of users per badge in the Badges.xml file. Prepared the script to run in parallel using Hadoop streaming.

3.Used the posts.xml file to analyze below things.

A.)Analyzed the popularity of tags (how many posts used each of the tags).
B.) Calculated the View Count Distribution (How many posts were viewed a given number of times). Identified the top 10 most viewed posts on DataScienceExchange.
C.)Calculated the number of Posts per Hour of the day, for each of the 24 hours. (Tells us how the user activity varies.) Also calculated the ratio of the peak to lowest user activity per hour.

4.Using the Comments.xml file, wrote Map-Reduce Jobs to create summary tables (plot wherever possible) for the total Number of Comments and Median of Comment Length by Month from May 2014 to Sep 2021.

5. Using the Users.xml file and PostsHistory.xml, calculated the correlation coefficient of the reputation of the user in Users.xml to the total answers given by the user in PostsHistory.xml file. 