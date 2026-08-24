def pipeline_function(input_dictionary):
    a = input_dictionary['a']
    b = input_dictionary['b']
    c = a + b
    output_dictionary = {'c': c}
    return output_dictionary
