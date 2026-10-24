class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> SEEN = new HashSet<>();
        for (int n = 0; n<Math.min(k, nums.length); n++) {
            if(SEEN.contains(nums[n])) {
                return true;
            } else {
                SEEN.add(nums[n]);
            }
        }
        for(int i = k ; i < nums.length; i++) {
            if (SEEN.contains(nums[i])) {
                return true;
            } else { 
                SEEN.add(nums[i]);
                SEEN.remove(nums[i-k]);
            }
        }
        return false;

    }
}
