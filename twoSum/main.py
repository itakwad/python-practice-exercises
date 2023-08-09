def twoSum(nums, target):
    # إنشاء خريطة فارغة لتخزين العناصر وفهرستها
    num_map = {}
    
    # تفحص كل عنصر في المصفوفة
    for i, num in enumerate(nums):
        # حساب العدد المطلوب للوصول إلى الهدف
        complement = target - num
        
        # التحقق من وجود العدد المطلوب في الخريطة
        if complement in num_map:
            # إرجاع الفهرس الحالي والفهرس المخزن في الخريطة لهذا العدد
            return [num_map[complement], i]
        
        # إضافة العنصر الحالي وفهرسته إلى الخريطة
        num_map[num] = i
    
    # في حالة عدم العثور على أي زوج
    raise ValueError("No two sum solution found.")

# تجربة الحل على المثال المعطى
nums = [3, 7, 11, 15]
target = 26
result = twoSum(nums, target)
print(result)