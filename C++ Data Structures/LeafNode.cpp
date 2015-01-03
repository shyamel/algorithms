//Anthony Chen and Shyam Venkataraman

#include <iostream>
#include "LeafNode.h"
#include "InternalNode.h"
#include "QueueAr.h"
#include <math.h>

using namespace std;


LeafNode::LeafNode(int LSize, InternalNode *p,
  BTreeNode *left, BTreeNode *right) : BTreeNode(LSize, p, left, right)
{
  values = new int[LSize + 1];
}  // LeafNode()



int LeafNode::getMinimum()const
{
  if(count > 0)  // should always be the case
    return values[0];
  else
    return 0;

} // LeafNode::getMinimum()

void LeafNode::print(Queue <BTreeNode*> &queue)
{

  cout << "Leaf: ";
  for (int i = 0; i < count; i++)
    cout << values[i] << ' ';
  cout << endl;
} // LeafNode::print()

int LeafNode::isFull()
{
  if(count == leafSize)
    return 1;
  else 
    return 0;

}
//----------------------My Helper Functions ------------------------ ---------//
//---------------------------------------------------------------------------//
LeafNode* LeafNode::insert(int value)
{
  int full = 0; LeafNode *temp = NULL;
  full = isFull();
 
  sort(value);
  if(full == 1)
  {
    if(canPushLeft()){
    }
    else if(canPushRight()){
    }
    else{
      temp = split();
      if(rightSibling!=NULL){
        temp->rightSibling = rightSibling;
        rightSibling->setLeftSibling(temp);
      }
      setRightSibling(temp);
    }
  }
  
  return temp; 
}  // LeafNode::insert()

//inserts the value in the appropriate position
void LeafNode::sort(int value)
{
  int i = count;
  
  if(count == 0)
    values[0] = value;
  else{
    for(i = count - 1; i > -1; i--)
    {
       
      if(value> values[i]){
        values[i + 1] = value;
        break;
      }
      else
        values[i + 1] = values[i];
      if(i == 0)
        values[0] = value;   
    }
  }//if there are things in the LeafNode 
  count++;
  
}

//splits the leaf node and connects the two
LeafNode* LeafNode::split()
{
 
  LeafNode* temp = new LeafNode(leafSize, NULL, this, NULL);
  int numberToMove = ceil(count/2.0);

  int i, move, tempCount = count;
 
  for(i = count; i > tempCount - numberToMove; i--)
  {
    move = values[i - 1];
    temp->insert(move);
   
    count--;
  }

  return temp;
}

//pawnsleft
bool LeafNode::canPushLeft()
{
  LeafNode* temp = (LeafNode*)leftSibling;
  if(temp == NULL || temp->isFull())
    return false;
  temp->insert(getMinimum()); 

  removeTop();
  updateKey();
  temp->updateKey();
  return true;
}

//pawns right
bool LeafNode::canPushRight()
{
  LeafNode* temp = (LeafNode*)rightSibling;
  if(temp == NULL || temp->isFull())
    return false;
  temp->insert(values[count - 1]);
  count--;
  
  updateKey();
  temp->updateKey();
  return true;
}

//takes top off when pawning left
void LeafNode::removeTop()
{
  int i;
  for(i = 1; i < count; i++)
  {
    values[i - 1] = values[i];
  }
  count--;
}

//updates keys when pawning off
void LeafNode::updateKey()
{
  InternalNode* temp = parent;
  for(int i = 0; i < parent->getCount(); i++)
  {
    parent->keys[i] = parent->children[i]->getMinimum();
  
  }
  if(temp!=NULL)
   temp->updateKey();
}
