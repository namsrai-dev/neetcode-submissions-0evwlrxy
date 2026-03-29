class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        print("adding word", word)
        cur = self.root
        for c in word:
            index = ord(c) - ord('a')
            if cur.children[index] is None:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.isLeaf = True
        

    def search(self, word: str) -> bool:

        cur_arr = [self.root]
        print("searching word", word)
        for c in word:
            index = ord(c) - ord('a')
            if c != '.':
                
                print("len(cur_arr)", len(cur_arr))
                new_arr = []
                for cur in cur_arr:
                    print("cur.children", cur.children)
                    print("index", index)
                    if cur.children[index] is not None:
                        print("char found", c)
                        new_arr.append(cur.children[index])
                    # cur_arr.pop(0)
                cur_arr = new_arr
            else:
                print(". orson", len(cur_arr))
                new_arr = []
                for cur in cur_arr:
                    print("forever",cur)
                    for i, child in enumerate(cur.children):
                        if child:
                            print("i index set", i)
                            new_arr.append(child)

                    cur_arr.pop(0)
                cur_arr = new_arr

                print(len(cur_arr))

        print(cur_arr)

        for cur in cur_arr:
            if cur.isLeaf:
                return True
        return False