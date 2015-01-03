//Anthony Chen and Shyam Venkataraman

#include <iostream>
#include "InternalNode.h"
#include <math.h>
using namespace std;

InternalNode::InternalNode(int ISize, int LSize,
  InternalNode *p, BTreeNode *left, BTreeNode *right) :
  BTreeNode(LSize, p, left, right), internalSize(ISize)
{
  keys = new int[internalSize + 1]; // keys[i] is the minimum of children[i]
  children = new BTreeNode* [ISize + 1];
} // InternalNode::InternalNode()


int InternalNode::getMinimum()const
{
  if(count > 0)   // should always be the case
    return children[0]->getMinimum();
  else
    return 0;
} // InternalNode::getMinimum()





void InternalNode::print(Queue <BTreeNode*> &queue)
{
  int i;

  cout << "Internal: ";
  for (i = 0; i < count; i++)
    cout << keys[i] << ' ';
  cout << endl;

  for(i = 0; i < count; i++)
    queue.enqueue(children[i]);

} // InternalNode::print()


//----------------------------------------------//
                 //MY FUNCTIONS//
//----------------------------------------------//

void InternalNode::insert(BTreeNode *oldRoot, BTreeNode *node2)
{ // Node must be the root, and node1
  // students must write this
} // InternalNode::insert()

InternalNode* InternalNode::insert(int value)
{
 
  int pos; bool full = isFull();
  BTreeNode *temp = NULL;

  for(pos = count - 1; pos > -1; pos--){
    if(value > keys[pos])
      break;
  }
  if(pos == -1) //find the positions to insert to
   pos = 0;
  temp = children[pos]->insert(value);
  keys[pos] = children[pos]->getMinimum(); //reupdate minimum

 
  updateKey();
  if(temp == NULL)
    return NULL; //quit if the value inserted with no splits
  
  sort(temp);
  temp=NULL;
  if(full)
  {
     if(canPushLeft()){
     }
     else if(canPushRight()){
     }
     else{
       temp = split();
       if(rightSibling!=NULL){
         temp->setRightSibling(rightSibling);
         rightSibling->setLeftSibling(temp);
       }
     }
     setRightSibling(temp);
    
  }
  InternalNode* temp2 = (InternalNode*)temp;
  updateKey();
  return temp2; 
} // InternalNode::insert()

void InternalNode::insert(BTreeNode *newNode) // from a sibling
{
  // students may write this
} // InternalNode::insert()

//Insert a new LeafNode into Internal Node
void InternalNode::sort(BTreeNode *temp)
{
  int i = count;
  if(count == 0)
  {
    keys[0] = temp->getMinimum();
    children[0] = temp;
    count++;
    return;
  }
  for(i = count - 1; i > -1; i--)
  {  
    
    if(temp->getMinimum() > keys[i])
    {
      keys[i + 1] = temp->getMinimum();
      children[i + 1] = temp;
      temp->setParent(this);
      break;
    }
    else
    {
      keys[i + 1] = keys[i];
      children[i + 1] = children[i];
    }
    if(i == 0)
    {
      keys[0] = temp->getMinimum();
      children[0] = temp;
      temp->setParent(this);
    }
  }
  count++;
}

InternalNode* InternalNode::split()
{
  InternalNode* temp = new InternalNode(internalSize, leafSize, NULL, this, NULL);
  int numberToMove = ceil(count/2.0);

  int i, tempCount = count;

  for(i = count; i > tempCount - numberToMove; i--)
  {
    temp->sort(children[i -1]);
    count--;
  }
  return temp;
}

InternalNode* InternalNode::createNew(BTreeNode* root)
{
 
  int i = 0;
  while(root != NULL)
  {
    children[i] = root;
    keys[i] = root->getMinimum();
    i++;
    count++; 
    root->setParent(this);  
    root = root->getRightSibling();
  }
  
  return this;
}

bool InternalNode::isFull()
{ 
  if(internalSize == count)
    return true;
  return false;
}

bool InternalNode::canPushLeft()
{
  InternalNode* temp = (InternalNode*)leftSibling;
  if(temp==NULL || temp->isFull())
    return false;
  temp->sort(children[0]);
  
  removeLeft();
  updateKey();
  temp->updateKey();
  return true;
}

bool InternalNode::canPushRight()
{
  InternalNode* temp = (InternalNode*)rightSibling;
  if(temp == NULL || temp->isFull())
    return false;
  temp->sort(children[count - 1]);
  count--;
  updateKey();
  temp->updateKey();
  return true;
}

void InternalNode::removeLeft()
{
  int i;
  for(i = 1; i < count; i++)
  {
    keys[i - 1] = keys[i];
    children[i - 1] = children[i];    
  }
  count--;
}


void InternalNode::updateKey()
{
  InternalNode* temp = parent;
  if(temp == NULL)
    return;
  for(int i = 0; i < parent->getCount(); i++)
  {
    parent->keys[i] = parent->children[i]->getMinimum();

  }
  if(temp!=NULL)
   temp->updateKey();
}

