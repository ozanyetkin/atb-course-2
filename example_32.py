from itertools import combinations

def fourSum(nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        combined_fours = set(combinations(nums, 4))
        winner_fours = set()
        for comb in combined_fours:
            if sum(comb) == target:
                winner_fours.add(comb)
        return list(winner_fours)

print(fourSum(nums = [1,0,-1,0,-2,2], target = 0))
print(fourSum([-499,-486,-479,-462,-456,-430,-415,-413,-399,-381,-353,-349,-342,-337,-336,-331,-330,-322,-315,-280,-271,-265,-249,-231,-226,-219,-216,-208,-206,-204,-188,-159,-144,-139,-123,-115,-99,-89,-80,-74,-61,-22,-22,-8,-5,4,43,65,82,86,95,101,103,123,149,152,162,165,168,183,204,209,209,220,235,243,243,244,248,253,260,273,281,284,288,290,346,378,382,384,407,411,423,432,433,445,470,476,497], target=3032))
