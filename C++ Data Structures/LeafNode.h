//Anthony Chen and Shyam Venkataraman

#ifndef LeafNodeH
#define LeafNodeH

#include "BTreeNode.h"

class LeafNode:public BTreeNode
{
  int *values;
public:
  LeafNode(int LSize, InternalNode *p, BTreeNode *left,
    BTreeNode *right);
  int getMinimum() const;
  LeafNode* insert(int value); // returns pointer to new Leaf if splits
  // else NULL
  void print(Queue <BTreeNode*> &queue);

  //my helper functions
  int isFull();
  void sort(int value);
  LeafNode* split();
  bool canPushLeft();
  bool canPushRight();
  void removeTop();
  void updateKey();
 
}; //LeafNode class

#endif
