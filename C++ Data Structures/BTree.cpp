//Anthony Chen and Shyam Venekataraman

#include <iostream>
#include "BTree.h"
#include "BTreeNode.h"
#include "LeafNode.h"
#include "InternalNode.h"
using namespace std;

BTree::BTree(int ISize, int LSize):internalSize(ISize), leafSize(LSize)
{
  root = new LeafNode(LSize, NULL, NULL, NULL);
} // BTree::BTree()


void BTree::insert(const int value)
{
  BTreeNode *root2 = root;
  BTreeNode* temp;
  temp = root->insert(value);
  if(temp != NULL)
  { 

    InternalNode* new_node = new InternalNode(internalSize, leafSize, NULL, NULL, NULL);
    root = new_node->createNew(root2);
  }
    
} // BTree::insert()


void BTree::print()
{
  BTreeNode *BTreeNodePtr;
  Queue<BTreeNode*> queue(1000);

  queue.enqueue(root);
  while(!queue.isEmpty())
  {
    BTreeNodePtr = queue.dequeue();
    BTreeNodePtr->print(queue);
  } // while
} // BTree::print()

int BTree::size()
{
  return 0; 
}
