"""
Exercise 4

Practicing List Comprehension (with if and if else statements)
Each of these definitions is already complete, solve each of the following definitions using list comprehension.
Solutions do not need to be 1 line long.

List Comprehension is sometimes called List Display:
    https://docs.python.org/3.6/reference/expressions.html#list-displays
"""


def rc(dna):
    """
    This is the third iteration of our reverse compliment function. Use a dictionary AND list comprehension to
    convert a DNA string into its reverse compliment.
    EX: rc("CCCTTTCCCAAA") should return "TTTGGGAAAGGG"
    :param dna: A string containing only C, T, A, and G
    :return: A string containing only C, T, A, and G
    """
    comp_dict = {"A": "T", "G": "C", "T": "A", "C": "G"}
    rc_dna = [comp_dict[char] for char in dna]
    return ''.join(rc_dna[::-1])


print(rc("CCCTTTCCCAAA"))


def percent_decimal(numbers):
    """
    Takes in a list of numbers and converts a percentage to a decimal or a decimal to a percentage
    depending on the input i
    EX: percent_decimal([0.0, 0.5, 1.0, 50.0, 100.0]) should return [0.0, 50.0, 100.0, 0.5, 1.0]
    :param i: a list of floats between 0 and 100
    :return: a list of floats between 0 and 100
    """

    new_numbers = [num / 100 if num > 1 else num * 100 for num in numbers]
    return new_numbers


print(percent_decimal([0.0, 0.5, 1.0, 50.0, 100.0]))


def multiple_proteins_from_rna(rna):

    C2AA = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
            "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
            "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
            "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
            "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
            "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
            "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
            "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
            "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
            "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
            "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
            "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
            "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
            "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
            "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
            "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

    # Turn the input string (rna) into its amino acid composition
    protein = [C2AA[rna[i:i + 3]] for i in range(0, len(rna), 3)]

    # Now we extract every [M -> end] slice of our protein
    protein_list = [''.join(protein[index:]) for index, char in enumerate(protein) if char == "M"]
    return protein_list


# print(multiple_proteins_from_rna("UCCAUGUUUAUGAGGAGGUGA"))


def percent_decimal1(numbers):
    """
    Takes in a list of numbers and converts a percentage to a decimal or a decimal to a percentage
    depending on the input i
    EX: percent_decimal([0.0, 0.5, 1.0, 50.0, 100.0]) should return [0.0, 50.0, 100.0, 0.5, 1.0]
    :param i: a list of floats between 0 and 100
    :return: a list of floats between 0 and 100
    """

    new_numbers = []
    for num in numbers:
        if num > 1:
            new_numbers.append(num / 100)
        else:
            new_numbers.append(num * 100)

    return new_numbers

print(percent_decimal1([0.0, 0.5, 1.0, 50.0, 100.0]))