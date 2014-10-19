
import java.util.*;

public class Sorts{
  private long steps;

  public Sorts(){
    steps = 0;
  }

  public void bubbleSort(ArrayList <Comparable> list){
	for(int outer = 0; outer < list.size(); outer++){
		for(int inner=0; inner< list.size() -1 ; inner++){
			steps++;
			if(list.get(inner).compareTo(list.get(inner+1)) > 0){
				swap(list, inner, inner+ 1);
			}

		}
	}
  }

  public void selectionSort(ArrayList <Comparable> list){
	
	int possible = list.size() - 1;
	for( int outer = 0; outer < list.size(); outer++){
		int largeIndex = 0;
		for(int inner = 0; inner < possible; inner++){
			steps++;
			if(list.get(inner).compareTo(list.get(largeIndex)) > 0)
				largeIndex = inner;
		}
		swap(list, largeIndex, possible);
		possible --;
	}
  }

  public void insertionSort(ArrayList <Comparable> list){
  		for (int outer = 1; outer < list.size(); outer++){
    		int position = outer;
    		Comparable key = list.get(position);

    // Shift larger values to the right
    		while (position > 0 && list.get(position - 1).compareTo(key) > 0){
      			list.set(position, list.get(position - 1));
      			steps++;
     	 		position--;
    		}
    		list.set(position, key);
    		steps++;
  		}

  }
  

    public long getStepCount(){
    return steps;
  }

  public void setStepCount(long stepCount){
    steps = stepCount;
  }

  public void swap(ArrayList <Comparable> list, int a, int b){
	Comparable temp1 = list.get(a);
	Comparable temp2 = list.get(b);

	list.set(a, temp2);
	steps ++;
	list.set(b, temp1);
	steps ++;
  }
}
