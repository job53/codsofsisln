def duplicate_or_unique(inList):
    # Count the frequency of each element
    counts = {}
    for x in inList:
        counts[x] = counts.get(x, 0) + 1

    # n will be the number of unique numbers
    n = len(counts)
    
    # Determine which problem type it is:
    # Type 1 (duplicate case) has n+1 elements
    # Type 2 (unique case) has 2*n - 1 elements
    if len(inList) == n + 1:
        # Type 1: Find the number with frequency 2 (the duplicate)
        for key, value in counts.items():
            if value == 2:
                return key
    elif len(inList) == 2 * n - 1:
        # Type 2: Find the number with frequency 1 (the unique)
        for key, value in counts.items():
            if value == 1:
                return key

    # Fallback if none of these patterns match.
    return None


# Below are the sample tests provided

if __name__ == "__main__":
    # Test lists and expected outputs:
    print(duplicate_or_unique([1,2,3,6,5,4,1]))                      # Expected 1 (Type 1)
    print(duplicate_or_unique([1,2,3,1,2,3,4]))                      # Expected 4 (Type 2)
    print(duplicate_or_unique([1,2,3,6,5,4,6]))                      # Expected 6 (Type 1)
    print(duplicate_or_unique([3,6,9,2,5,8,1,4,8,7]))                # Expected 8 (Type 1)
    print(duplicate_or_unique([9,8,7,1,2,3,9,7,1,2,3,4,4,5,5,6,6]))    # Expected 8 (Type 2)