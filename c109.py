import plotly.figure_factory as ff
import statistics
import pandas as pd

df = pd.read_csv("data.csv")
height_list = df["height"].to_list()
weight_list = df["weight"].to_list()
sd = statistics.stdev(height_list)
sd2 = statistics.stdev(weight_list)
mean1 = statistics.mean(height_list)
mean2 = statistics.mean(weight_list)

median1 = statistics.median(height_list)
median2 = statistics.median(weight_list)

mode1 = statistics.mode(height_list)
mode2 = statistics.mode(weight_list)

print(sd,sd2)
print(mean1,mean2)
print(median1,median2)
print(mode1,mode2)

height_first_std_start,height_first_std_end = mean1 - sd, mean1 + sd
height_second_std_start,height_second_std_end = mean1 -(2*sd), mean1 + (2*sd)
height_third_std_start,height_third_std_end = mean1 -(3*sd), mean1 + (3*sd)

weight_first_std_start,weight_first_std_end = mean2 - sd2, mean2 + sd2
weight_second_std_start,weight_second_std_end = mean2 -(2*sd2), mean2 + (2*sd2)
weight_third_std_start,weight_third_std_end = mean2 -(3*sd2), mean2 + (3*sd2)

height_list_of_data_within_one_std = [result for result in height_list if result>height_first_std_start and result<height_first_std_end]
height_list_of_data_within_two_std = [result for result in height_list if result>height_second_std_start and result<height_second_std_end]
height_list_of_data_within_three_std = [result for result in height_list if result>height_third_std_start and result<height_third_std_end]

weight_list_of_data_within_one_std = [result for result in weight_list if result>weight_first_std_start and result<weight_first_std_end]
weight_list_of_data_within_two_std = [result for result in weight_list if result>weight_second_std_start and result<weight_second_std_end]
weight_list_of_data_within_three_std = [result for result in weight_list if result>weight_third_std_start and result<weight_third_std_end]

print("{}% of data for height lie within one std".format(len(height_list_of_data_within_one_std)*100.0/len(height_list)))
print("{}% of data for height lie within two std".format(len(height_list_of_data_within_two_std)*100.0/len(height_list)))
print("{}% of data for height lie within three std".format(len(height_list_of_data_within_three_std)*100.0/len(height_list)))