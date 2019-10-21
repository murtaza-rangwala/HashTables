class BSTTreeNode:
  '''
  This class represents a node in the binary search tree
  '''
  def __init__(self, key = None, data =None, left = None, right = None):
    '''
    This function initializes the node elements
    @complexity:    O(1)
    @input:         key: key from the key, value pair
                    data: value from the key, value pair
                    left: Link to left child
                    right: Link to right child
    @return:        None
    '''
    self.key = key
    self.data = data
    self.left = left
    self.right = right


class BinarySearchTree:
  '''
  This class represents the binary search tree
  '''
  def __init__(self):
    '''
    This function initialises the binary search tree
    @complexity:    O(1)
    @input:         None
    @returns:       None
    '''
    self.root = None
    self.count = 0
  
  def is_empty(self):
    '''
    This function checks if the BST is empty
    @complexity:    O(1)
    @input:         None
    @returns:       True if BST is empty, else False
    '''
    return self.root is None

  def __contains__(self, key):
    return self.contains_aux(self.root, key)

  def contains_aux(self, current, key):
    if current is None:
      return False
    elif current.key < key:
      return self.contains_aux(current.right ,key)
    elif current.key > key:
      return self.contains_aux(current.left ,key)
    elif current.key == key:
      return True

  def __setitem__(self, key, data):
    '''
    This function called setitem_aux to set a node in the BST
    @input:     key: key for the key, value pair
                data: value for the key, value pair
    @returns:   None
    '''
    self.count = 0
    self.root = self.setitem_aux(self.root, key, data)
  
  def setitem_aux(self, current, key, data):
    '''
    This function sets a new node item or changes a current node item in the BST
    @complexity:    Worst Case Complexity: O(BST length) / Best Case Complexity: O(1)
    @input:         current: Current Binary Tree node
                    key: key for the key, value pair
                    data: value for the key, value pair
    @returns:       New BST node
    '''
    if current is None:
      current = BSTTreeNode(key, data)
    elif current.key < key:
      self.count += 1
      current.right = self.setitem_aux(current.right ,key, data)
    elif current.key > key:
      self.count += 1
      current.left = self.setitem_aux(current.left ,key, data)
    else:
      current.data = data
    return current
  
  def __getitem__(self, key):
    '''
    This function called getitem_aux to get a node in the BST
    @input:     key: key for the key, value pair
                data: value for the key, value pair
    @returns:   None
    '''
    return self.getitem_aux(self.root, key)
  
  def getitem_aux(self, current, key):
    '''
    This function gets a node in the BST
    @complexity:    Worst Case Complexity: O(BST length) / Best Case Complexity: O(1)
    @input:         current: Current Binary Tree node
                    key: key for the key, value pair
    @returns:       Target BST node
    '''
    if current is None:
      raise KeyError("key not found")
    elif current.key < key:
      return self.getitem_aux(current.right ,key)
    elif current.key > key:
      return self.getitem_aux(current.left ,key)
    else:
      return current.data
  
  def print_preorder(self):
    '''
    This function calls print_preorder_aux to print the BST
    @input:     None
    @returns:   None
    '''
    self.print_preorder_aux(self.root)
  
  def print_preorder_aux(self, current):
    '''
    This function prints the BST
    @input:     current: current node
    @returns:   None
    '''
    if current is not None:
      print(current.key)
      self.print_preorder_aux(current.left)
      self.print_preorder_aux(current.right)