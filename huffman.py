# Represents a Huffman tree for use in encoding/decoding strings.
# A sample usage is as follows:
#
# h = HuffmanTree([('A', 2), ('B', 7), ('C', 1)])
# assert(h.encode('ABC') == '01100')
# assert(h.decode(h.encode('ABC')) == 'ABC')


class HuffmanTree:
    # Helper object for building the Huffman tree.
    # You may modify this constructor but the grading script rlies on the left, right, and symbol fields.
    class TreeNode:
        def __init__(self, left=None, right=None, symbol=None, min_element=None):
            self.left = left
            self.right = right
            self.symbol = symbol
            self.min_element = min_element

    # The `symbol_list` argument should be a list of tuples `(symbol, weight)`,
    # where `symbol` is a symbol that can be encoded, and `weight` is the
    # the unnormalized probabilitiy of that symbol appearing.
    def __init__(self, symbol_list):
        assert(len(symbol_list) >= 2)
        sl = []
        for s in symbol_list:
            sl.append((self.TreeNode(symbol=s[0], min_element=s[0]), s[1]))

        self.root = None  # (place TreeNode object here)
        self._coding_dict = {}
        self._char_dict = {}
        while len(sl) > 1:
            sl.sort(key=lambda x: x[0].min_element)
            sl.sort(key=lambda x: x[1])
            n1 = sl[0]
            n2 = sl[1]

            self.root = self.TreeNode(n1[0], n2[0], min_element=n1[0].min_element if
                                      n1[0].min_element < n2[0].min_element else n2[0].min_element)
            sl = sl[2:]
            sl.append((self.root, n1[1] + n2[1]))
        self._create_coding_dict(self.root, '')

    def _create_coding_dict(self, node, cur_code):
        if node.symbol != None:
            self._coding_dict[node.symbol] = cur_code
            self._char_dict[cur_code] = node.symbol
            return

        self._create_coding_dict(node.left, cur_code + '0')
        self._create_coding_dict(node.right, cur_code + '1')

    # Encodes a string of characters into a string of bits using the
    # symbol/weight list provided.

    def encode(self, s):
        assert(s is not None)

        ret = ''
        for c in s:
            ret += self._coding_dict[c]
        return ret

    # Decodes a string of bits into a string of characters using the
    # symbol/weight list provided.
    def decode(self, s):
        assert(s is not None)

        ret = ''
        cur_code = ''
        for c in s:
            cur_code += c
            if cur_code in self._char_dict:
                ret += self._char_dict[cur_code]
                cur_code = ''

        if cur_code != '': return None
        return ret
