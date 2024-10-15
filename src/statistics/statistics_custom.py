import math
import re

pos_z_code_list = [['.50000', '.50399', '.50798', '.51197', '.51595', '.51994', '.52392', '.52790', '.53188', '.53586'], ['.53983', '.54380', '.54776', '.55172', '.55567', '.55962', '.56356', '.56749', '.57142', '.57535'], ['.57926', '.58317', '.58706', '.59095', '.59483', '.59871', '.60257', '.60642', '.61026', '.61409'], ['.61791', '.62172', '.62552', '.62930', '.63307', '.63683', '.64058', '.64431', '.64803', '.65173'], ['.65542', '.65910', '.66276', '.66640', '.67003', '.67364', '.67724', '.68082', '.68439', '.68793'], ['.69146', '.69497', '.69847', '.70194', '.70540', '.70884', '.71226', '.71566', '.71904', '.72240'], ['.72575', '.72907', '.73237', '.73565', '.73891', '.74215', '.74537', '.74857', '.75175', '.75490'], ['.75804', '.76115', '.76424', '.76730', '.77035', '.77337', '.77637', '.77935', '.78230', '.78524'], ['.78814', '.79103', '.79389', '.79673', '.79955', '.80234', '.80511', '.80785', '.81057', '.81327'], ['.81594', '.81859', '.82121', '.82381', '.82639', '.82894', '.83147', '.83398', '.83646', '.83891'], ['.84134', '.84375', '.84614', '.84849', '.85083', '.85314', '.85543', '.85769', '.85993', '.86214'], ['.86433', '.86650', '.86864', '.87076', '.87286', '.87493', '.87698', '.87900', '.88100', '.88298'], ['.88493', '.88686', '.88877', '.89065', '.89251', '.89435', '.89617', '.89796', '.89973', '.90147'], ['.90320', '.90490', '.90658', '.90824', '.90988', '.91149', '.91309', '.91466', '.91621', '.91774'], ['.91924', '.92073', '.92220', '.92364', '.92507', '.92647', '.92785', '.92922', '.93056', '.93189'], ['.93319', '.93448', '.93574', '.93699', '.93822', '.93943', '.94062', '.94179', '.94295', '.94408'], ['.94520', '.94630', '.94738', '.94845', '.94950', '.95053', '.95154', '.95254', '.95352', '.95449'], ['.95543', '.95637', '.95728', '.95818', '.95907', '.95994', '.96080', '.96164', '.96246', '.96327'], ['.96407', '.96485', '.96562', '.96638', '.96712', '.96784', '.96856', '.96926', '.96995', '.97062'], ['.97128', '.97193', '.97257', '.97320', '.97381', '.97441', '.97500', '.97558', '.97615', '.97670'], ['.97725', '.97778', '.97831', '.97882', '.97932', '.97982', '.98030', '.98077', '.98124', '.98169'], ['.98214', '.98257', '.98300', '.98341', '.98382', '.98422', '.98461', '.98500', '.98537', '.98574'], ['.98610', '.98645', '.98679', '.98713', '.98745', '.98778', '.98809', '.98870', '.98899', '.98928'], ['.98956', '.98983', '.99010', '.99036', '.99061', '.99086', '.99111', '.99134', '.99158', '.99180'], ['.99202', '.99224', '.99245', '.99266', '.99286', '.99305', '.99324', '.99343', '.99361', '.99379'], ['.99396', '.99413', '.99430', '.99446', '.99461', '.99477', '.99492', '.99506', '.99520', '.99534'], ['.99547', '.99560', '.99573', '.99585', '.99598', '.99609', '.99621', '.99632', '.99643', '.99653'], ['.99664', '.99674', '.99683', '.99693', '.99702', '.99711', '.99720', '.99728', '.99736', '.99744'], ['.99752', '.99760', '.99767', '.99774', '.99781', '.99788', '.99795', '.99801', '.99807', '.99813'], ['.99819', '.99825', '.99831', '.99836', '.99841', '.99846', '.99851', '.99856', '.99861', '.99865'], ['.99869', '.99874', '.99878', '.99882', '.99886', '.99889', '.99893', '.99896', '.99900', '.99903'], ['.99906', '.99910', '.99913', '.99916', '.99918', '.99921', '.99924', '.99926', '.99929', '.99931'], ['.99934', '.99936', '.99938', '.99940', '.99942', '.99944', '.99946', '.99948', '.99950', '.99952'], ['.99953', '.99955', '.99957', '.99958', '.99960', '.99961', '.99962', '.99964', '.99965', '.99966'], ['.99968', '.99969', '.99970', '.99971', '.99972', '.99973', '.99974', '.99975', '.99976', '.99977'], ['.99978', '.99978', '.99979', '.99980', '.99981', '.99981', '.99982', '.99983', '.99983', '.99984'], ['.99985', '.99985', '.99986', '.99986', '.99987', '.99987', '.99988', '.99988', '.99989', '.99989'], ['.99990', '.99990', '.99990', '.99991', '.99991', '.99992', '.99992', '.99992', '.99992', '.99993'], ['.99993', '.99993', '.99994', '.99994', '.99994', '.99994', '.99995', '.99995', '.99995', '.99995'], ['.99995', '.99996', '.99996', '.99996', '.99996', '.99996', '.99996', '.99997', '.99997']]

t_table_confidence = ['0.1000', '0.0500', '0.0250', '0.0100', '0.0050', '0.0010', '0.0005']

t_table_list = [[3.078, 6.314, 12.076, 31.821, 63.657, 318.310, 636.620],
[1.886, 2.920, 4.303, 6.965, 9.925, 22.326, 31.598],
[1.638, 2.353, 3.182, 4.541, 5.841, 10.213, 12.924],
[1.533, 2.132, 2.776, 3.747, 4.604, 7.173, 8.610],
[1.476, 2.015, 2.571, 3.365, 4.032, 5.893, 6.869],
[1.440, 1.943, 2.447, 3.143, 3.707, 5.208, 5.959],
[1.415, 1.895, 2.365, 2.998, 3.499, 4.785, 5.408],
[1.397, 1.860, 2.306, 2.896, 3.355, 4.501, 5.041],
[1.383, 1.833, 2.262, 2.821, 3.250, 4.297, 4.781],
[1.372, 1.812, 2.228, 2.764, 3.169, 4.144, 4.587],
[1.363, 1.796, 2.201, 2.718, 3.106, 4.025, 4.437],
[1.356, 1.782, 2.179, 2.681, 3.055, 3.930, 4.318],
[1.350, 1.771, 2.160, 2.650, 3.012, 3.852, 4.221],
[1.345, 1.761, 2.145, 2.624, 2.977, 3.787, 4.140],
[1.341, 1.753, 2.131, 2.602, 2.947, 3.733, 4.073],
[1.337, 1.746, 2.120, 2.583, 2.921, 3.686, 4.015],
[1.333, 1.740, 2.110, 2.567, 2.898, 3.646, 3.965],
[1.330, 1.734, 2.101, 2.552, 2.878, 3.610, 3.922],
[1.328, 1.729, 2.093, 2.539, 2.861, 3.579, 3.883],
[1.325, 1.725, 2.086, 2.528, 2.845, 3.552, 3.850],
[1.323, 1.721, 2.080, 2.518, 2.831, 3.527, 3.819],
[1.321, 1.717, 2.074, 2.508, 2.819, 3.505, 3.792],
[1.319, 1.714, 2.069, 2.500, 2.807, 3.485, 3.767],
[1.318, 1.711, 2.064, 2.492, 2.797, 3.467, 3.745],
[1.316, 1.708, 2.060, 2.485, 2.787, 3.450, 3.725],
[1.315, 1.706, 2.056, 2.479, 2.779, 3.425, 3.707],
[1.314, 1.703, 2.052, 2.473, 2.771, 3.421, 3.690],
[1.313, 1.701, 2.048, 2.467, 2.763, 3.408, 3.674],
[1.311, 1.699, 2.045, 2.462, 2.756, 3.396, 3.659],
[1.310, 1.697, 2.042, 2.457, 2.750, 3.385, 3.646],
[1.303, 1.684, 2.021, 2.423, 2.704, 3.307, 3.551],
[1.296, 1.671, 2.000, 2.390, 2.660, 3.232, 3.460],
[1.289, 1.658, 1.980, 2.358, 2.617, 3.160, 3.373],
[1.282, 1.645, 1.960, 2.326, 2.576, 3.090, 3.291]]


def mean(*args):
    val_sum = sum(args)
    return val_sum / len(args)


def median(*args):
    if len(args) % 2 == 0:
        i = round((len(args) + 1) / 2)
        j = i - 1
        return (args[i] + args[j]) / 2
    else:
        k = round(len(args) / 2)
        return args[k]


def mode(*args):
    # Count how many times values show up in
    # the list and put it in a dictionary
    dict_vals = {i: args.count(i) for i in args}
    # Create a list of keys that have the maximum
    # number of occurrence in the list
    max_list = [k for k, v in dict_vals.items() if v == max(dict_vals.values())]
    return max_list


def variance(*args):
    mean_val = mean(*args)
    numerator = 0
    for i in args:
        numerator += (i - mean_val) ** 2
    denominator = len(args) - 1
    try:
        answer = numerator / denominator
    except ZeroDivisionError:
        answer = numerator / 1
    return answer


def standard_deviation(*args):
    return math.sqrt(variance(*args))


def coefficient_variation(*args):
    return standard_deviation(*args) / mean(*args)


def covariance(*args):
    # Use a list comprehension to get all values
    # stored in the 1st & 2nd list
    list_1 = [i[0] for i in args]
    list_2 = [i[1] for i in args]
    # Pass those lists to get their means
    list_1_mean = mean(*list_1[0])
    list_2_mean = mean(*list_2[0])
    numerator = 0

    # We must have the same number of elements
    # in both lists
    if len(list_1[0]) == len(list_2[0]):
        for i in range(len(list_1[0])):
            # FInd xi - x mean * yi - y mean
            numerator += (list_1[0][i] - list_1_mean) * (list_2[0][i] - list_2_mean)
        denominator = len(list_1[0]) - 1
        return numerator / denominator
    else:
        print("Error : You must have the same number of values in both lists")


def correlation_coefficient(*args):
    list_1 = [i[0] for i in args]
    list_2 = [i[1] for i in args]
    # Pass those lists to get their standard deviations
    list_1_sd = standard_deviation(*list_1[0])
    list_2_sd = standard_deviation(*list_2[0])
    denominator = list_1_sd * list_2_sd
    # Get the covariance
    numerator = covariance(*args)
    print(f"Covariance {numerator}")
    print(f"list_1_sd {list_1_sd}")
    print(f"list_2_sd {list_2_sd}")
    return numerator / denominator


def normalize_list(*args):
    sd_list = standard_deviation(*args)
    return [(i - mean(*args))/sd_list for i in args]


def sample_error(*args):
    sd_list = standard_deviation(*args)
    return sd_list / (math.sqrt(len(args)))


def get_z_code(z_code_area):
    # Get index for first closest matching value in Z Table
    # Define what I'm looking for
    # Trim the 0 from the area because it isn't used in the
    # list of table values
    z_code_area = ("%.3f" % z_code_area).lstrip('0')
    # Create the Regex with . 3 provided values and any
    # last 2 digits
    regex = "\\" + z_code_area + "\d{2}"
    # Iterate the multidimensional list
    for i in range(0, len(pos_z_code_list) - 1):
        for j in range(0, len(pos_z_code_list[0])):
            # If I find a match
            if re.search(regex, pos_z_code_list[i][j]):
                # Combine column and row values into Z Code
                z_code = float(i * .1 + j * .01)
                return z_code


# Formula (x,y) = x̄ ± Z(α/2) * σ/√n
# x̄ : Sample Mean
# α : Alpha (1 - Confidence)
# σ : Standard Deviation
# n : Sample Size
def get_confidence_interval(sample_mean, confidence, sd, sample_size):
    alpha_val = (1 - confidence)
    critical_probability = 1 - alpha_val / 2
    z_code = get_z_code(critical_probability)
    print("Alpha {:.3f}".format(alpha_val))
    print("Critical Probability {:.3f}".format(critical_probability))
    print("Z Code {:.3f}".format(z_code))
    print("Margin of Error {:.3f}".format((z_code * (sd / math.sqrt(sample_size)))))
    x = sample_mean - (z_code * (sd / math.sqrt(sample_size)))
    y = sample_mean + (z_code * (sd / math.sqrt(sample_size)))
    print(f"Confidence Interval")
    print("Low : {:.2f}".format(x))
    print("High : {:.2f}".format(y))


def get_t_confidence_interval(confidence, *args):
    # Get alpha for T Table with 4 decimals
    half_alpha = (1 - confidence) / 2
    half_alpha = ("%.4f" % half_alpha)

    # Get the T Value, sample mean and standard
    # deviation based on the data
    if half_alpha in t_table_confidence:
        alpha_index = t_table_confidence.index(half_alpha)
        # Subtract 2 instead of 1 because list is 0 based
        degree_freedom = len(args) - 2
        if 1 <= degree_freedom <= 30:
            t_value = t_table_list[degree_freedom][alpha_index]
        elif 31 <= degree_freedom <= 60:
            t_value = t_table_list[31][alpha_index]
        elif 61 <= degree_freedom <= 120:
            t_value = t_table_list[32][alpha_index]
        else:
            t_value = t_table_list[33][alpha_index]
        sample_mean = mean(*args)
        sd = standard_deviation(*args)
        print("T Distribution")
        print("Sample Mean : {:.4f}".format(sample_mean))
        print("Standard Deviation : {:.4f}".format(sd))
        print("T Value : {:.3f}".format(t_value))

        # Return high and low distribution
        low_val = sample_mean - (t_value * (sd / math.sqrt(degree_freedom)))
        high_val = sample_mean + (t_value * (sd / math.sqrt(degree_freedom)))
        print("Low : {:.2f}".format(low_val))
        print("High : {:.2f}".format(high_val))


# Receives list of x & y samples and returns a
# regression list
def get_linear_regression_list(*args):
    # Sum of all x and y values
    x_sum = 0
    y_sum = 0
    for i in range(len(args)):
        for j in range(len(args[i])):
            x_sum += args[i][j][0]
            y_sum += args[i][j][1]

    # Get x & y bar (Means)
    x_bar = x_sum / len(args[0])
    y_bar = y_sum / len(args[0])

    numerator = 0
    denominator = 0
    for i in range(len(args)):
        for j in range(len(args[i])):
            x_sums = args[i][j][0] - x_bar
            denominator += math.pow(x_sums, 2)
            numerator += x_sums * (args[i][j][1] - y_bar)

    slope = numerator/denominator

    y_intercept = y_bar - slope * x_bar

    # Create multidimensional list of x y values
    # for the regression line with x being equal
    # to all values of x in the passed list
    lr_list = [[0] * 2 for k in range(len(args[0]))]
    for l in range(len(args)):
        for m in range(len(args[l])):
            # Get x value
            lr_list[m][0] = args[l][m][0]
            # Calculate y value
            lr_list[m][1] = int(y_intercept + (slope * args[l][m][0]))

    # Return the linear regression list
    return lr_list


chi_square_list = [[.45, 1.64, 2.70, 3.84, 5.02, 5.41, 6.63, 7.87, 9.55, 10.82], [1.38, 3.21, 4.60, 5.99, 7.37, 7.82, 9.21, 10.59, 12.42, 13.81], [2.36, 4.64, 6.25, 7.81, 9.34, 9.83, 11.34, 12.83, 14.79, 16.266]]

chi_per_list = [.5, .2, .1, .05, .025, .02, .01, .005, .002, .001]


def root_mean_squared_deviation(*args):
    y_sample_list = [i[0] for i in args]
    y_regression_list = [i[1] for i in args]

    sample_length = len(args[0][0])
    numerator = 0
    denominator = sample_length - 1
    for j in range(sample_length):
        difference = args[0][0][j] - args[0][1][j]
        numerator += math.pow(difference, 2)
    return math.sqrt(numerator/denominator)


def chi_square_test(*args):
    list_1 = [i[0] for i in args]
    list_2 = [i[1] for i in args]
    num_cols = len(args[0][0])
    num_rows = len(args[0])
    degree_freedom = (num_cols - 1) * (num_rows - 1)
    col_sum_list = [sum(x) for x in zip(*args[0])]
    row_sum_list = [sum(x) for x in args[0]]
    row_sum = sum(row_sum_list)
    expected_table = []
    temp_list =[]
    for i in range(len(row_sum_list)):
        for j in range(len(col_sum_list)):
            temp_list.append(round(row_sum_list[i] * col_sum_list[j] / row_sum))
        expected_table.append(temp_list)
        temp_list = []
    chi_num = 0
    for m in range(len(list_1[0])):
        chi_num += math.pow(expected_table[0][m] - list_1[0][m], 2) / expected_table[0][m]
    for n in range(len(list_2[0])):
        chi_num += math.pow(expected_table[0][n] - list_2[0][n], 2) / expected_table[0][n]

    for p in range(9):
        if chi_num <= chi_square_list[degree_freedom-1][p]:
            print(f"Confidence : {1 - chi_per_list[p]}")
            break