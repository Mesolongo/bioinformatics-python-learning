#####################################
print("Exercise 1")
#####################################

def count_nucleotides(dna_sequence):
    # Your code here
    dna_sequence = dna_sequence.upper()
    counts = {}
    dna_bases = 'ATCG'

    for nucleotide in dna_sequence:
        if nucleotide in dna_bases:
                counts[nucleotide] = counts.get(nucleotide, 0) +1
    return counts

# Test cases:
print(count_nucleotides("ATCGATCGAA"))  
# Expected: {'A': 4, 'T': 2, 'C': 2, 'G': 2}

print(count_nucleotides("AAAA"))  
# Expected: {'A': 4}

print(count_nucleotides("ATCG"))  
# Expected: {'A': 1, 'T': 1, 'C': 1, 'G': 1}

print(count_nucleotides("ATcgNNatcg"))  
# Expected: {'A': 2, 'T': 2, 'C': 2, 'G': 2}

#####################################
print("Exercise 2")
#####################################


def count_codons(dna_sequence):
    # Your code here
    counts = {}
    for i in range(0, len(dna_sequence) - len(dna_sequence)%3, 3):
        codons = dna_sequence[i:i+3]
        counts[codons] = counts.get(codons, 0) + 1
    return counts

# Test cases:
print(count_codons("ATGATCTGA"))
# Expected: {'ATG': 1, 'ATC': 1, 'TGA': 1}

print(count_codons("ATGATGATG"))
# Expected: {'ATG': 3}

print(count_codons("ATGATCTGACC"))
# Expected: {'ATG': 1, 'ATC': 1, 'TGA': 1}
# Note: 'CC' at the end is incomplete, so it's ignored

#####################################
print("exercise 3")
#####################################


def aggregate_expression(measurements):
    # First, build dictionary of lists
    counts = {}
    for gene_name, expression_level in measurements: 
        counts[gene_name] = counts.get(gene_name, []) + [expression_level]
    
    # Then, transform to include averages
    result = {}
    for gene_name, expression_list in counts.items():
        average = sum(expression_list) / len(expression_list)
        result[gene_name] = {
            'values': expression_list,
            'average': round(average, 1)
        }
    
    return result

# Test case:
data = [("BRCA1", 5.2), ("TP53", 3.1), ("BRCA1", 4.8), ("TP53", 3.5), ("BRCA1", 5.0)]
print(aggregate_expression(data))
# Expected: 
# {'BRCA1': {'values': [5.2, 4.8, 5.0], 'average': 5.0}, 
#  'TP53': {'values': [3.1, 3.5], 'average': 3.3}}