from tree_sitter import Language, Parser

Language.build_library("build/java.so", ["tree-sitter-java"])

JAVA_LANGUAGE = Language("build/java.so", "java")

parser = Parser()
parser.set_language(JAVA_LANGUAGE)

src = b"""
class A {
  public int b() {
    int c = 5;
  }
}
"""

tree = parser.parse(src)

root_node = tree.root_node

print(root_node)
print(root_node.type)
print(root_node.start_point)
print(root_node.end_point)

child_node = root_node.children[0]

print(child_node)
print(child_node.type)
print(child_node.start_point)
print(child_node.end_point)

