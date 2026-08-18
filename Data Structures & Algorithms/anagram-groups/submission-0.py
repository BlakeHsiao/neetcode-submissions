class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_dict = {}

        for i in range(len(strs)):

            curr_word = strs[i]
            alpha_word = "".join(sorted(curr_word))

            if alpha_word not in sorted_dict:
                sorted_dict[alpha_word] = [curr_word]
            else:
                sorted_dict[alpha_word].append(curr_word)
            
        return list(sorted_dict.values())


#Create a hashmap with only unique values by casting strs into a hashmap. 
#Sort each of those string values and use them as keys
#Loop through strs a second time and if any of them match a key append that word into the value array within that dictionary
#Create a new list that chronologically appends each of those values within the dictionary to a new array, which will be returned
