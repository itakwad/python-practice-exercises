##لحل هذه المسألة، يمكن استخدام تقنية البحث عن الأزواج (Pair Sum) في المصفوفة. يمكن استخدام خوارزمية بسيطة لحل المسألة وفقًا للخطوات التالية:

1. قم بإنشاء خريطة (Map) فارغة لتخزين العناصر الموجودة في المصفوفة وفهرستها.
2. قم بتفحص كل عنصر في المصفوفة بالتسلسل.
3. قم بحساب العدد المطلوب للوصول إلى الهدف من خلال طرح العنصر الحالي من الهدف. مثلاً، إذا كان الهدف هو 9 والعنصر الحالي هو 2، فإن العدد المطلوب هو 9 - 2 = 7.
4. تحقق مما إذا تم العثور على العدد المطلوب في الخريطة. إذا تم العثور عليه، فهذا يعني أن لدينا زوجًا يمكن أن يضيف إلى الهدف.
5. إذا تم العثور على العدد المطلوب في الخريطة، فقم بإرجاع الفهرس الحالي والفهرس المخزن في الخريطة لهذا العدد.
6. إذا لم يتم العثور على العدد المطلوب في الخريطة، فقم بإضافة العنصر الحالي وفهرسته إلى الخريطة.
7. إذا انتهى اللوب دون العثور على أي زوج، فهذا يعني أنه لا يوجد حلاً ممكنًا، ويمكن إلقاء استثناء أو إرجاع قيمة خاصة.

تطبيقًا على المثال الذي أعطيته:

المصفوفة: [2, 7, 11, 15]
الهدف: 9

1. يتم إنشاء خريطة فارغة.
2. يتم التحقق من العنصر الأول في المصفوفة (2).
3. العدد المطلوب: 9 - 2 = 7.
4. لم يتم العثور على العدد 7 في الخريطة.
5. يتم إضافة العنصر 2 إلى الخريطة مع الفهرس 0.
6. يتم التحقق من العنصر الثاني في المصفوفة (7).
7. العدد المطلوب: 9 - 7 = 2.
8. يتم العثور على العدد 2 في الخريطة بفهرس 0.
9. يتم إرجاع الفهرسين [0, 1].

وبالتالي، الإجابة النهائية هي [0, 1]، حيث أن مجموع العنصرين في هذه الفهرسين يساوي الهدف (9).

هذا هو الحل المطلوب لهذه المسألة. يمكن تنفيذه باستخدام لغة البرمجة التي تفضلها، وهو يعمل بكفاءة بمعدل زمعدل زمني يعادل O(n)، حيث n هو حجم المصفوفة.
## حل مسألة البحث عن الأزواج في البايثون

يمكن استخدام تقنية البحث عن الأزواج (Pair Sum) في البايثون لحل هذه المسألة. يمكن تنفيذها باستخدام الخوارزمية التالية:

```python
def find_pair_sum(nums, target):
    num_map = {}  # خريطة لتخزين العناصر الموجودة وفهرستها
    
    for i, num in enumerate(nums):
        complement = target - num  # العدد المطلوب للوصول إلى الهدف
        
        if complement in num_map:
            # تم العثور على العدد المطلوب في الخريطة
            return [num_map[complement], i]
        
        # إضافة العنصر الحالي وفهرسته إلى الخريطة
        num_map[num] = i
    
    # لم يتم العثور على أي زوج
    return None
```

الآن يمكنك استدعاء الدالة `find_pair_sum` وتمرير المصفوفة والهدف للحصول على الزوج المطلوب. على سبيل المثال:

```python
nums = [2, 7, 11, 15]
target = 9

result = find_pair_sum(nums, target)
if result:
    print("الزوج المطلوب:", result)
else:
    print("لا يوجد حلاً ممكنًا.")
```

ستتم طباعة الزوج المطلوب `[0, 1]` في هذا المثال، حيث أن مجموع العنصرين في هذه الفهرسين يساوي الهدف (9).

يمكنك استخدام هذا الحل كنقطة انطلاق لتطوير تطبيقك أو بناء واجهة مستخدم تفاعلية حسب احتياجاتك.