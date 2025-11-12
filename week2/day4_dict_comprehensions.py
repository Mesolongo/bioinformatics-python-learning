import pprint
#####################################
print("Exercise 1")
#####################################

def normalize_expression(expression_dict):
    # Your code here
    total = sum(expression_dict.values())
    normalized = {gene: round((value/total)*100, 2) for gene, value in expression_dict.items()}
    return normalized

# Test it
expression = {'BRCA1': 100, 'TP53': 50, 'EGFR': 75, 'KRAS': 25}
result = normalize_expression(expression)
pprint.pprint(result)
# Expected (rounded to 2 decimals):
# {'BRCA1': 40.0, 'TP53': 20.0, 'EGFR': 30.0, 'KRAS': 10.0}

#####################################
print("Exercise 2")
#####################################

def classify_expression(expression_dict):
    # Your code here
    classified = {
        gene: 'high' if count >= 7 else 'moderate' 
        for gene, count in expression_dict.items()
        if count > 3.0
        }
    return classified

# Test it
expression = {
    'BRCA1': 8.5,
    'TP53': 2.1,
    'EGFR': 6.3,
    'KRAS': 1.5,
    'MYC': 9.2,
    'APC': 4.7
}

result = classify_expression(expression)
pprint.pprint(result)
# Expected:
# {'BRCA1': 'high', 'EGFR': 'moderate', 'MYC': 'high', 'APC': 'moderate'}
# Note: TP53 and KRAS are excluded (expression <= 3.0)

#####################################
print("Exercise 3")
#####################################

def create_expression_matrix(genes, samples, values):
    # Your code here
    n = len(samples)
    data = {
        gene: {
            sample: value for sample, value in zip(samples,values[i*n : (i+1)*n])
            } 
            for i, gene in enumerate(genes)
        }
    return data

# Test it
genes = ['BRCA1', 'TP53', 'EGFR']
samples = ['Sample1', 'Sample2']
values = [5.2, 6.1, 3.1, 2.8, 4.0, 4.5]
# Order: BRCA1-Sample1, BRCA1-Sample2, TP53-Sample1, TP53-Sample2, EGFR-Sample1, EGFR-Sample2

result = create_expression_matrix(genes, samples, values)
pprint.pprint(result)
# Expected:
# {
#   'BRCA1': {'Sample1': 5.2, 'Sample2': 6.1},
#   'TP53': {'Sample1': 3.1, 'Sample2': 2.8},
#   'EGFR': {'Sample1': 4.0, 'Sample2': 4.5}
# }