#443. 压缩字符串

class Solution:
    def compress(self, chars: List[str]) -> int:
        change_pointer = 0

        cur_char = ""
        cur_char_len = 0

        for idx in range(len(chars)):
            if chars[idx] != cur_char:
                if cur_char == "":
                    cur_char = chars[idx]
                    cur_char_len = 1

                else:
                    chars[change_pointer] = cur_char
                    change_pointer+=1
                    cur_char_len_str_list = list(str(cur_char_len))
                    if cur_char_len > 1:
                        for num in cur_char_len_str_list:
                            chars[change_pointer] = num
                            change_pointer+=1
                    cur_char = chars[idx]
                    cur_char_len = 1
            else:
                cur_char_len += 1
        
        # corner case: last
        chars[change_pointer] = cur_char
        change_pointer+=1
        cur_char_len_str_list = list(str(cur_char_len))
        if cur_char_len > 1:
            for num in cur_char_len_str_list:
                chars[change_pointer] = num
                change_pointer+=1
        return change_pointer





# 题目比较抽象，需要仔细审题
# 审题明白后就是很明显的双指针，且必定一快一慢

class Solution:
    def compress(self, chars: List[str]) -> int:
        def write_group(char: str, count: int, write_ptr: int) -> int:
            """Write a character group and return the new write pointer."""
            chars[write_ptr] = char
            write_ptr += 1
            if count > 1:
                for digit in str(count):
                    chars[write_ptr] = digit
                    write_ptr += 1
            return write_ptr
        
        write_ptr = 0
        read_ptr = 0
        
        while read_ptr < len(chars):
            cur_char = chars[read_ptr]
            count = 0
            
            # Count all consecutive same characters
            while read_ptr < len(chars) and chars[read_ptr] == cur_char:
                read_ptr += 1
                count += 1
            
            # Write this group (no special cases needed!)
            write_ptr = write_group(cur_char, count, write_ptr)
        
        return write_ptr