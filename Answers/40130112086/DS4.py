def MergeSorte(nums1,nums2):
    merge= []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merge.append(nums1[i])
            i += 1
        else:
            merge.append(nums2[j])
            j += 1
    while i < len(nums1):
        merge.append(nums1[i])
        i += 1
    while j < len(nums2):
        merge.append(nums2[j])
        j += 1
    return merge
