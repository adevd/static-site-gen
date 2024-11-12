from textnode import TextNode, TextType

def main():
    test_node = TextNode("this is text", TextType.BOLD, "https://www.boot.dev")
    print(test_node.__repr__())

main()
