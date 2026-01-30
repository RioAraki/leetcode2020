class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        word_list.reverse()
        return " ".join(word_list)

# 忘记了 split 会保留 empty string
# 不知道 split 默认就会 split by any whitespace and treat multiple whitespace as one and strip the whitespace
# 忘记了 reverse 是原地翻转，不是返回新的列表
# 正确表达lambda的方式：