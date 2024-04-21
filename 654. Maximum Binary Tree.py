                
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(nums):
            if nums is None:
                return None
            
            new_val = max(nums)
            node= TreeNode(new_val)
            split_index = nums.index(new_val) # grabbing the index of max value
            prefix = nums[:split_index] # slicing out everything before the max value
            suffix = nums[split_index+1:] # slicing out everything after the max value

            if len(prefix):
                node.left = dfs(prefix)
            if len(suffix):
                node.right = dfs(suffix)

            return node
        
        return dfs(nums)