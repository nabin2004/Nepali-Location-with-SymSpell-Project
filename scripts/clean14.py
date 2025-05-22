import json 
original_to_simplified = {'भक्तपुर': 'भक्तपर', 'ललितपुर': 'ललतपर', 'पोखरा': 'पखर', 'विराटनगर': 'वरटनगर', 'धरान': 'धरन', 'बुटवल': 'बटवल', 'धनगढी': 'धनगढ', 'नेपालगंज': 'नपलगज', 'जनकपुर': 'जनकपर', 'बिरगंज': 'बरगज', 'सर्लाही': 'सर्लह', 'मोरङ': 'मरङ', 'रुपन्देही': 'रपन्दह', 'सिन्धुपाल्चोक': 'सन्धपल्चक', 'धादिङ': 'धदङ', 'रसुवा': 'रसव', 'सिन्धुली': 'सन्धल', 'सुकेकोट': 'सककट', 'सुकेटार': 'सकटर', 'सुकेधारा': 'सकधर', 'पशुपतिनाथ': 'पशपतनथ', 'सिंहदरबार': 'सहदरबर', 'नारायणहिटी': 'नरयणहट', 'त्रिपुरेश्वर': 'त्रपरश्वर', 'बौद्ध': 'बद्ध'}


# Reverse: value-to-key dictionary
simplified_to_original = {v: k for k, v in original_to_simplified.items()}

with open("original_to_simplified.json", "w", encoding="utf-8") as f1:
    json.dump(original_to_simplified, f1, ensure_ascii=False, indent=2)

with open("simplified_to_original.json", "w", encoding="utf-8") as f2:
    json.dump(simplified_to_original, f2, ensure_ascii=False, indent=2)

print("Dictionaries saved successfully.")