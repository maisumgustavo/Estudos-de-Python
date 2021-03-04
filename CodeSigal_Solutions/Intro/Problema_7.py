def almostIncreasingSequence(sequence):
    return sequence[:] < sequence[::1]

print(almostIncreasingSequence(input()))
