
class Phonebook:
    def __init__(self):
        self.entries = {}

    def add(self, name, number):
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def is_consistent(self):
        names = list(self.entries.keys())
        nums = list(self.entries.values())

            #print('orig={0} num_is_dupe={1}', original_num, num_is_dupe)
        
        def dupe_name(self, name):
            return names.count(name) > 1

        def dupe_num(self, num):
            return nums.count(num) > 1

        def dupe_prefix(self, original_num):
            prefix_is_dupe = False
            for num in nums:
                if num != original_num:
                    if num[:len(original_num)] == original_num:
                        prefix_is_dupe = True
            return prefix_is_dupe

        if len(self.entries) == 0:
            return True
        else:
            name_count = (sum(name for name in names if dupe_name(self, name)))
            num_count = (sum(num for num in nums if dupe_num(self, num)))
            prefix_count = (sum(num for num in nums if dupe_prefix(self, num)))

            #print('name_count={0} num_count={1} prefix_count={2}', name_count, num_count, prefix_count)

            return (name_count + num_count + prefix_count) == 0

    
