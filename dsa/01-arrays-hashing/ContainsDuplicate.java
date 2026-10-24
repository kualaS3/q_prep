class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int a : nums) {
            if (!set.contains(a)) {
                set.add(a);
            } else {
                return true;
            }
        }
        return false;
    }
}
