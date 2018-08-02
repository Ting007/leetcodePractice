import java.io.PrintStream;
import java.util.*;
import java.util.List;
import java.util.Arrays;
class TransMatrix{
	public static int[][] transpose(int[][] A){
		int a = A.length, b = A[0].length;
		int[][] transM = new int[a][b];
		for (int i = 0; i < b; i++){
			for (int j = 0; j < a; j++){
				transM[i][j]=A[j][i];

			}
		}
		return transM;
	}


	public static void main(String[] args){
		int[][] M = {{1,2,3},{4,5,6},{7,8,9}};
		int[][] x = transpose(M);
		System.out.println(Arrays.deepToString(x));
	}

}