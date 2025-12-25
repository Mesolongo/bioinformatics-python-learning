#####################################
print("Exercise 1")
#####################################

def count_codons(dna):
    """
    Count occurrences of each codon in a DNA sequence.
    
    Parameters:
        dna (str): DNA sequence to analyze
        
    Returns:
        dict: Dictionary with codons as keys and their counts as values
        
    Example:
        >>> count_codons("ATGATGCCCATG")
        {'ATG': 3, 'CCC': 1}
    """
    result = {}
    for i in range(0, len(dna)- len(dna)%3, 3):
        codon = dna[i:i+3]
        result[codon] = result.get(codon, 0) +1
    return result
print(count_codons("ATGATGCCCATG"))
# Should output: {'ATG': 3, 'CCC': 1}

#####################################
print("Exercise 2")
#####################################

def filter_by_quality(sequence, quality_scores, min_quality=20):
    """
    Filter DNA sequence based on quality scores.
    
    Parameters:
        sequence (str): DNA sequence to filter
        quality_scores (list): List of quality scores (one per base)
        min_quality (int): Minimum quality threshold (default: 20)
        
    Returns:
        str: Filtered sequence containing only high-quality bases
        
    Example:
        >>> filter_by_quality("ATGC", [30, 25, 15, 35], min_quality=25)
        'ATG'
    """
    result = ''.join(base for base, score in zip(sequence, quality_scores) 
                 if score >= min_quality)
    return result

seq = "ATGCGATCG"
scores = [30, 25, 15, 35, 10, 40, 28, 22, 18]
print(filter_by_quality(seq, scores))  # Should output: "ATCATC"
print(filter_by_quality(seq, scores, min_quality=25))  # Should output: "ATCAT"

#####################################
print("Exercise 3")
#####################################

def protein_analysis(protein_sequence):
    """
    Analyze amino acid sequence and return statistics.
    
    Parameters:
        protein_sequence (str): Amino acid sequence to analyze
        
    Returns:
        dict: Dictionary containing:
            - 'length': Number of amino acids
            - 'molecular_weight': Approximate weight in Daltons (110 Da per AA)
            - 'charged_count': Count of charged amino acids (D, E, K, R, H)
            - 'hydrophobic_count': Count of hydrophobic amino acids (A, V, L, I, M, F, W, P)
        
    Example:
        >>> protein_analysis("ACDEFGH")
        {'length': 7, 'molecular_weight': 770, 'charged_count': 3, 'hydrophobic_count': 2}
    """

    charged = 'DEKRH'
    hydrophobic = 'AVLIMFWP'
    length_of_aa = len(protein_sequence)
    molecular_weight = length_of_aa * 110

    charged_count = sum(protein_sequence.count(aa) for aa in charged)
    hydrophobic_count = sum(protein_sequence.count(aa) for aa in hydrophobic)

    result = {
        'length': length_of_aa,
        'molecular_weight' : molecular_weight,
        'charged_count' : charged_count,
        'hydrophobic_count' : hydrophobic_count
    }

    return result

result = protein_analysis("ACDEFGHIKLMNPQRSTVWY")
print(result)
# Should show length=20, molecular_weight=2200, etc.

