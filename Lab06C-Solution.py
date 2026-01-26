# Lab06C

import unittest

def split_line_to_words_and_spaces(line, width):

    words = line.split()

    totalOfWordLengths = 0
    for word in words:
        totalOfWordLengths += len(word)

    spaceCount = width - totalOfWordLengths

    return (words, spaceCount)


def distribute_spaces_at_end(words, spaces):
    # This will blow up with a zerodivide in the special case of having only one word on the line
    # As a special case we will left justify that word, and pad the line with spaces
    if len(words) > 1:
        gaps = len(words) - 1
        spaces_per_gap = spaces // gaps
        leftoverOddSpaces = spaces % gaps
        words.reverse()

        wordsWithSpaces = []
        for word in words:
            if leftoverOddSpaces > 0:
                spacesThisGap = spaces_per_gap + 1
                leftoverOddSpaces -= 1
            else:
                spacesThisGap = spaces_per_gap

            wordsWithSpaces.append(' ' * spacesThisGap + word)

        # Previous loop adds an EXTRA unwanted space in front of the FIRST word
        # Correct that.  The words are reversed so it's the LAST one in the list
        # Take a slice of that string from position 1 to the (defaulted) end
        wordsWithSpaces[-1] = wordsWithSpaces[-1][1:]

        
        wordsWithSpaces.reverse()

        return ''.join(wordsWithSpaces)
    else:
        return words[0] + " " * spaces    
    

class TestAddFunction(unittest.TestCase):
    def test_lineDecomposition(self):

        words, spaces = split_line_to_words_and_spaces("the..   boy", 12)

        self.assertEqual(words, ["the..",  "boy"])
        self.assertEqual(spaces, 4)

    def test_distributeExcessSpacesAtEndOfLine(self):
        line = distribute_spaces_at_end(["the..", "boy", "stood", "on"], 4)
        self.assertEqual(line, "the.. boy stood  on")

    def test_lineWithOnlyOneWord(self):
        line = distribute_spaces_at_end(["the.."], 2)
        self.assertEqual(line, "the..  ")


if __name__ == '__main__':
    unittest.main()