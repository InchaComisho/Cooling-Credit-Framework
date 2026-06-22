# مقدّر درجة أرصدة التبريد

## نموذج محاكاة أولي بلغة Python لتقدير Cooling Credit Score

يوفر هذا المجلد نموذجًا أوليًا غير اعتمادي لتقدير **Cooling Credit Score** أو درجة أرصدة التبريد.

يسمح النموذج للشركات والبلديات والباحثين ومصممي المشاريع بإدخال قيم على مستوى المشروع، ثم الحصول على تقدير أولي للمساهمة في التبريد، والأداء بعد تعديل المخاطر، ووحدات تبريد افتراضية غير رسمية.

هذا النموذج ليس أداة اعتماد رسمية. إنه أداة شفافة للتقييم الأولي، وتصميم MRV، والمقارنة بين السيناريوهات، ومحاكاة السياسات.

---

## الهدف

يهدف مقدّر درجة أرصدة التبريد إلى تحويل مفهوم أرصدة التبريد إلى نموذج عددي قابل للتجربة.

يقيم النموذج:

- خفض الحرارة
- التبريد التبخري
- تحسن مؤشر WBGT
- استعادة دورة المياه
- استعادة رطوبة التربة
- استعادة نتح النباتات
- خفض الحرارة المهدرة
- استعادة قدرة النظام البيئي على التبريد

كما يطبق عقوبات على:

- إجهاد المياه
- مخاطر الرطوبة أو تفاقم WBGT
- المخاطر البيئية
- استخدام الطاقة

الغاية هي جعل مفهوم أرصدة التبريد قابلًا للاختبار والمقارنة والتوسيع قبل إنشاء أي نظام رسمي للاعتماد.

---

## تنبيه مهم

ينتج هذا النموذج **نتائج محاكاة أولية وغير معتمدة**.

لا يقوم النموذج بإصدار أرصدة قانونية أو قابلة للتداول أو معترف بها رسميًا.

ينبغي تفسير القيم الناتجة على أنها:

- تقديرات أولية
- مؤشرات للمقارنة بين المشاريع
- دعم لتصميم MRV
- مخرجات لمحاكاة السياسات
- مؤشرات بحثية وتعليمية

إصدار أرصدة رسمية يتطلب معيارًا مؤسسيًا، وتحققًا من طرف ثالث، وضمانات بيئية، ومعايرة إقليمية، ومراقبة طويلة الأمد.

---

## بنية الملفات

```text
simulations/cooling_credit_score_estimator/
  cooling_credit_score_estimator.py
  README.md
  README_ja.md
  README_ar.md
  example_inputs.csv
  example_results.csv
```

---

## طريقة التشغيل

من جذر المستودع:

```bash
python simulations/cooling_credit_score_estimator/cooling_credit_score_estimator.py \
  --input simulations/cooling_credit_score_estimator/example_inputs.csv \
  --output simulations/cooling_credit_score_estimator/results/cooling_credit_score_results.csv \
  --json-output simulations/cooling_credit_score_estimator/results/cooling_credit_score_results.json \
  --print-summary
```

لا يحتاج النموذج إلى حزم Python خارجية.

---

## أعمدة ملف الإدخال

يجب أن يحتوي ملف CSV على الأعمدة التالية:

| العمود | المعنى |
|---|---|
| `project_id` | معرف المشروع |
| `project_name` | اسم المشروع |
| `technology_type` | نوع التقنية أو فئة التنفيذ |
| `baseline_air_temp_c` | درجة حرارة الهواء قبل التنفيذ |
| `reduced_air_temp_c` | درجة حرارة الهواء بعد التنفيذ |
| `baseline_surface_temp_c` | درجة حرارة السطح قبل التنفيذ |
| `reduced_surface_temp_c` | درجة حرارة السطح بعد التنفيذ |
| `baseline_wbgt_c` | WBGT قبل التنفيذ |
| `reduced_wbgt_c` | WBGT بعد التنفيذ |
| `cooled_area_m2` | مساحة التبريد |
| `duration_hours` | مدة التنفيذ أو التشغيل |
| `water_used_liters` | كمية المياه المستخدمة |
| `evaporated_water_liters` | كمية المياه المتبخرة المقدرة |
| `recycled_water_ratio` | نسبة مياه الأمطار أو المياه المعاد تدويرها، 0–1 أو 0–100 |
| `electricity_used_kwh` | استهلاك الكهرباء |
| `soil_moisture_before_pct` | رطوبة التربة قبل التنفيذ |
| `soil_moisture_after_pct` | رطوبة التربة بعد التنفيذ |
| `vegetation_cover_before_pct` | الغطاء النباتي قبل التنفيذ |
| `vegetation_cover_after_pct` | الغطاء النباتي بعد التنفيذ |
| `waste_heat_reduction_kwh` | خفض الحرارة المهدرة المقدّر |
| `water_stress_level` | مستوى إجهاد المياه الإقليمي، 0–1 أو 0–100 |
| `humidity_risk_level` | مستوى مخاطر الرطوبة أو WBGT، 0–1 أو 0–100 |
| `ecological_risk_level` | مستوى المخاطر البيئية، 0–1 أو 0–100 |
| `mrv_data_quality` | جودة بيانات MRV، 0–1 أو 0–100 |

---

## مؤشرات الإخراج

ينتج النموذج:

- `thermal_reduction_score`
- `evaporative_cooling_score`
- `wbgt_improvement_score`
- `water_cycle_recovery_score`
- `soil_moisture_recovery_score`
- `vegetation_transpiration_score`
- `waste_heat_reduction_score`
- `ecological_cooling_score`
- `water_stress_penalty`
- `humidity_risk_penalty`
- `ecological_risk_penalty`
- `energy_use_penalty`
- `positive_score_before_penalties`
- `total_penalty`
- `cooling_credit_score`
- `gross_cooling_credit_units`
- `risk_adjusted_cooling_credit_units`
- `scenario_grade`
- `mrv_reliability_level`
- `warnings`

---

## الصيغة المفاهيمية

يتبع النموذج البنية المفاهيمية التالية:

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

---

## وحدات أرصدة تبريد افتراضية

يحسب السكربت أيضًا وحدات افتراضية:

```text
gross_units = positive_score / 100 × cooled_area_m2 × duration_hours / 1000
risk_adjusted_units = gross_units × risk_adjustment × MRV quality
```

هذه الوحدات ليست أرصدة رسمية. إنها وحدات محاكاة نسبية للمقارنة وتصميم السياسات.

---

## الاستخدامات الممكنة

يمكن استخدام هذا النموذج في:

- مقارنة مشاريع الرذاذ الحضري
- تقدير فوائد تبريد التربة المتجددة
- تقييم مشاريع استعادة الغابات أو الغطاء النباتي
- تقييم نماذج استصلاح الصحراء
- الفحص الأولي لمفاهيم OTU أو تبريد المحيط
- تصميم برامج تجريبية لأرصدة التبريد في البلديات
- إعداد متطلبات MRV لمشاريع التبريد الخاصة بالشركات

---

## المؤلف

Master / inchacomusho / InchaComisho

---

## الرخصة

Creative Commons Attribution 4.0 International (CC BY 4.0)
