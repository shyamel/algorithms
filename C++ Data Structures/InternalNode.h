//Anthony Chen and Shyam Venkataraman

#ifndef InternalNodeH
  #define InternalNodeH

#include "BTreeNode.h"

class InternalNode:public BTreeNode
{
public:
  int internalSize;
  BTreeNode **children;
  int *keys;

  InternalNode(int ISize, int LSize, InternalNode *p,
    BTreeNode *left, BTreeNode *right);
  int getMinimum()const;
  InternalNode* insert(int value); // returns pointer to new InternalNode
    // if it splits else NULL
  void insert(BTreeNode *oldRoot, BTreeNode *node2); // if root splits use this
  void insert(BTreeNode *newNode); // from a sibling
  void print(Queue <BTreeNode*> &queue);

  //----------my helper functions-------------------//
  InternalNode* createNew(BTreeNode* root);
  int getCount(){return count;}
  bool isFull();
  void sort(BTreeNode* temp);
  InternalNode* split(); 
  bool canPushLeft();
  bool canPushRight();
  void removeLeft();
  void updateKey();
}; // InternalNode class

#endif
