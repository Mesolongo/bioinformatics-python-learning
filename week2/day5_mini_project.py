def load_valid_genes(filename):
    with open(filename, 'r') as file:
        return {line.strip() for line in file}

def load_all_samples(sample_files, valid_genes):
    all_samples = {}
    for filename in sample_files:
        # Extract sample name: sample1_expression.csv -> sample1
        sample_name = filename.split('_')[0] 
        
        with open(filename, 'r') as file:
            next(file)  # skip header
            result = {}
            for line in file:
                line = line.strip()
                if line:  # skip empty lines
                    gene, expression = line.split(',')
                    if gene in valid_genes:
                        result[gene] = float(expression)  # convert to float
            all_samples[sample_name] = result
    return all_samples

def find_common_genes(samples_data):
    # Convert each sample's gene dictionary into a set of gene names
    gene_sets = [set(genes.keys()) for genes in samples_data.values()]

    # Find genes present in ALL samples
    common_genes = set.intersection(*gene_sets)

    return common_genes

def calculate_average_expression(samples_data):
    # Your code here
    result = {}
    gene_counts = {}
    gene_sums = {}

    # Count occurrences and sum values
    for genes in samples_data.values():
        for gene, expression in genes.items():
            gene_counts[gene] = gene_counts.get(gene, 0) + 1
            gene_sums[gene] = gene_sums.get(gene, 0) + expression

    # Compute averages only for genes appearing in ≥ 2 samples
    for gene in gene_counts:
        if gene_counts[gene] >= 2:
            avg = round(gene_sums[gene]/ gene_counts[gene], 2)
            result[gene] = avg
            
    return result

def find_high_expression_genes(average_expression, threshold=7.0):
    result = {}

    #Filter genes above threshold
    for gene, expression in average_expression.items():
        if expression >= threshold:
            result[gene]= expression

    #Sort descending by expression
    result = dict(sorted(result.items(), key=lambda x:x[1], reverse=True))

    return result

def generate_report(samples_data, valid_genes):
    # 1. Total number of samples
    total_samples = len(samples_data)

    # 2. Total valid genes (simply size of valid_genes set)
    total_valid_genes = len(valid_genes)

    # 3. Common genes across all samples
    common_genes = find_common_genes(samples_data)

    # 4. Average expression (only for genes appearing ≥2 samples)
    average_expression = calculate_average_expression(samples_data)

    # 5. High expression genes (avg ≥ 7.0)
    high_expression_genes = find_high_expression_genes(average_expression, threshold=7.0)

    # 6. Gene count per sample
    genes_per_sample = {sample: len(genes) for sample, genes in samples_data.items()}

    # 7. Return everything in a dictionary
    return {
        "total_samples": total_samples,
        "total_valid_genes": total_valid_genes,
        "common_genes": common_genes,
        "average_expression": average_expression,
        "high_expression_genes": high_expression_genes,
        "genes_per_sample": genes_per_sample
    }

# Test it with main
def main():
    valid_genes = load_valid_genes("valid_genes.txt")
    
    sample_files = [
        "sample1_expression.csv",
        "sample2_expression.csv", 
        "sample3_expression.csv"
    ]
    samples_data = load_all_samples(sample_files, valid_genes)
    
    report = generate_report(samples_data, valid_genes)
    
    print("=== Gene Expression Analysis Report ===\n")
    print(f"Total samples analyzed: {report['total_samples']}")
    print(f"Total valid genes: {report['total_valid_genes']}")
    print(f"\nGenes per sample: {report['genes_per_sample']}")
    print(f"\nCommon genes across all samples: {report['common_genes']}")
    print(f"\nHigh expression genes (avg >= 7.0):")
    for gene, expr in report['high_expression_genes'].items():
        print(f"  {gene}: {expr}")

if __name__ == "__main__":
    main()

