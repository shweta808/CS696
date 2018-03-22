"""
Homework 02
DO NOT RENAME THIS FILE OR ANY CLASSES/DEFINITIONS!
Place this file in your github repo inside of a folder titled "Homework".

Python allows more than 1 class per file, and the general consensus of opinion is that one file (module) should be
limited to only the items that will be used together. For example, if two modules are almost always imported together
then they should be condensed to one file (and thus one import statement). The opposite is also true, classes and
definitions that are unrelated in functionality should be split to separate modules (files).
"""


class String_Aligner:
    """
    This is a class that will contain several different methods for comparing and aligning two strings. Because DNA,
    RNA and Proteins are represented in strings, these 'simple' string comparisons will have a big role in answering
    biological questions.

    The class is instantiated with two strings (s1 and s2) that will be compared with following algorithms:
        Analysis                             Read
        * Hamming Distance                   * https://en.wikipedia.org/wiki/Hamming_distance
        * Needleman-Wunsch(matrix only)      * https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm
        * Smith-Waterman(matrix only)        * https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm

    """

    def __init__(self, string1, string2):
        """
        Sets the two strings as self attributes
        :param string1: any non empty string
        :param string2: any non empty string
        """
        self.s1 = string1
        self.s2 = string2
        return

    def hamming_dist(self):
        """
        Returns the hamming distance between s1 and s2. The Hamming distance is calculated as the number of pair-wise
        mismatches between two strings - if they are of unequal length, count the extra spaces as mismatches.

        For Example:
            s1 = 'AABBCCDD'
            s2 = 'AAXXXCDD'
        would return 3, because there are three positions at which the two do not match. Another Example:
            s1 = 'AABBCCDD'
            s2 = 'XAABBCCDD'
        would return 9, because there are 9 mismatches when each index is compared.

        :return: a non negative integer
        """
        diff = abs(len(self.s1) - len(self.s2))
        hamming_dist_sum = sum(char1 != char1 for char1, char2 in zip(self.s1, self.s2))
        return hamming_dist_sum + diff

    def empty_matrix(self):
        """
        returns a list of lists (2d array) the outer list should hold len(s1)+1 elements,
        and each inner list should hold len(s2)+1 indexes. For example:
        s1 = 'ABC'
        s2 = 'ABCD'
        should produce [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
        to better visualize it:

                 A  B  C  D
            [[0, 0, 0, 0, 0],
        A    [0, 0, 0, 0, 0],
        B    [0, 0, 0, 0, 0],
        C    [0, 0, 0, 0, 0]]

        :return: a list of lists
        """
        return [[0 for i in range(len(self.s2)+1)] for j in range(len(self.s1)+1)]

    def init_needleman_wunsch_matrix(self):
        """
        This definition returns a 2d array of values initialized for the smith waterman algorithm.
        For example:
        s1 = 'ABC'
        s2 = 'ABCD'
        should produce [[0, -1, -2, -3, -4],[-1, 0, 0, 0, 0],[-2, 0, 0, 0, 0],[-3, 0, 0, 0, 0]]
        to better visualize it:

                   A   B   C   D
            [[ 0, -1, -2, -3, -4],
        A    [-1,  0,  0,  0,  0],
        B    [-2,  0,  0,  0,  0],
        C    [-3,  0,  0,  0,  0]]

        :return: a list of lists
        """
        empty_matrix = self.empty_matrix()  # Building on the previous definition, this will give you an empty matrix

        column_value = 0
        for c_index in range(len(self.s1)+1):
            empty_matrix[c_index][0] = column_value
            column_value -= 1

        row_value = 0
        for r_index in range(len(self.s2)+1):
            empty_matrix[0][r_index] = row_value
            row_value -= 1

        return empty_matrix


    def needleman_wunsch_fill(self):
        """
        This function builds upon the initialized NW matrix and scores the remaining cells based on a scoring function
        defined below.
        Match +1
        Mismatch -1
        Insertion/Deletion -1

        For example:
        s1 = 'ABC'
        s2 = 'ABCD'
        should produce [[0, -1, -2, -3, -4], [-1, 1, 0, -1, -2], [-2, 0, 2, 1, -1], [-3, -1, 1, 3, 2]]
        To better visualize it:

                   A   B   C   D
            [[ 0, -1, -2, -3, -4],
        A    [-1,  1,  0, -1, -2],
        B    [-2,  0,  2,  1, -1],
        C    [-3, -1,  1,  3,  2]]

        :return: a list of lists
        """

        matrix = self.init_needleman_wunsch_matrix() # Building on the previous definition

        def score_cell(i,j):
            """
            This is our first example of a nested definition. This scoreing definition will return the score of
            a position (i, j) based on the left, upper, and upper left values. Your scoring function should:
                * Choose the maximum of the following 3 values for the score
                    * the value of (i-1, j) + insertion/deletion penalty
                    * the value of (i, j-1) + insertion/deletion penalty
                    * If the characters at i-1 and j-1 in s1 and s2 respectively match:
                        the value of (i-1, j-1) + match score
                      else
                        the value of (i-1, j-1) + mismatch penalty
            :param i: integer, the outer list index (s1)
            :param j: integer, the inner list index (s2)
            :return: integer
            """
            match = 1
            mismatch = -1
            insertion_deletion = -1

            if self.s1[i - 1] == self.s2[j - 1]:
                upper_left = matrix[i - 1][j - 1] + match
            else:
                upper_left = matrix[i - 1][j - 1] + mismatch

            upper_value = matrix[i - 1][j] + insertion_deletion
            left_value = matrix[i][j - 1] + insertion_deletion

            max_score = max(upper_value, left_value, upper_left)

            return max_score

        for row_index in range(1, len(self.s1) + 1):
            for col_index in range(1, len(self.s2) + 1):
                matrix[row_index][col_index] = score_cell(row_index, col_index)

        return matrix

    def smith_waterman_fill(self):
        """
        Fills in a matrix using the Smith-Waterman Algorithm. This algorithm builds upon an empty matrix
        from self.empty_matrix()
        Match +3
        Mismatch -3
        Insertion/Deletion -2

        For example:
        s1 = 'ABC'
        s2 = 'ABCD'
        Should return: [[0, 0, 0, 0, 0], [0, 3, 1, 0, 0], [0, 1, 6, 4, 2], [0, 0, 4, 9, 7]]
        to better visualize it:

                 A  B  C  D
            [[0, 0, 0, 0, 0],
        A    [0, 3, 1, 0, 0],
        B    [0, 1, 6, 4, 2],
        C    [0, 0, 4, 9, 7]]
        :return: a list of lists
        """

        matrix = self.empty_matrix() # Building on the previous definition

        def score_cell(i, j):
            """
            This scoreing definition will return the score of
            a position (i, j) based on the left, upper, and upper left values.
            Your scoring function should:
                * Choose the maximum of the following 4 values for the score
                    * the value of (i-1, j) + insertion/deletion penalty
                    * the value of (i, j-1) + insertion/deletion penalty
                    * If the characters at i-1 and j-1 in s1 and s2 respectively match:
                        the value of (i-1, j-1) + match score
                      else
                        the value of (i-1, j-1) + mismatch penalty
                    * 0   (if all other numbers are negative, use 0)
            :param i: integer, the outer list index
            :param j: integer, the inner list index
            :return: integer
            """
            match = 3
            mismatch = -3
            insertion_deletion = -2

            if self.s1[i - 1] == self.s2[j - 1]:
                upper_left = matrix[i - 1][j - 1] + match
            else:
                upper_left = matrix[i - 1][j - 1] + mismatch

            upper_value = matrix[i - 1][j] + insertion_deletion
            left_value = matrix[i][j - 1] + insertion_deletion

            max_score = max(upper_value, left_value, upper_left, 0)

            return max_score

        for row_index in range(1, len(self.s1) + 1):
            for col_index in range(1, len(self.s2) + 1):
                matrix[row_index][col_index] = score_cell(row_index, col_index)

        return matrix


"""
These are general string functions outside of the String Alignment Class (notice they start without any indentation)
They are imported with the Class (import homework_2), but can run without it.

**IMPORTANT** For the first 3 definiitions, your program should avoid
performing lookups in lists (if char in my_list) and use a set() instead. 
For time complexity, see: https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
"""

def is_dna(string):
    """
    Checks a string using list comprehension for any unallowed characters (DNA can only contain C, T, A, and G) and
    returns True if it only contains those 4 characters, and False otherwise
    For Example:
    is_dna("CCCAAATTTGGG") should return True
    is_dna("CCCAAATTTGGGXXX") should return False
    :return: Boolean
    """
    allowed_dna_list = ['C', 'T', 'A', 'G']
    check_dna = False if False in [char in allowed_dna_list for char in string] else True
    return check_dna

def is_rna(string):
    """
    Checks a string using list comprehension for any unallowed characters (DNA can only contain C, U, A, and G) and
    returns True if it only contains those 4 characters, and False otherwise
    For Example:
    is_dna("CCCAAAUUUGGG") should return True
    is_dna("CCCAAAUUUGGGXXX") should return False
    :return: Boolean
    """
    allowed_rna_list = ['C', 'U', 'A', 'G']
    check_rna = False if False in [char in allowed_rna_list for char in string] else True
    return check_rna


def is_protein(string):
    """
    Checks a string using list comprehension for any unallowed characters:
    ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'K', 'L', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
    returns True if it only contains those characters, and False otherwise
    For Example:
    is_dna("ARQGHI") should return True
    is_dna("XPLNNO") should return False
    :return: Boolean
    """
    allowed_protein_list = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'K', 'L', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
    check_protein = False if False in [char in allowed_protein_list for char in string] else True
    return check_protein


"""
Regex and UrlLib definitions
"""
import re
import urllib.request as ur

def get_sra_xml(sra_run_id):
    """
    The Sequence Read Archive (SRA) is the worlds largest database of raw sequencing data.
    This definition takes in the run_id of one dataset and downloads the xml metadata from the URL below.
    For Example:
    The return from get_sra_xml('SRR3403834') should start with:
    '<RunViewer run="srr3403834"> ...'
    :param sra_run_id: string
    :return: **A string**  not b'my_string' <- the b is for byte, this is a byte string
    """
    url = "http://www.ncbi.nlm.nih.gov/Traces/sra/?run={}&experimental=1&retmode=xml".format(sra_run_id)
    return ur.urlopen(url).read().decode()

def get_filesize(string):
    """
    Using the string returned from get_sra_xml(), finds the file size of the sra run (it is in bytes),
    convert it to gigabytes and returns it as a float.
    For Example:
    get_filesize('SRR3403834')  should return
    1.411331958
    :param string: the xml metadata document in string format from get_sra_xml()
    :return: a float
    """

    file_size = re.search("size=\"(.*?)\"", get_sra_xml(string))
    file_size_gb = float(file_size.group(1)) / 1000000000
    return file_size_gb

def get_protein_fasta(uniprot_id):
    """
    Uniprot is a database of protein sequence data. Given the uniprot_id of a protein,
    and using urllib, return only the sequence (not the header) from the fasta entry.
    Be sure to remove new line characters from the protein sequence.
    EX:
    get_protein_fasta('P69892')   should return
    'MGHFTEEDKATITSLWGKVNVEDAGGETLGRLLVVYPWTQRFFDSFGNLSSASAIMGNPKVKAHGKKVLTSLGDAIKHLDDLKGTFAQLSELHCDKLHVDPENFKLLGNVLVTVLAIHFGKEFTPEVQASWQKMVTGVASALSSRYH'
    :param uniprot_id: string
    :return: string
    """
    url = "http://www.uniprot.org/uniprot/{}.fasta".format(uniprot_id)
    response = ur.urlopen(url).read().decode()
    fasta_seq = re.split("\n", response)[1:]
    return ''.join(fasta_seq)


