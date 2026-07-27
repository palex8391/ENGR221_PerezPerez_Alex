""" 
Author: Alex Perez Perez
Last updated: July 26, 2026
Description: Defines a TreeNode class used to build and search the Engineering faculty tree. """

from enum import Enum


class TreeNode:
    # Initialize a new tree node with a name, type, optional data, and empty child list.
    def __init__(self, name, node_type, data=None):
        self.name = name  # Store the node's display name.
        self.node_type = node_type  # Store the node's category/type.
        self.data = data  # Optional extra information for the node.
        self.parent = None  # Reference to the parent node.
        self.children = []  # List of child nodes.


    def add_child(self, child) -> None:
        """Add a child node to this node and link the parent reference."""
        child.parent = self  # Set the child's parent to this node.
        self.children.append(child)  # Add the child to this node's list.


    def remove_child(self, child) -> None:
        """Remove a child if it exists and clear its parent reference."""
        if child in self.children:
            self.children.remove(child)  # Remove the child from this node.
            child.parent = None  # Detach the child from the tree.


    def is_leaf(self) -> bool:
        """Return True when this node has no children; otherwise return False."""
        return len(self.children) == 0  # A leaf has no child nodes.


    def depth(self) -> int:
        """Return the number of edges from the root to this node."""
        depth_count = 0  # Count how many parent links must be followed.
        current = self.parent  # Start from the parent of this node.

        # Walk upward through the parent chain until the root is reached.
        while current is not None:
            depth_count += 1  # Add one level for each parent encountered.
            current = current.parent  # Move to the next ancestor.

        return depth_count

    def height(self) -> int:
        """Return the height of this node in the tree."""
        if self.is_leaf():
            return 0  # A leaf has height 0.

        return 1 + max(child.height() for child in self.children)  # Add one level above the tallest child.


    def find(self, name):
        """Return the first node with the given name, or None if not found."""
        if self.name == name:
            return self  # This node matches the requested name.

        for child in self.children:
            result = child.find(name)  # Search each child recursively.
            if result is not None:
                return result  # Return the first match found.

        return None  # No matching node was found.


    def print_tree(self, indent=0):
        """Print the tree with indentation to show its structure."""
        print("    " * indent + str(self))  # Print the current node with indentation.

        for child in self.children:
            child.print_tree(indent + 1)  # Recursively print each child at a deeper level.


    def __str__(self):
        return self.name  # Return the node's name when it is converted to a string.


    class NodeType(Enum):
        # Define the possible types of nodes in the tree.
        SCHOOL = "School"
        PROGAM = "Program"
        FACULTY = "Faculty"

        @classmethod
        def init_from_str(cls, node_type):
            # Convert a string into the matching enum value.
            return cls[node_type.strip().upper()]

if __name__ == "__main__":
    # Create a sample tree to demonstrate the class behavior.
    root = TreeNode("Engineering", TreeNode.NodeType.SCHOOL)

    comp_e = TreeNode("CompE", TreeNode.NodeType.PROGAM)
    root.add_child(comp_e)

    ee = TreeNode("EE", TreeNode.NodeType.PROGAM)
    root.add_child(ee)

    kubota = TreeNode("Kubota", TreeNode.NodeType.FACULTY)
    comp_e.add_child(kubota)

    qin = TreeNode("Qin", TreeNode.NodeType.FACULTY)
    comp_e.add_child(qin)

    root.print_tree()