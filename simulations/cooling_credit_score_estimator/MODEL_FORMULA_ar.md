# ملاحظة صيغة مقدّر درجة أرصدة التبريد

تلخص هذه الملاحظة منطق التقييم الأولي المستخدم في `cooling_credit_score_estimator.py`.

## المكونات الإيجابية

يحسب النموذج المكونات الإيجابية التالية:

- درجة خفض الحرارة
- درجة التبريد التبخري
- درجة تحسن WBGT
- درجة استعادة دورة المياه
- درجة استعادة رطوبة التربة
- درجة استعادة نتح النباتات
- درجة خفض الحرارة المهدرة
- درجة استعادة قدرة النظام البيئي على التبريد

## مكونات العقوبة

يطرح النموذج:

- عقوبة إجهاد المياه
- عقوبة مخاطر الرطوبة
- عقوبة المخاطر البيئية
- عقوبة استخدام الطاقة

## البنية المفاهيمية

```text
Cooling Credit Score =
  Thermal Reduction
+ Evaporative Cooling
+ WBGT Improvement
+ Water Cycle Recovery
+ Soil Moisture Recovery
+ Vegetation Transpiration Recovery
+ Waste Heat Reduction
+ Ecological Cooling Recovery
- Water Stress Penalty
- Humidity Risk Penalty
- Ecological Risk Penalty
- Energy Use Penalty
```

## الوحدات الافتراضية

```text
gross_units = positive_score / 100 × cooled_area_m2 × duration_hours / 1000
risk_adjusted_units = gross_units × risk_adjustment × MRV quality
```

هذه وحدات محاكاة افتراضية، ولا ينبغي تفسيرها كأرصدة رسمية أو قابلة للتداول.

## المعايرة المستقبلية

تم اختيار المعاملات الأولية بهدف الشفافية، ويجب معايرتها من خلال:

- البيانات الميدانية
- برامج تجريبية بلدية
- قياسات الحساسات
- بيانات إجهاد المياه حسب المنطقة
- مراقبة WBGT والرطوبة
- تقييمات السلامة البيئية
- إجراءات MRV من طرف ثالث
