public class P07PrefixSum {
    public static void main(String[] args) {
        int[] arr = {2,3,7,5};
        Solution s = new Solution();
        int [] prefixSum = s.prefixSum(arr);
        for (int i = 0; i < prefixSum.length; i++) {
            System.out.print(prefixSum[i] + " ");
        }
    }
}

class Solution{
    int[] prefixSum(int[] arr){
        for(int i=1; i<arr.length; i++){          
            arr[i] = arr[i-1] + arr[i];
        }
        
        return arr;
    }
}
