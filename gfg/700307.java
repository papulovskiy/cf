/* A Binary Tree node
class Node
{
    int data;
    Node left, right;

    Node(int item)
    {
        data = item;
        left = right = null;
    }
}
*/

class GfG
{
    int max_depth(Node node) {
        if(node == null) {
            return 0;
        }
        int left_depth = this.max_depth(node.left);
        int right_depth = this.max_depth(node.right);
        if(left_depth > right_depth) {
            return left_depth + 1;
        } else {
            return right_depth + 1;
        }
    }
    boolean check(Node root)
    {
        if(root == null) {
            return true;
        }
        int left_depth = this.max_depth(root.left);
        int right_depth = this.max_depth(root.right);
        if(left_depth > 0 && right_depth == 0) {
            return this.check(root.left);
        }
        if(left_depth == 0 && right_depth > 0) {
            return this.check(root.right);
        }
        if(left_depth > 0 && right_depth > 0) {
            return left_depth == right_depth;
        }
        return true;
    }
}
