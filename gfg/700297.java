/* Link list Node 
class Node
{
	Node next;
	int data;
	
	Node(int d)
	{
		data = d;
		next = null;
	}
} */

class GfG
{
    /*You are required to complete this method*/
    Node delete(Node head, int k)
    {
        int i = 0;
    	Node current = head;
    	Node previous = null;
    	while(current != null) {
    	    i++;
    	    if(i == k) {
    	        previous.next = current.next;
    	        i = 0;
    	    }
    	    previous = current;
    	    current = current.next;
    	}
    	return head;
    }
}

