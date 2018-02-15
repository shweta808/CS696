"""
Homework 01
DO NOT RENAME THIS FILE OR ANY DEFINITIONS!
Place this file in your github repo inside of a folder titled "Homework".
"""


# String Functions
def fast_complement(dna):
    """
    Uses a dictionary to convert a DNA sequence into the complement strand.  C <--> G,  T <--> A
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    dna_dictionary = {'C': 'G', 'G': 'C', 'T': 'A', 'A': 'T'}
    f_compliment = ''.join([dna_dictionary[x] for x in dna])

    return f_compliment


def remove_interval(s, start, stop):
    """
    Removes the interval of characters from a string or list inclusively, 0 based
    EX: remove_intervals('ABCDEFGHI', 2, 5) will return 'ABGHI'.
    :param s: a string
    :param start: a non-negative integer
    :param stop: a non-negative integer greater than the start integer.
    :return: a string
    """
    remove_interval = s[:start] + s[stop+1:]

    return remove_interval


def kmer_list(s, k):
    """
    Generates all kmers of size k for a string s and store them in a list
    :param s: any string
    :param k: any integer greater than zero
    :return: a list of strings
    """
    kmers_list = []
    kmer_len = len(s)

    for i in range(0, kmer_len - k + 1):
        kmers_list.append(s[i:i + k])

    return kmers_list


def kmer_set(s, k):
    """
    Generates all kmers of size k for a string s and store them in a set
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    kmers_set = set()
    kmer_len = len(s)

    for i in range(0, kmer_len - k + 1):
        kmers_set.add(s[i:i + k])

    return kmers_set


def kmer_dict(s, k):
    """
    Generates all kmers of size k for a string s and store them in a dictionary with the
    kmer(string) as the key and the number of occurances of the kmer as the value(int).
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    kmer_count = {}

    for i in range(len(s) - k + 1):
        kmer_str = s[i:i + k]
        kmer_count[kmer_str] = kmer_count.get(kmer_str, 0) + 1

    return kmer_count


# Reading Files
def head(file_name):
    """
    Prints the FIRST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    with open(file_name) as f:
        f = f.read().splitlines()
        lines = [line for line in f]

        for i in range(0, 10):
            print(lines[i])

    return


def tail(file_name):
    """
    Prints the LAST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    with open(file_name) as f:
        f = f.read().splitlines()
        lines = [line for line in f]

        for i in range(len(lines) - 10, len(lines)):
            print(lines[i])

    return


def print_even(file_name):
    """
    Prints the even numbered lines of a file
    :param file_name: a string
    :return: None
    """
    with open(file_name) as f:
        f = f.read().splitlines()
        lines = [line for line in f]

        for i in range(0, len(lines)):
            if i % 2 == 0:
                print(lines[i])

    return


def csv_list(file_name):
    """
    Read in a CSV file to a 2D array (In python it is a list of lists)
    :param file_name: a string
    :return: a list of lists
    """
    with open(file_name) as f:
        f = f.read()
        lines = f.split('\n')
        csv_two_d = []

        for line in lines:
            sublist = []
            words = line.split(',')
            for j in words:
                sublist.append(j)
            csv_two_d.append(sublist)

        print(csv_two_d)

    return


def get_csv_column(file_name, column):
    """
    Reads in a CSV file and returns a list of values belonging to the column specified
    :param file_name: a string
    :param column: a positive integer
    :return: a list
    """
    with open(file_name) as f:
        f = f.read()
        lines = f.split('\n')
        list = []

        for line in lines:
            words = line.split(',')
            list.append(words[column])

        print(list)

    return


def fasta_seqs(file_name):
    """
    Reads in a FASTA file and returns a list of only the sequences
    :param file_name: a string
    :return: a list of strings
    """

    with open(file_name, 'r') as f:
        content = f.read()
        file_content = content.split('>')
        file_content = file_content[1:]
        sequence_list = []

        for f_content in file_content:
            try:
                split_fasta = f_content.split('\n', 1)
                sequence_list.append(split_fasta[1].replace('\n', '').replace('\r', ''))
            except:
                print('bad sequence')

    return sequence_list


def fasta_headers(file_name):
    """
    Reads in a FASTA file and returns a list of only the headers (Lines that start with ">")
    :param file_name: a string
    :return: a list of strings
    """
    with open(file_name, 'r') as f:
        content = f.read()
        file_content = content.split('>')
        file_content = file_content[1:]
        header_list = []

        for f_content in file_content:
            try:
                split_fasta = f_content.split('\n', 1)
                header_list.append(split_fasta[0].replace('\n', '').replace('\r', ''))
            except:
                print('bad headers')

    return header_list


def fasta_dict(file_name):
    """
    Reads in a FASTA file and returns a dictionary of the format {header: sequence, ...}, where
    the sequence headers are keys and the sequence is the value
    :param file_name: a string
    :return: a dictionary
    """

    fasta_heads = fasta_headers(file_name)
    fasta_seq = fasta_seqs(file_name)
    fasta_dictionary = dict(zip(fasta_heads, fasta_seq))

    return fasta_dictionary


def fastq_to_fasta(file_name, new_name=None):
    """
    Reads in a FASTQ file and writes it to a new FASTA file. This definition should also
    keep the same file name and change the extension to from .fastq to .fasta if new_name is not specified.
    EX: fastq_to_fasta('ecoli.fastq') should write to a new file called ecoli.fasta
    :param file_name: a string
    :param new_name: a string
    :return: None
    """

    if file_name.endswith('.fastq'):
        if new_name is not None:
            fasta_fname = new_name
        else:
            fasta_fname = file_name.replace('.fastq', '.fasta')

        try:
            with open(file_name, 'r') as f:
                content = f.read()
                file_content = content.split('@')[1:]
                fasta_file = open(fasta_fname, 'w')

                for f_content in file_content:
                    try:
                        if len(f_content) == 0:
                            continue
                        split_fastq = f_content.split('\n')
                        headers = split_fastq[0]
                        sequence_list = split_fastq[1]
                        fasta_file.write('>' + headers + '\n' + sequence_list + '\n')
                    except:
                        print('file content error')
                fasta_file.close()
        except:
            print('not able to parse file')

    else:
        print('File must be .fastq')
    return


# Transcription and Translation
def reverse_complement(dna):
    """
    Returns the strand of DNA that is the reverse complement of the sequence given
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    dna_dictionary = {'C': 'G', 'G': 'C', 'T': 'A', 'A': 'T'}
    r_compliment = "".join([dna_dictionary[key] for key in reversed(dna)])

    return r_compliment


def transcribe(dna):
    """
    Transcribes a string of DNA into RNA
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, U, A, and G
    """
    dna = dna.replace('T', 'U')

    return dna


def translate(rna):
    """
    Translates the strand of RNA given into its amino acid composition.
    DO NOT INCLUDE * IN YOUR RETURN STRING
    :param rna: a string containing only the characters C, U, A, and G
    :return: a string containing only the characters G, A, L, M, F, W, K, Q, E, S, P, V, I, C, Y, H, R, N, D, and T
    """
    RNA_CODON_TABLE = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
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

    result = ''

    try:
        for i in range(0, len(rna), 3):
            value = RNA_CODON_TABLE[rna[i:i + 3]]
            if value == '*':
                break
            result = result + value

    except KeyError:
        print('key not found')

    return result


def reading_frames(dna):
    """
    Generates a list of all 6 possible reading frames for a given strand of DNA
    For the non-biologists: https://en.wikipedia.org/wiki/Open_reading_frame
    :param dna: a string containing only the characters C, T, A, and G
    :return: a list of 6 strings containing only C, T, A, and G
    """
    result_frame = []
    result_frame.append(dna)
    result_frame.append(dna[1:-2])
    result_frame.append(dna[2:-1])

    reverse_comp = reverse_complement(dna)
    result_frame.append(reverse_comp)
    result_frame.append(reverse_comp[1:-2])
    result_frame.append(reverse_comp[2:-1])

    return result_frame

