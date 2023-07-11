# Problem 7: Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

exam_st_date = (11, 12, 2014)
tup2str = str(exam_st_date)
print(tup2str.replace(",", " /"))
# output should be 11 / 12 / 2014 but in this case its (11 / 12 / 2014), I'm working on it.
