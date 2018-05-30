
class Solution{
	public int numTrees(int n){
		int [] result = new int[n+1];
		result[0] = 1;
		result[1] = 1;
		for (int i =2; i <= n; i++){
			for (int j = 0; j < i; j++){
				result[i] += result[i-j-1]*result[j];
			}
		}
		return result[n];
	}
	


	public static void main(String[] args){
     	Solution foo = new Solution();
     	System.out.println(foo.numTrees(4));
	}
}