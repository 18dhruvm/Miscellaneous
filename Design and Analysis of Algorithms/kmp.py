# -*- coding: utf-8 -*-
"""KMP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ShaQY9j_bE3848jCo94kkApFiHHVkCEO
"""

import time

"""Brute Force Algorithm
takes O(nm) where n is length of text and m is length of pattern
"""

def bruteForce(pat, txt):
    M = len(pat)
    N = len(txt)
 
    # A loop to slide pat[] one by one */
    for i in range(N):
        j = 0
         
        # For current index i, check
        # for pattern match */
        while(j < M):
            if (txt[i + j] != pat[j]):
                break
            j += 1
 
        if (j == M):
            print("Pattern found at index ", i)

"""KMP Algorithm takes O(n + m)"""

# Python program for KMP Algorithm
def KMPSearch(pat, txt):
	M = len(pat)
	N = len(txt)

	# create lps[] that will hold the longest prefix suffix values for pattern
	lps = [0]*M
	j = 0

	# Preprocess the pattern (calculate lps[] array)
	LPSArray(pat, M, lps)

	i = 0 # index for txt[]
	while i < N:
		if pat[j] == txt[i]:
			i = i+1
			j = j+1

		if j == M:
			print ("Found pattern at index " + str(i-j))
			j = lps[j-1]

		# mismatch after j matches
		elif i < N and pat[j] != txt[i]:
			# Do not match lps[0..lps[j-1]] characters,they will match anyway
			if j != 0:
				j = lps[j-1]
			else:
				i = i+1

def LPSArray(pat, M, lps):
	len = 0 # length of the previous longest prefix suffix

	lps[0] # lps[0] is always 0
	i = 1

	# the loop calculates lps[i] for i = 1 to M-1
	while i < M:
		if pat[i]== pat[len]:
			len+=1
			lps[i] = len
			i+=1
		else:
			if len != 0:
				len = lps[len-1]

			else:
				lps[i] = 0
				i+=1

"""Optimized KMP algorithm which makes lesser comparisons compared to KMP algorithm"""

class Globals():
    
    # Function to construct the failure function corresponding to the pattern
  
    def constructFailureFunction(P, F):

        # P is the pattern,
        # F is the FailureFunction
        # assume F has length m,
        # where m is the size of P

        len5 = len(P)

        # F[0] must have the value 0
        F[0] = 0

        # The index, we are parsing P[1..j]
        j = 1
        l = 0

        # Loop to iterate through the pattern
        while j < len5:

            # Computing the lsp
            if P[j] == P[l]:
                l += 1
                F[j] = l
                j += 1
            elif l > 0:
                l = F[l - 1]
            else:
                F[j] = 0
                j += 1

    # Function to construct the failure table.
    
    def constructFailureTable(P, pattern_alphabet, F, FT):
        len7 = len(P)

        # T is the char where we mismatched
        for t in pattern_alphabet:

            # Allocate an array
            FT[t] = [0 for _ in range(len7)]
            l = 0
            while l < len7:
                if P[F[l]] == t:

                    # Old failure function gives
                    # a good shifting
                    FT[t][l] = F[l] + 1
                else:

                    # Move to the next char if
                    # the entry in the failure
                    # function is 0
                    if F[l] == 0:
                        FT[t][l] = 0

                    # Fill the table if F[l] > 0
                    else:
                        FT[t][l] = FT[t][F[l] - 1]
                l += 1

    def KMP(T, P, pattern_alphabet):

        # Size of the pattern
        m = len(P)

        # Size of the text
        n = len(T)

        # Initialize the Failure Function
        F = [0 for i in range(m)]

        # Constructing the failure function using KMP algorithm
        Globals.constructFailureFunction(P, F)

        FT = {}

        # Construct the failure table and store it in FT[][]
        Globals.constructFailureTable(P, pattern_alphabet, F, FT)

        # The starting index will be when the first match occurs
        found_index = -1

        # Variable to iterate over the indices in Text T
        i = 0

        # Variable to iterate over the indices in Pattern P
        j = 0

        # Loop to iterate over the text
        while i < n:
            if P[j] == T[i]:

                # Matched the last character in P
                if j == m - 1:
                    found_index = i - m + 1
                    break
                else:
                    i += 1
                    j += 1
            else:
                if j > 0:

                    # T[i] is not in P's alphabet
                    if T[i] not in FT.keys():

                        # Begin a new matching process
                        j = 0

                    else:
                        j = FT[T[i]][j - 1] # Update 'j' to be the length of,the longest suffix of P[1..j] which is also a prefix of P
                    i += 1
                else:
                    i += 1

        # If pattern found, print index
        if found_index != -1:
            print("Found at index ", end = '')
            print(found_index, end = '')
            print('\n', end = '')
        else:
            print("Not Found \n", end = '')

        for t in pattern_alphabet:

            # Deallocate the arrays in FT
            FT[t] = None

        return

"""Test Cases"""

T ="huw8bifwbb9b9brpqpqpqrpqpqprpuh9fsu9qbf9qbf9qu9qg9g9gc56ef"
pattern_alphabet = set(T)
patterns = ["pqpqprp", "pqpqr", "rpqqq"]


for i in patterns:
  
  print("Naive Algorithm:")
  t = time.time()
  bruteForce(i,T)
  elapsed = time.time() - t
  print(elapsed*1000)

  print("KMP algo:")
  t = time.time()
  KMPSearch(i,T)
  elapsed = time.time() - t
  print(elapsed*1000)
  
  
  print("Optimized KMP algo:")
  t = time.time()
  Globals.KMP(T, i, pattern_alphabet)
  elapsed = time.time() - t
  print(elapsed*1000)
  print("\n")