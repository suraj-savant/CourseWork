public class P06ProductExpectSelf {
    public static void main(String[] args) {
        var s = new Solution();
        int[] nums = {-1,1,0,-3,3};
        int[] ans = s.productExceptSelf(nums);
        for (int i : ans) {
            System.out.print(i + " ");
        }
    }
}


class Solution{
    public int[] productExceptSelf(int[] nums) {
    int product = 1;
    boolean hasZero = false;
    for (int i = 0; i < nums.length; i++) {
        if(nums[i] == 0){
            hasZero = true;
            continue;
        }
        product *= nums[i];
    }

    for (int i = 0; i < nums.length; i++) {
        if(hasZero){
            if(nums[i]!=0) nums[i] = 0;
            else nums[i] = product;
            continue;
        } 

        nums[i] = product/nums[i];
    }

        return nums;
       
    }
}