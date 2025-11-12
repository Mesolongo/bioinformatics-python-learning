#####################################
print("Exercise 1")
#####################################

import pprint
def compare_gene_sets(sample1_file, sample2_file):
    # Your code here
    with open(sample1_file, 'r') as file1, open(sample2_file, 'r') as file2:
        set1 = set()
        set2 = set()

        for line in file1:
            set1.add(line.strip())

        for line in file2:
            set2.add(line.strip())

    result = {
        'common': set1 & set2,
        'unique_to_sample1': set1 - set2,
        'unique_to_sample2': set2 - set1,
        'all_genes': set1 | set2
    }

    return result
    
# Test it
result = compare_gene_sets("sample1_genes.txt", "sample2_genes.txt")
pprint.pprint(result)
# Expected:
# {
#   'common': {'BRCA1', 'TP53'},
#   'unique_to_sample1': {'EGFR', 'KRAS'},
#   'unique_to_sample2': {'MYC', 'APC'},
#   'all_genes': {'BRCA1', 'TP53', 'EGFR', 'KRAS', 'MYC', 'APC'}
# }

#####################################
print("Exercise 2")
#####################################

def map_genes_to_samples(filename):
    # Your code here
    with open(filename, 'r') as file:
        result = {}
        for line in file:
            line = line.strip()
            parts = line.split(',')

            gene_name = parts[1]
            sample_name = parts[0]

            result.setdefault(gene_name,set()).add(sample_name)

    return result
# Test it
result = map_genes_to_samples("gene_samples.txt")
pprint.pprint(result)
# Expected:
# {
#   'BRCA1': {'Sample1', 'Sample2', 'Sample3'},
#   'TP53': {'Sample1', 'Sample2'},
#   'EGFR': {'Sample2', 'Sample3'},
#   'KRAS': {'Sample1'}
# }

#####################################
print("Exercise 3")
#####################################

def merge_sample_data(sample_dicts):
    # Your code here
    merged_data = {}
    for sample_name, gene_data in sample_dicts.items():
        for gene, expression in gene_data.items():
            merged_data.setdefault(gene, {})[sample_name] = expression
    return (merged_data)

# Test it
sample1 = {'BRCA1': 5.2, 'TP53': 3.1, 'EGFR': 4.0}
sample2 = {'BRCA1': 6.1, 'TP53': 2.8, 'KRAS': 3.5}
sample3 = {'BRCA1': 5.8, 'EGFR': 4.5, 'MYC': 7.2}

samples = {
    'Sample1': sample1,
    'Sample2': sample2,
    'Sample3': sample3
}

result = merge_sample_data(samples)
pprint.pprint(result)
# Expected:
# {
#   'BRCA1': {'Sample1': 5.2, 'Sample2': 6.1, 'Sample3': 5.8},
#   'TP53': {'Sample1': 3.1, 'Sample2': 2.8},
#   'EGFR': {'Sample1': 4.0, 'Sample3': 4.5},
#   'KRAS': {'Sample2': 3.5},
#   'MYC': {'Sample3': 7.2}
# }