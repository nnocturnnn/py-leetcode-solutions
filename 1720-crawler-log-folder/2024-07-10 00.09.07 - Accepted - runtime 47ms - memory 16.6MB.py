class Solution:
    def minOperations(self, logs: List[str]) -> int:
        operations_count = 0
        for operation in logs:
            if operation == "../":
                if operations_count:
                    operations_count -= 1 
            elif operation == "./":
                continue
            else:
                operations_count += 1
        return operations_count