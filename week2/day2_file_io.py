#####################################
print("Exercise 1")
#####################################

def parse_fasta(filename):
    # Your code here
    with open(filename, 'r') as file:
        sequences = {}
        current_gene = None

        for line in file:
            line = line.strip()

            if line.startswith('>'):
                current_gene = line[1:]
                sequences[current_gene] = ''
            else:
                sequences[current_gene] = sequences[current_gene] + line
    return sequences
# Test it
result = parse_fasta("sequences.fasta")
print(result)
# Expected: {'BRCA1': 'ATCGATCGATCGATCG', 'TP53': 'GCTAGCTAGCTA', 'EGFR': 'TTTTAAAA'}

#####################################
print("Exercise 2")
#####################################

def analyze_gene_lengths(filename):
    with open(filename, 'r') as file:
        sequences = {}
        current_gene = None

        # --- Read and store sequences ---
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_gene = line[1:]       # remove '>'
                sequences[current_gene] = ''  # initialize entry
            else:
                sequences[current_gene] += line  # append sequence

    # --- Calculate lengths ---
    lengths = {gene: len(seq) for gene, seq in sequences.items()}

    # --- Find the longest gene ---
    longest_gene = max(lengths, key=lengths.get)

    # --- Build and return final structured dictionary ---
    result = {
        'lengths': lengths,
        'longest_gene': longest_gene
    }

    return result
    
# Test it
result = analyze_gene_lengths("sequences.fasta")
print(result)
# Expected: 
# {
#   'lengths': {'BRCA1': 16, 'TP53': 12, 'EGFR': 8},
#   'longest_gene': 'BRCA1'
# }

#####################################
print("Exercise 3")
#####################################

def parse_expression_csv(filename):
    # Your code here
    result = {}
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            line = line.strip()
            parts = line.split(',')

            gene = parts[0]
            condition = parts[1]
            expression = float(parts[2])

            if gene not in result:
                result[gene] = {}

            result[gene][condition] = expression
    return result
# Test it
result = parse_expression_csv("expression_data.csv")
print(result)
# Expected:
# {
#   'BRCA1': {'normal': 5.2, 'tumor': 8.1},
#   'TP53': {'normal': 3.5, 'tumor': 1.2},
#   'EGFR': {'normal': 4.0, 'tumor': 9.5}
# }