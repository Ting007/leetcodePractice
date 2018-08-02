import java.lang.*;
import java.util.*;
import java.lang.String;
class Solution {
    public int primePalindrome(int N) {
        if (N == 1)
            return 2;
        if (isPalindrome(N) && isPrime(N)){
            return N;
        }
        else{
            N += 1;
            if (10_000_000 < N && N < 100_000_000)
                N = 100_000_001;
            return primePalindrome(N);
        }
    }
    public boolean isPrime(int N){
        double limit = Math.sqrt(N);
        for (int i = 2; i <= limit; i++){
            if (N % i == 0){
                return false;
            }
        }
        return true;
    }
    public boolean isPalindrome(int N){
        if(N < 12){
            return true;
        }
        if (N < 100){
            return false;
        }
        int rev = 0;
        int origin = N;
        while (N>0){
            int i = (N % 10);
            rev = rev*10 + i;
            N = (int)(N/10);
        }
        return  origin == rev;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int N = Integer.parseInt(line);
            
            int ret = new Solution().primePalindrome(N);
            
            String out = String.valueOf(ret);
            
            System.out.print(out);
        }
    }
    
}